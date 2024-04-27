# models.py

from odoo import models, fields

class Product(models.Model):
    _name = 'vente.product'
    _description = 'Product'

    name = fields.Char('Product Name', required=True)
    description = fields.Text('Description')
    category_id = fields.Many2one('vente.category', 'Category')
    price = fields.Float('Price')
    quantity_available = fields.Integer('Quantité disponible')
    image = fields.Binary('Image')
    order_id = fields.Many2one('vente.order','Commande' )
    category_id = fields.Many2one('vente.category', 'Categorie')
