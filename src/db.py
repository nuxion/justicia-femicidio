from elasticsearch import Elasticsearch

class DBElastic(object):

    def __init__(self):
        self.client = None
        self.index = None
        self.doc_type = None

    def init_app(self,
                 host='localhost', port=9200,
                 user=None, passw=None):
        if user and passw:
            self.client = Elasticsearch(
                hosts=[{'host': host, 'port': port }],
                http_auth=(user, passw))
        else:
            self.client = Elasticsearch(
                hosts=[{'host': host, 'port': port}]
            )

    def arrayInsert(self, elements, key_dict, index, d_type, _id):

        for e in elements[key_dict]:
            self.client.index(
                index=index,
                doc_type=d_type,
                id=e[_id],
                body=e
            )
    def insertDict(self, document, index, d_type, _id):
        """
        Inserta solo un elemento a la vez, en este caso
        un diccionario.

        Se le especifica un _id que es la key del diccionario
        que debe usar como id del documento en elastic.

        `index`, es la base en elastic para ser usada.

        `document`:<<dict>>
        `index`: <<string>
        `d_type`: <<string>>
        `_id`: <<string>>.
        """

        self.client.index(index=index,
                          doc_type=d_type,
                          id = _id,
                          body = document)
