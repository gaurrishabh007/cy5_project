import requests
import json
url = "https://rahulgangtuhh.atlassian.net//rest/api/3/issue"
headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload=json.dumps(
   {
    "fields": {
       "project":
       {
          "key": "CY5"
       },
       "summary": "REST ye merry gentlemen.",
       "description": "Creating of an issue using project keys and issue type names using the REST API",
       "issuetype": {
          "name": "Bug"
       }
   }
}
)
    
response=requests.post(url, headers=headers, data=payload, auth=("rahulgangtuhh@gmail.com","R6MUCtlKF9nDPhwkL1tH7FFB"))
print(response.text)
