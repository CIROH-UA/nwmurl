from tqdm import tqdm
import requests

from functools import partial
import gevent


def check_valid_urls(file_list, session=None, visualize_progress=True):
    """if not session:
    session = requests.Session()"""
    t = tqdm(range(len(file_list))) if visualize_progress else None
    check_url_part = partial(check_url, t)
    """with ThreadPoolExecutor(max_workers=10) as executor:
        valid_file_list = list(executor.map(check_url_part, file_list))"""
    valid_file_list = [
        gevent.spawn(check_url_part, file_name) for file_name in file_list
    ]
    gevent.joinall(valid_file_list)
    return [file.get() for file in valid_file_list if file.get() is not None]


def check_url(t, file):
    filename = file.split("/")[-1]
    try:
        with requests.head(file, allow_redirects=True) as response:
            if response.status_code == 200:
                if t:
                    t.set_description(f"Found: {filename}")
                    t.update(1)
                    t.refresh()
                return file
            else:
                # print(f"Not Found: {filename} (Status Code: {response.status_code})")
                if t:
                    t.set_description(f"Not Found: {filename}")
                    t.update(1)
                    t.refresh()
                return None
        # response = session.head(file, timeout=1)
    except requests.exceptions.RequestException:
        if t:
            t.set_description(f"Not Found: {filename}")
            t.update(1)
            t.refresh()
        return None
