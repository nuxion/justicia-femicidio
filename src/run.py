from db import DBElastic
from config import Config
from preprocessors import opencsv
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
        dbE.insertDict(c, '2femicidio', 'dataset')
if __name__ == '__main__':
    main()


