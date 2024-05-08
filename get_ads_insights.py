from dotenv import load_dotenv
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.api import FacebookAdsApi
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

access_token = os.getenv('ACCESS_TOKEN')
ad_account_id = os.getenv('AD_ACCOUNT_ID')
app_secret = os.getenv('APP_SECRET')
app_id = os.getenv('APP_ID')

FacebookAdsApi.init(access_token=access_token)

fields = [
    'impressions',
    'spend',
    'actions'
]

params = {
    'date_preset': 'yesterday',
    'level': 'account',
}

print(AdAccount(ad_account_id).get_insights(fields=fields, params=params))
