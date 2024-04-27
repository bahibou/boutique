# models.py

from odoo import models, fields

class Order(models.Model):
    _name = 'vente.order'
    _description = 'Sale Order'

    name = fields.Char('Order Number', required=True)
    customer_id = fields.Many2one('vente.customer', 'Customer')
    product_ids  = fields.One2many('vente.product', 'order_id', 'Produits')
    customer_ids = fields.One2many('vente.customer', 'order_id', 'Clients')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped')
    ], 'Status')
    date_order = fields.Date('Order Date', default=fields.Date.today)
    total_amount = fields.Float('Total Amount', compute='_compute_total_amount', store=True)

    def _compute_total_amount(self):
        for order in self:
            total = sum(line.price_total for line in order.order_line)
            order.total_amount = total
