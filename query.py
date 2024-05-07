import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def get_access_token():
    url = f"https://graph.facebook.com/v19.0/{os.getenv('ID_DA_PAGINA')}"
    params = {
        'fields': 'access_token',
        'access_token': os.getenv('TOKEN_USUARIO')
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()['access_token']

# Restante do código...


def get_lead_data(access_token):
    url = f"https://graph.facebook.com/v19.0/{os.environ.get('ID_DA_PAGINA')}"
    params = {
        'fields': 'access_token,leadgen_forms{leads}',
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def extract_lead_data(response_data):
    leads = response_data.get('leadgen_forms', {}).get('data', [])
    extracted_data = []
    for lead in leads:
        lead_data = lead.get('leads', {}).get('data', [])
        for data in lead_data:
            if 'field_data' in data:
                lead_dict = {item['name']: item['values'][0] for item in data['field_data']}
                extracted_data.append({
                    'full_name': lead_dict.get('full_name', None),
                    'email': lead_dict.get('email', None),
                    'phone_number': lead_dict.get('phone_number', None)
                })
    return extracted_data

def main():
    access_token = get_access_token()
    response_data = get_lead_data(access_token)
    extracted_data = extract_lead_data(response_data)
    df = pd.DataFrame(extracted_data)
    print(df.head())

if __name__ == "__main__":
    main()
