import json
from decimal import Decimal
from datetime import date

class IdrogeoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

def fixValues(data:dict):
    """Fixes values in the data dictionary.
    
    Can be issues due to flat origin data or data types.
    """
    for key, value in data.items():
        # field "gruppi_elementi_danni" has to be a list of strings
        if key == 'gruppi_elementi_danni':
            string2List(data, key, value)
        # field "Compila danni" has to be a boolean
        elif key == 'compila_danni':
            data[key] = bool(value)
        # field "Gruppi elementi danni (danni di primo livello)" has to be a list of strings
        elif key == 'gruppi_elementi_danni_danni_di_primo_livello':
            string2List(data, key, value)
        # field "Metodo" has to be a list of strings
        elif key == 'metodo':
            string2List(data, key, value)

    return data 

def string2List(data, key, value):
    if value:
        v = str(value)
        data[key] = [v]
    else:
        data[key] = []   
