import requests
import json

api_url = "https://us-central1-marcy-playground.cloudfunctions.net/ordoroCodingTest"
your_email_address = "jalisahewitt@gmail.com"

def getData():
    response = requests.get(api_url)
    return response.json()

def postData(unique_emails, user_domain_counts, april_emails):
    headers =  {"Content-Type":"application/json"}
    json_data = {"your_email_address": your_email_address, "unique_emails": unique_emails, "user_domain_counts":user_domain_counts, "april_emails": april_emails  }
    response = requests.post(api_url,json.dumps(json_data), headers=headers)
    print(response)
    return response.status_code