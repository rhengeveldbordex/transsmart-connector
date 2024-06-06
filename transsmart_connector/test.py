from dotenv import load_dotenv
import os
from transsmart_connector import TranssmartConnector


load_dotenv()

# This is a test script to test the TranssmartConnector class
# Make sure to set the environment variables in a .env file in the root of this project
# The following environment variables are required:
# TRANSSMART_ACCOUNT
# TRANSSMART_USERNAME
# TRANSSMART_PASSWORD

# Initialize the TranssmartConnector class
transsmart = TranssmartConnector()

# GET all shipments
shipments = transsmart.get_shipments()
print(shipments)

# GET shipment by ID
shipment_id = 'YOUR_SHIPMENT_ID_HERE'
shipment = transsmart.get_shipment(shipment_id)
print(shipment)

# Cancel shipment by ID
shipment_id = 'YOUR_SHIPMENT_ID_HERE'
response = transsmart.cancel_shipment(shipment_id)
print(response)

# GET labels by shipment ID
shipment_id = 'YOUR_SHIPMENT_ID_HERE'
labels = transsmart.get_labels(shipment_id)
print(labels)

# GET documents by shipment ID
shipment_id = 'YOUR_SHIPMENT_ID_HERE'
documents = transsmart.get_documents(shipment_id)
print(documents)

