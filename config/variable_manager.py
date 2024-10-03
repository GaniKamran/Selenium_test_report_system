import hvac
import sys
import os
import yaml

class Environment():
    def __init__(self) -> None:
        adress_host=os.getenv('ADRESS_HOST')
        adress_token = os.getenv('TOKEN') 
        self.client = hvac.Client(
        url=adress_host,
        token=adress_token,  # Replace with your Vault token
        )
        read_response = self.client.secrets.kv.read_secret_version(path='my-secret-credentials')
        # Extracting the username, password, and URL
        self.username = read_response['data']['data']['username']
        self.password = read_response['data']['data']['password']
        self.url = read_response['data']['data']['url']
        
    def text_data(self,case):
        with open("config.yaml", 'r') as file:
            config = yaml.safe_load(file)
            # Accessing data from the YAML file
            self.alert_data = config['alert']         
            self.db_host = config['database']['host']
            self.welcome_message = config['messages']['welcome']
            self.user_list = config['users']