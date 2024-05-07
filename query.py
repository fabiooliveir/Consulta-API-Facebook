import requests
import pandas as pd
import os

url1 = "https://graph.facebook.com/v19.0/"+os.environ.get('ID_DA_PAGINA')
params1 = {
    'fields': 'access_token',
    'access_token': '[[TOKEN USUÁRIO]]'
}
response1 = requests.get(url1, params=params1)
access_token = response1.json()['access_token']

url2 = "https://graph.facebook.com/v19.0/"+os.environ.get('ID_DA_PAGINA')
params2 = {
    'fields': 'access_token,leadgen_forms{leads}',
    'access_token': access_token
}
response2 = requests.get(url2, params=params2)

print(response2.json())

response_data = response2.json()

leads = response_data.get('leadgen_forms', {}).get('data', [])

full_names = []
emails = []
phone_numbers = []

for lead in leads:
    lead_data = lead.get('leads', {}).get('data', [])
    for data in lead_data:
        if 'field_data' in data:
            lead_dict = {item['name']: item['values'][0] for item in data['field_data']}
            full_names.append(lead_dict.get('full_name', None))
            emails.append(lead_dict.get('email', None))
            phone_numbers.append(lead_dict.get('phone_number', None))
        else:
            full_names.append(None)
            emails.append(None)
            phone_numbers.append(None)

df = pd.DataFrame({
    'full_name': full_names,
    'email': emails,
    'phone_number': phone_numbers
})

df.head()