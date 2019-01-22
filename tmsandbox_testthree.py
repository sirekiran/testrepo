'''Author : Sireesha Palnati'''
'''Date : 22-Jan-2019'''
'''Description : This test main funda is to make a call to some API and read the response to assert some values from respective keys'''

###Import all the packages required
import requests
import logging
import json
import os

name_field = "Carbon credits Carbon credits"
promotions_gallery_text = "2x larger image 2x larger image"
report_file = "report.txt"

### Making an API call
response = requests.get("https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false")
### Convert response type to accessible json format without unicode values
response = response.json()

###Creating a file to log errors###
try:
    os.remove(report_file)
except OSError:
    pass
file  = open(report_file, 'w')


###Assertions for the required key values pairs###
try:
    assert(response['Name'].encode("utf-8") == name_field)
except AssertionError, e:
    file.write(str(e) + " seen for Name field assertions since expected is " + name_field + " but actual is " + response['Name'].encode("utf-8") + "\n")
    logging.error(str(e) + " seen for Name field assertions since expected is " + name_field + " but actual is " + response['Name'].encode("utf-8"))
try:
   assert(response['CanRelist'] == False)
except AssertionError, e:
    file.write(str(e) + " seen for CanRelist field assertions since expected is False while actual is "+ str(response['CanRelist']) + "\n")
    logging.error(str(e) + " seen for CanRelist field assertions since expected is False while actual is "+ str(response['CanRelist']))
try:
    for i in range(0, len(response['Promotions'])):
        if(response['Promotions'][i]['Name'].encode("utf-8") == "Gallery"):
            assert(promotions_gallery_text in response['Promotions'][i]['Description'].encode("utf-8"))
except AssertionError, e:
    file.write(str(e) + " seen for Gallery description since expected subtext is " + promotions_gallery_text + " but actual is " + response['Promotions'][i]['Description'].encode("utf-8") + "\n")
    logging.error(str(e) + " seen for Gallery description since expected subtext is " + promotions_gallery_text + " but actual is " + response['Promotions'][i]['Description'].encode("utf-8"))
print("All the Assertions verification are successful with catching exceptions")
file.close()














