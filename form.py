#!/usr/bin/env python

import sys, os
from selenium import webdriver

try:
    if len(sys.argv) < 2:
        os.write(2, b"Usage: form.py [link]\n")
        exit()
    browser = webdriver.Firefox()
    browser.get(sys.argv[1])
    names = browser.find_elements_by_class_name("office-form-question-title")
    fields = browser.find_elements_by_tag_name("input")
    if len(fields) == 2:
        if names[0].text == "1.\nName" or names[0].text == "1.\nname":
            fields[0].send_keys("Sachin Mudaliyar")
            fields[1].send_keys("41")
        else:
            fields[0].send_keys("41")
            fields[1].send_keys("Sachin Mudaliyar")
    else:
        fields[0].send_keys("41")
    browser.find_element_by_tag_name("button").click()
    print("Done, Successfully")
    browser.close()

except Exception as e:
    browser.close()
    print("Oops!", e.__class__, "occured") 
    exit()
