# -*- coding: utf-8 -*-
from odoo import http

# class HrExtensions(http.Controller):
#     @http.route('/hr_exipre_doc/hr_exipre_doc/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_exipre_doc/hr_exipre_doc/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_exipre_doc.listing', {
#             'root': '/hr_exipre_doc/hr_exipre_doc',
#             'objects': http.request.env['hr_exipre_doc.hr_exipre_doc'].search([]),
#         })

#     @http.route('/hr_exipre_doc/hr_exipre_doc/objects/<model("hr_exipre_doc.hr_exipre_doc"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_exipre_doc.object', {
#             'object': obj
#         })
