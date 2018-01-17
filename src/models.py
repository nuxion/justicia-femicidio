from marshmallow import Schema, fields, pprint

class Victim(Schema):
    anio_denuncia = fields.Int()
    tipificacion = fields.String()
    id_ruvte = fields.Int()
    nomb_ape_paternos = fields.String()
    ape_manternos = fields.String()
    ape_casada = fields.String()
    edad_al_momento = fields.Int()
    prov_nacimiento = fields.String()
    nacionalidad = fields.String()
    embarazo_orig = fields.String()
    embarazo_boolean = fields.Boolean()
    fecha_lugar_detencion = fields.String()




