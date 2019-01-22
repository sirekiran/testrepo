'''Author : Sireesha Palnati'''
'''Date : 22-Jan-2019'''
'''Description : This test main funda is to make a call to some API and read the response to assert some values from respective keys'''

###Import all the packages required
import requests
import json

name_field = "Carbon credits"
promotions_gallery_text = "2x larger image"

### Making an API call
response = requests.get("https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false")
### Convert response type to accessible json format without unicode values
response = response.json()

###Assertions for the required key values pairs###
assert(response['Name'].encode("utf-8") == name_field)
assert(response['CanRelist'] == True)
for i in range(0, len(response['Promotions'])):
    if(response['Promotions'][i]['Name'] == "Gallery"):
        assert(promotions_gallery_text in response['Promotions'][i]['Description'])
print("All the Assertions are successful")















