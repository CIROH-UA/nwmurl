from tqdm import tqdm
import requests

def check_valid_urls(file_list, session=None):
    t = tqdm(range(len(file_list)))
    valid_file_list = [check_url(file_name, t) for file_name in file_list]
    return [file for file in valid_file_list if file is not None]

def check_url(file, t):
    filename = file.split("/")[-1]
    try:
        with requests.head(file) as response:
            if response.status_code == 200:
                t.set_description(f"Found: {filename}")
                t.update(1)
                t.refresh()
                return file
            else:
                t.set_description(f"Not Found: {filename}")
                t.update(1)
                t.refresh()
                return None
    except requests.exceptions.RequestException:
        t.set_description(f"Not Found: {filename}")
        t.update(1)
        t.refresh()
        return None
