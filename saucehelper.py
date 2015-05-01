'''
This library is not supported by Sauce Labs. It merely servers as an
example on send data to the Sauce Labs API.
'''
 
import requests
import json
import time
 
# Can be used to time different selenium commands
def timeit(f):

    def timed(*args, **kw):
 
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
 
        print 'func:%r args:[%r, %r] took: %2.4f sec' % \
        (f.__name__, args, kw, te-ts)
        return result
 
    return timed
        # Set the status of a test to pass or fail status can be passed or failed.
def reportStatus(status, session_id, user_id, access_key):
    hdrs = {"Content-Type": "text/json"}
    payload = {"passed" : status}
    r = requests.put("http://" + user_id + ":" + access_key + "@saucelabs.com/rest/v1/" + user_id + "/jobs/" + session_id, headers=hdrs, data=json.dumps(payload))
 
def reportCustom(custom_data, session_id, user_id, access_key):
    hdrs = {"Content-Type": "text/json"}
    payload = {"custom-data" : custom_data}
    r = requests.put("http://" + user_id + ":" + access_key + "@saucelabs.com/rest/v1/" + user_id + "/jobs/" + session_id, headers=hdrs, data=json.dumps(payload))
 
# from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time, unittest, sys, saucehelper, copy
import wd.parallel