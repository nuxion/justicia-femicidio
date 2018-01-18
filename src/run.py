from db import DBElastic
from config import Config
from preprocessors import opencsv
from casting import (_return_datetime,
                     _return_int_timestamp)
from helpers import (_setup_log,
                     _open_yaml,
                     _mapper_values)


#def row_scheme(_csv_list):
 #   for row in _csv_list:
def main():

    # Config inicial
    conf = Config()
    logger = _setup_log(conf, __name__)

    # Destino:
    dbE = DBElastic()
    dbE.init_app(conf.ES_HOST, conf.ES_PORT)

    # schema para el dataset
    _scheme = _open_yaml(conf.SCHEME)
    headers = _scheme['headers']
    scheme_id = _scheme['scheme_id']

    # Load csv, return a <list[]>
    # c/elemento de la lista es un dict{}
    list_csv = opencsv(conf.CSV_FILE, headers)
    for c in list_csv:
        #timestp = _return_datetime(c)
        #c.update()
        #import pdb;pdb.set_trace()
        _format = '%d/%m/%Y'
        try:
            timestamp = _return_int_timestamp(c['fecha_hecho'])
            iso_string = c['fecha_hecho'].isoformat()
        except ValueError:
            timestamp = int()
        except TypeError:
            timestamp = int()
        _id = "{}-{}-{}".format(c['numero'],
                                c['edad'],
                                timestamp)
        c.update({'@timestamp':iso_string,'id_f':_id})
        dbE.insertDict(c, conf.ES_INDEX, 'dataset', _id)
if __name__ == '__main__':
    main()


