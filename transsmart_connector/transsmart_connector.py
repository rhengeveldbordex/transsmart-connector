import json
import os
import requests as req

class TranssmartConnector:
    """
    Connector class for Transsmart API.
    
    Attributes:
        api_key (str): API key for Transsmart API.
        api_url (str): Base URL for Transsmart API.
    """
        
    # Constants
    base_url = 'https://api.transsmart.com'
    endpoint_url = '{base_url}/{version}/shipments/{account}/{action}'
      
    def __init__(self, account = None, username = None, password = None, version='v2'):
        """
        Initialize the TranssmartConnector with the given API key and URL.
        
        Args:
            api_key (str): API key for Transsmart API.
            api_url (str): Base URL for Transsmart API.
        """
        #Initialize the TranssmartConnector class
        self.account = os.getenv('TRANSSMART_ACCOUNT') if account is None else account
        self.username = os.getenv('TRANSSMART_USERNAME') if username is None else username
        self.password = os.getenv('TRANSSMART_PASSWORD') if password is None else password
        self.access_token = self.get_access_token()
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        self.version = version
        
    def get_access_token(self):
        """
        Get the access token for the Transsmart API.
        
        Returns:
            str: Access token for the Transsmart API.
        """
        url = f'{self.base_url}/login'
        body = (self.username, self.password)
        response = req.get(url, auth=body)
        try:
            data = response.json()
            self.access_token = data['token']
            return self.access_token
        except:
            raise ValueError('Failed to get access token')
        
    def get_shipments(self, url: str = None, **params):
        """
        Get all shipments from the Transsmart API with optional request parameters.
        
        Args:
            **params: Optional parameters for filtering shipments.
            
        Returns:
            dict: All shipments from the Transsmart API.
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=''
        )
        response = req.get(url, headers=self.headers, params=params)
        return response.json(), url
    
    def get_shipment(self, shipment_id: str):
        """
        Get the shipment with the given ID.
        
        Args:
            shipment_id (str): ID of the shipment.
        
        Returns:
            dict: Shipment data from the Transsmart API.
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=shipment_id
        )
        response = req.get(url, headers=self.headers)
        return response.json()
    
    def cancel_shipment(self, shipment_id: str):
        """
        Cancel the shipment with the given ID.
        
        Args:
            shipment_id (str): ID of the shipment.
        
        Returns:
            dict: Response from the Transsmart API.
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=f'{shipment_id}/cancel'
        )
        response = req.post(url, headers=self.headers)
        return response.json()
    
    def get_labels(self, shipment_id: str):
        """
        Get the labels for the shipment with the given ID.
        
        Args:
            shipment_id (str): ID of the shipment.
        
        Returns:
            dict: Labels for the shipment from the Transsmart API.
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=f'{shipment_id}/labels'
        )
        response = req.get(url, headers=self.headers)
        return response.json()
    
    def get_documents(self, shipment_id: str):
        """
        Get the documents for the shipment with the given ID.
        
        Args:
            shipment_id (str): ID of the shipment.
        
        Returns:
            dict: Documents for the shipment from the Transsmart API.
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=f'{shipment_id}/documents'
        )
        response = req.get(url, headers=self.headers)
        return response.json()
    
    def create_shipment(self, shipment_data: dict):
        """
        Create a shipment with the given data.
        
        Args:
            shipment_data (dict): Data for the shipment.
        
        Returns:
            dict: Response from the Transsmart API.
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=''
        )
        response = req.post(url, headers=self.headers, data=json.dumps(shipment_data))
        return response.json()
    
    def update_shipment(self, shipment_id: str, shipment_data: dict):
        """
        Update the shipment with the given ID.
        
        Args:
            shipment_id (str): ID of the shipment.
            shipment_data (dict): Data for the shipment.
        
        Returns:
            dict: Response from the Transsmart API.
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=shipment_id
        )
        response = req.put(url, headers=self.headers, data=json.dumps(shipment_data))
        return response.json()
    
    def delete_shipment(self, shipment_id: str):
        """
        Delete the shipment with the given ID.
        
        Args:
            shipment_id (str): ID of the shipment.
        
        Returns:
            dict: Response from the Transsmart API.
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=shipment_id
        )
        response = req.delete(url, headers=self.headers)
        return response.json()
    
    def get_shipment_status(self, shipment_id: str):
        """
        Get the status of the shipment with the given ID.
        
        Args:
            shipment_id (str): ID of the shipment.
        
        Returns:
            dict: Status of the
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=f'{shipment_id}/status'
        )
        response = req.get(url, headers=self.headers)
        return response.json()
    
    def get_track_and_trace(self, shipment_id: str):
        """
        Get the track and trace information for the shipment with the given ID.
        
        Args:
            shipment_id (str): ID of the shipment.
        
        Returns:
            dict: Track and trace information for the
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action=f'{shipment_id}/trackandtrace'
        )
        response = req.get(url, headers=self.headers)
        return response.json()
    
    def get_carriers(self):
        """
        Get all carriers from the Transsmart API.
        
        Returns:
            dict: All
        """
        url = self.endpoint_url.format(
            base_url=self.base_url,
            version=self.version,
            account=self.account,
            action='carriers'
        )
        response = req.get(url, headers=self.headers)
        return response.json()