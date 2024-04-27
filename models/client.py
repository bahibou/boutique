# models.py

from odoo import models, fields

class Customer(models.Model):
    # _inherit = 'res.partner'
    _name = "vente.customer"
    _description = 'Customer'

    email = fields.Char('Email')
    shipping_address = fields.Text('Shipping Address')
    order_id = fields.Many2one('vente.customer','Commande')
