'''
Created on Jun 8, 2018

@author: runshengsong
'''
# TO DO
# move settings to config
import sys
import base64
import numpy as np

import boto
import os
from boto.s3.key import Key
from boto.exception import S3ResponseError

DOWNLOAD_LOCATION_PATH = os.path.expanduser("~") + "/s3-backup/"

def base64_encode_image(a):
    """
    encode the image
    """
    # base64 encode the input NumPy array
    return base64.b64encode(a).decode("utf-8")

def base64_decode_image(a, dtype, shape):
    """
    decode the image
    """
    # convert the string to a NumPy array using the supplied data
    # type and target shape
    a = np.frombuffer(base64.decodestring(a), dtype=dtype)
    a = a.reshape(shape)

    # return the decoded image
    return a

def down_load_a_dir_from_s3(bucket_url, local):
    """
    download the folder from S3 
    
    local: /src/tmp/model_data/
    """
    pass
    
    