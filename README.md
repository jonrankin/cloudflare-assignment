# Cloudflare Assignment
Created a website with cloudflare services which can be found at: https://carena.ca. 


Included are the following: 
1. NGINX configuration to listen on ipv6 for both port 80 and 443 
2. Railgun configuration. 
3. Railgun Nat configuration, had to be done for a single server. 
4. Script to compare HTTP headers from the origin site over ipv6 versus the origin site passed through Cloudflare services.

## Script Usage

### Downloading the Script
The script can be grabbed from any linux based machine by typing
```
wget https://raw.githubusercontent.com/jonrankin/cloudflare-assignment/master/cloudflare-compare.py
```

### Running the Script
The script needs to be put on an IPv6 capable device that can run python, once downloaded use the following line when in the same directory as the script: 
``` 
python cloudflare-compare.py 
``` 

It will output a table that compares the headers of the two sites found within the two variables in the script by the name: 
* cloudflare_site
* origin_site

**NOTE:** You will need to ensure the window width is wide enough to compensate for the large information contained in some of the headers.

Sample Output:
![alt text](https://imgur.com/3zmmEUF.png "Sample Output")
