from odoo import models, fields

class ProductoOxxo(models.Model):
    __name ='oxxo.producto'
    __description = 'Producto oxxo' 
    __rec_name = 'nombre'
    __orden = 'nombre asc'


    nombre = fields.Char(
        string = 'nombre del producto',
        required = True
    )

    codigo = fields.Char(
        string = 'codigo',
        required=True
    )

    tipo_producto = fields.Selection(
        [
        ('zapato','Zapato'),
        ('gorra','Gorra'),
        ('combo','Combo'),
        ('accesorios','Accesorios'),
        ('otros','Otros'),
        ],
    string = 'Tipo de producto',
    required=True,
    default = 'otro'
    )

    precio_venta = fields.float(
    string = 'precio de venta',
    required=True        
    )

    descripcion = fields.Text(
    string = 'Descripcion'
    )