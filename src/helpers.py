import logging
import yaml

def _open_yaml(filepath):
    """
    Recibe un string con la ruta para abrir
    el archivo de configuracion.

    fielpath: <<string>>
    return: <<dict>>
    """
    _dict = {}
    with open(filepath, 'r') as stream:
        try:
            _dict = yaml.load(stream)
        except yaml.YAMLError as exc:
            # agregar logger
            print("Error {0}").format(exc)
    return _dict

def _mapper_values(header, datos, _casting):
    """
    Recibe el header que seran el nombre de la key del dict
    el array del dato (generalmente un row del csv leido)
    y un array con los nombres de las funciones que se encargar
    de castear al tipo de dato correct.

    `header`: <<list>>
    `datos`: <<list>>
    `_casting`: <<list>>
    return: <<dict>>
    """

    dicto = {}
    for i in range(0, len(header)):
        try:
            cast = getattr(preprocessors, _casting[i])
            dicto[header[i]] = cast(datos[i])
        except AttributeError:
            pass

    return dicto

def _setup_log(conf, namespace=__name__):

    #conf = Config()
    logging.basicConfig(level=conf.LOG_LVL)
    logger = logging.getLogger(namespace)
    handler = logging.FileHandler(conf.LOG_PATH)
    formatter=logging.Formatter(conf.LOG_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

