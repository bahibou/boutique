# models.py

from odoo import models, fields

class ProductCategory(models.Model):
    _name = 'vente.category'
    _description = 'Product Category'

    name = fields.Char('Category Name', required=True)
    description = fields.Text('Description')
    product_ids = fields.One2many('vente.product', 'category_id', 'Produits')
