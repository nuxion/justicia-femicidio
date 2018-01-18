import csv
import casting


def opencsv(filepath, headers):
    ''' Metodo que recorre un archivo
    csv y retorna una lista de listas.

    `filepath`: <<string>>.
    return: <<list>>.
     '''
    array_csv = []
    # transform headers in only one dict:
    headers_dict = _array_to_dict(headers)
    # encoding because:
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1 in position 409:
    # invalid continuation bytE
    # https://stackoverflow.com/questions/21504319/python-3-csv-file-giving-unicodedecodeerror-utf-8-codec-cant-decode-byte-err
    with open(filepath, 'r', encoding='mac_roman') as f:
        reader = csv.reader(f)
        for row in reader:
            # agregar try por si falla
            # el schema con los datos del csv
            array_csv.append(_mapper_values(row, headers_dict))

    return array_csv

def _mapper_values(datos, headers):
    """
    Recibe el header que seran el nombre de la key del dict
    el array del dato (generalmente un row del csv leido)
    y un array con los nombres de las funciones que se encargar
    de castear al tipo de dato correct.
    Headers example:
        [{'nombre': '_return_string'}, {'apellido': '_return_string'}]
        key, value: key=nombre de la columna,
                    value=funcion de casteo.

    `headers`: <<list>> with <<dict{}>>
    `datos`: <<list>>
    `_casting`: <<list>>
    return: <<dict>>
    """
    dicto = {}
    # Loopea la lista para separar nombre de
    # funcion de casteo
    i = 0
    for name_key, _castFunc in headers.items():
        try:
            caster = getattr(casting, _castFunc)
            dicto[name_key] = caster(datos[i])
        except AttributeError:
            pass
        i = i + 1

    return dicto

def _array_to_dict(headers):

    dicto = {}
    for x in headers:
        dicto.update(x)
    return dicto




if __name__ == '__main__':
    opencsv("test.csv")
