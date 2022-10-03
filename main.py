# importing required modules
import requests, json, os

#globals
my_key=os.environ['api_key']
  
# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
  
# The text string on which to search
query = input('Search query: ')
  
# get method of requests module
# return response object
r = requests.get(url + 'query=' + query +
                        '&key=' + my_key)
  
# json method of response object convert
#  json format data into python format data
x = r.json()
  
# now x contains list of nested dictionaries
# we know dictionary contain key value pair
# store the value of result key in variable y
y = x['results']

#print("Search response: ",json.dumps(y,indent=4),"\n")

place_id_list=[]

# keep looping upto length of y
for i in range(len(y)):
      
    # Print value corresponding to the
    # 'name' key at the ith index of y
    place_id_list.append(y[i]['place_id'])


for i in place_id_list:
    # get method of requests module
    url="https://maps.googleapis.com/maps/api/place/details/json?place_id={}&key={}".format(i,my_key)
    r2 = requests.get(url)
    # json method of response object convert
    #  json format data into python format data
    x2 = r2.json()
    y2 = x2['result']
    print (y2['name'])
    try:
        print (y2['formatted_address'])
    except Exception as e:
        print('n/a')
    try:
        print (y2['formatted_phone_number'])
    except Exception as e:
        print('n/a')

#if __name__=="__main__":
"""