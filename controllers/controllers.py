# -*- coding: utf-8 -*-
from odoo import http

# class HomeProject(http.Controller):
#     @http.route('/home_project/home_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/home_project/home_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('home_project.listing', {
#             'root': '/home_project/home_project',
#             'objects': http.request.env['home_project.home_project'].search([]),
#         })

#     @http.route('/home_project/home_project/objects/<model("home_project.home_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('home_project.object', {
#             'object': obj
#         })