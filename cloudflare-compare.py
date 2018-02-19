
import json
import requests
from tabulate import tabulate
from pprint import pprint

#This script is designed to compare the response headers of an HTTP request between a web server not utilizing the Cloudflare services, and one that is. 
# when you type python cloudflare-compare.py the script will pull the websites response headers and format them into a table for simple reading to quickly compare the two services.


#The cloudflare URI and the origin site IP address. Both are the same server, just one goes through the cloudflare network
cloudflare_site = 'http://carena.ca'
origin_site = 'http://[2604:a880:800:a1::86a:1001]'


#grab the cloudflare sites headers and dump it into a list  for formatting
cloudflare_site_r = requests.get(cloudflare_site)
cloudflare_site_headers = json.dumps(cloudflare_site_r.headers.__dict__['_store'])

#create a list of our own to tabulate later
compare_table = []

#go through the list and append the value  to our own list. Note that the cloudflare_site_headers variable actually has the header-type listed twice. We only need one for this case.
for header, value in (json.loads(cloudflare_site_headers)).items():
   compare_table.append( value)

#grab the origin servers headers and dump it into a list for formatting
origin_site_r = requests.get(origin_site)
origin_site_headers = json.loads(json.dumps(origin_site_r.headers.__dict__['_store'])).items()

#go through the list and check to see if the header-type is already present. If so, add the origins site value to the list to make tabulating easier. If not, add it to the compare_table
for header,value in origin_site_headers:
   exist = False
   for header_type in compare_table:
        if header.lower() == header_type[0].lower():
          header_type.append(value[1])
          exist = True
   if not exist:
          value.insert(1, '-')
          compare_table.append( value)



#sort the table because it will make finding like types easier
compare_table.sort()
print tabulate(compare_table, headers=['Header Type','Cloudflare Site','Origin Site'], tablefmt='orgtbl')




