import requests

#account data
username = ""
password = ""

# get the access token
auth_res = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(username, password))
if auth_res.status_code == 200:
    # if response is OK, get the access token
    access_token = auth_res.content.decode()
    print("[!] Got access token:", access_token)
else:
    print("[!] Cannot get access token, exiting...")
    exit()