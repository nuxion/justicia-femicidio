import time
import re
from datetime import datetime, timedelta

# Regular expressions:
ONLY_NUMS = re.compile('[0-9]*').search


def _return_ddmmY(s_dat):
    '''
    recibe un string
    '''
    try:
        return datetime.strptime(s_dat,'%d/%m/%Y')
    except ValueError:
        return "Invalid"

def _return_datetime(s_dat, s_format):
    """
    Recibe un string el formato, el formato y lo transforma a date.
    `s_dat`:<<string>>
    `s_format`: <<string>>
    return: <<datetime>>
    """
    return datetime.strptime(s_dat,s_format)


def _return_int_timestamp(s_dat):
    """
    Recibe una fecha y devuelve un entero con el timestamp
    `s_dat`: <<datetime>>
    return <<int>>
    """

    return int((s_dat - datetime(1970,1,1))/timedelta(seconds=1))


def _return_int(s_dat):
    '''
    Metodo que obtiene solo los numeros
    de un string.
    `s_dat`: <<string>>
    return: <<int>>
    '''

    try:
        return int(ONLY_NUMS(s_dat).group(0))
    except AttributeError:
        return -1
    except:
        return -2


def _is_bool(s_data):
    '''
    Valida si el string esta vacio o no.
    `s_data`: <<string>>
    return: <<boolean>>
    '''

    if s_data:
        return True
    else:
        return False


def _return_str(s_data):
    return str(s_data)

def _return_lower_str(s_data):
    low = str(s_data)
    return low.lower()

