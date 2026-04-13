import unittest
from nwmurl.urlgennwm import create_file_list
from nwmurl.validation_util import check_valid_urls

def assumed_valid_args():
    """
    This function produced valid args for the create_file_list function
    on April 13th, 2026. 
    If related tests fail, data may have been destroyed or moved, and the args may need to be updated.
    """
    start_date = "202310150000"
    end_date = "202310150000"
    fcst_cycle = [0, 8]
    lead_time = [1, 18]
    varinput = 1
    geoinput = 1
    runinput = 1
    urlbaseinput = 4
    meminput = 0
    return {
        "start_date": start_date,
        "end_date": end_date,
        "fcst_cycle": fcst_cycle,
        "lead_time": lead_time,
        "varinput": varinput,
        "geoinput": geoinput,
        "runinput": runinput,
        "urlbaseinput": urlbaseinput,
        "meminput": meminput,
    }

class TestURLValidation(unittest.TestCase):
    # Need to check that it works for each of the 7 urlbaseinput options
    
    def try_test_for_urlbaseinput(self, urlbaseinput_value):
        # Get the default input args that should produce valid urls
        args = assumed_valid_args()
        
        # Adjust the urlbaseinput to point to the retrospective 2.1 data
        args["urlbaseinput"] = urlbaseinput_value
        
        # Create the file list using the provided args
        file_list = create_file_list(**args)
        
        # Check the validity of the URLs in the file list
        valid_urls = check_valid_urls(file_list, visualize_progress=False)
        
        # Check that all of the expected URLs are included in the valid URLs
        for url in file_list:
            self.assertIn(url, valid_urls, f"URL invalid. {len(valid_urls)}/{len(file_list)} URLs were valid.")
    
    # Note: the first urlbaseinput option (1) is currently not working, likely due to data being moved or deleted.
    # # 1: "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/",
    # def test_validate_for_urlbaseinput_1(self):
    #     self.try_test_for_urlbaseinput(1)
         
    # Note: the second urlbaseinput option (2) is currently not working, likely due to data being moved or deleted.
    # # 2: "https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/post-processed/WMS/",
    # def test_validate_for_urlbaseinput_2(self):
    #     self.try_test_for_urlbaseinput(2)
            
    # 3: "https://storage.googleapis.com/national-water-model/",
    def test_validate_for_urlbaseinput_3(self):
        self.try_test_for_urlbaseinput(3)
    
    # 4: "https://storage.cloud.google.com/national-water-model/",
    def test_validate_for_urlbaseinput_4(self):
        self.try_test_for_urlbaseinput(4)
    
    # Note: the fifth urlbaseinput option (5) is currently not working, likely due to data being moved or deleted.
    # # 5: "gs://national-water-model/",
    # def test_validate_for_urlbaseinput_5(self):
    #     self.try_test_for_urlbaseinput(5)
    
    # Note: the sixth urlbaseinput option (6) is currently not working, likely due to data being moved or deleted.
    # # 6: "gcs://national-water-model/",
    # def test_validate_for_urlbaseinput_6(self):
    #     self.try_test_for_urlbaseinput(6)
    
    # Note: the seventh urlbaseinput option (7) is currently not working, likely due to data being moved or deleted.
    # # 7: "https://noaa-nwm-pds.s3.amazonaws.com/",
    # def test_validate_for_urlbaseinput_7(self):
    #     self.try_test_for_urlbaseinput(7)
        
    # Note: the eighth urlbaseinput option (8) is currently not working, likely due to data being moved or deleted.
    # # 8: "s3://noaa-nwm-pds/",
    # def test_validate_for_urlbaseinput_8(self):
    #     self.try_test_for_urlbaseinput(8)
                
    # 9: "https://ciroh-nwm-zarr-copy.s3.amazonaws.com/national-water-model/",
    def test_validate_for_urlbaseinput_9(self):
        self.try_test_for_urlbaseinput(9)