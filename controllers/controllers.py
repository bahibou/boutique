# -*- coding: utf-8 -*-
# from odoo import http


# class Vente(http.Controller):
#     @http.route('/vente/vente', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vente/vente/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vente.listing', {
#             'root': '/vente/vente',
#             'objects': http.request.env['vente.vente'].search([]),
#         })

#     @http.route('/vente/vente/objects/<model("vente.vente"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vente.object', {
#             'object': obj
#         })

