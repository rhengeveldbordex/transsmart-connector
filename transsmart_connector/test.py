from dotenv import load_dotenv
import os
from transsmart_connector import TranssmartConnector


load_dotenv()

# Initialize the TranssmartConnector class
transsmart = TranssmartConnector()

# GET all shipments
shipments = transsmart.get_shipments()
print(shipments)

#GET shipment by ID
shipment_id = 'PNL-1717597661'
shipment = transsmart.get_shipment(shipment_id)
print(shipment)