# TranssmartConnector

De `TranssmartConnector` klasse biedt een interface voor het communiceren met de Transsmart API. Deze klasse bevat methoden voor het verkrijgen, aanmaken, bijwerken en verwijderen van zendingen, evenals andere functionaliteiten zoals het ophalen van labels, documenten en carriers.

## Inhoud

- [Installatie](#installatie)
- [Gebruik](#gebruik)
- [Methoden](#methoden)
  - [get_shipments](#get_shipments)
  - [get_shipment](#get_shipment)
  - [cancel_shipment](#cancel_shipment)
  - [get_labels](#get_labels)
  - [get_documents](#get_documents)
  - [create_shipment](#create_shipment)
  - [update_shipment](#update_shipment)
  - [delete_shipment](#delete_shipment)
  - [get_shipment_status](#get_shipment_status)
  - [get_track_and_trace](#get_track_and_trace)
  - [get_carriers](#get_carriers)

## Installatie

Zorg ervoor dat je de benodigde packages hebt geïnstalleerd:

```bash
pip install requests python-dotenv
```

## Gebruik

```python
import json
import os
from transsmart_connector import TranssmartConnector
from dotenv import load_dotenv

load_dotenv()

# Initialiseer de TranssmartConnector klasse
transsmart = TranssmartConnector()

# Haal alle zendingen op
shipments, url = transsmart.get_shipments()
print(shipments)
```

## Methoden

### `get_shipments`

Haalt alle zendingen op van de Transsmart API.

```python
def get_shipments(self, url: str = None):
    """
    Haal alle zendingen op van de Transsmart API, met optionele parameters.

    Args:
        **params: Optionele parameters voor filteren en pagineren van zendingen.
    
    Returns:
        dict: Alle zendingen van de Transsmart API.
    """
```

### `get_shipment`

Haalt een specifieke zending op aan de hand van het gegeven ID.

```python
def get_shipment(self, shipment_id: str):
    """
    Haal de zending op met het gegeven ID.
    
    Args:
        shipment_id (str): ID van de zending.
    
    Returns:
        dict: Zendinggegevens van de Transsmart API.
    """
```

### `cancel_shipment`

Annuleert een zending met het gegeven ID.

```python
def cancel_shipment(self, shipment_id: str):
    """
    Annuleer de zending met het gegeven ID.
    
    Args:
        shipment_id (str): ID van de zending.
    
    Returns:
        dict: Reactie van de Transsmart API.
    """
```

### `get_labels`

Haalt de labels op voor een zending met het gegeven ID.

```python
def get_labels(self, shipment_id: str):
    """
    Haal de labels op voor de zending met het gegeven ID.
    
    Args:
        shipment_id (str): ID van de zending.
    
    Returns:
        dict: Labels voor de zending van de Transsmart API.
    """
```

### `get_documents`

Haalt de documenten op voor een zending met het gegeven ID.

```python
def get_documents(self, shipment_id: str):
    """
    Haal de documenten op voor de zending met het gegeven ID.
    
    Args:
        shipment_id (str): ID van de zending.
    
    Returns:
        dict: Documenten voor de zending van de Transsmart API.
    """
```

### `create_shipment`

Maakt een nieuwe zending aan met de gegeven gegevens.

```python
def create_shipment(self, shipment_data: dict):
    """
    Maak een nieuwe zending aan met de gegeven gegevens.
    
    Args:
        shipment_data (dict): Gegevens voor de zending.
    
    Returns:
        dict: Reactie van de Transsmart API.
    """
```

### `update_shipment`

Werk een zending bij met het gegeven ID en gegevens.

```python
def update_shipment(self, shipment_id: str, shipment_data: dict):
    """
    Werk de zending bij met het gegeven ID.
    
    Args:
        shipment_id (str): ID van de zending.
        shipment_data (dict): Gegevens voor de zending.
    
    Returns:
        dict: Reactie van de Transsmart API.
    """
```

### `delete_shipment`

Verwijdert een zending met het gegeven ID.

```python
def delete_shipment(self, shipment_id: str):
    """
    Verwijder de zending met het gegeven ID.
    
    Args:
        shipment_id (str): ID van de zending.
    
    Returns:
        dict: Reactie van de Transsmart API.
    """
```

### `get_shipment_status`

Haalt de status op van een zending met het gegeven ID.

```python
def get_shipment_status(self, shipment_id: str):
    """
    Haal de status op van de zending met het gegeven ID.
    
    Args:
        shipment_id (str): ID van de zending.
    
    Returns:
        dict: Status van de zending van de Transsmart API.
    """
```

### `get_track_and_trace`

Haalt de track en trace informatie op voor een zending met het gegeven ID.

```python
def get_track_and_trace(self, shipment_id: str):
    """
    Haal de track en trace informatie op voor de zending met het gegeven ID.
    
    Args:
        shipment_id (str): ID van de zending.
    
    Returns:
        dict: Track en trace informatie voor de zending van de Transsmart API.
    """
```

### `get_carriers`

Haalt alle vervoerders op van de Transsmart API.

```python
def get_carriers(self):
    """
    Haal alle vervoerders op van de Transsmart API.
    
    Returns:
        dict: Alle vervoerders van de Transsmart API.
    """
```

## Omgevingsvariabelen

Zorg ervoor dat de volgende omgevingsvariabelen zijn ingesteld in je `.env` bestand:

```
TRANSSMART_ACCOUNT=your_account
TRANSSMART_USERNAME=your_username
TRANSSMART_PASSWORD=your_password
```
