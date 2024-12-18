from odoo import http
from odoo.http import request

class HospitalPortal(http.Controller):
    @http.route('/hello', website=True, auth="public")
    def say_hello(self, **args):
        return "<h1> Hello Odex !!! </h1>"
    
    # @http.route('/hello/<name>', website=True, auth="public")
    # def say_hello2(self,name, **args):
    #     return "<h1> Hello %s !!! </h1>"%(name)
    
    @http.route('/hello/<name>/<int:count>', website=True, auth="public")
    def say_hello3(self,name, count=2, **args):
        return "<h1> Hello %s  %s times !!! </h1>"%(name, count)
    
    # @http.route('/hello/<model("hospital.paitent"):obj>', website=True, auth="public")
    # def say_hello4(self,obj, **args):
    #     return "<h1> Hello %s  !! </h1>"%(obj.name)
    

    @http.route('/hello/<int:obj_id>', website=True, auth="public")
    def say_hello4(self,obj_id, **args):
        obj_model = request.env.get("hospital.paitent").sudo()  
        objects = obj_model.search([('id', '=', obj_id)])
        if not objects : return "<h1>Not Found </h1"
        obj = objects[0]
        return "<h1> Hello %s  !! </h1>"%(obj.name)
    

    @http.route('/hi/<name>', website=True, auth="public")
    def say_hi(self,name, **args):
        return request.render("hospital.hospital_portal", {'person_name' :  name})
    
    @http.route('/show', website=True, auth="public")
    def show_paitents(self, **args):
        obj_model = request.env.get("hospital.paitent").sudo()
        objects = obj_model.search([])
        return request.render("hospital.hospital_portal_list", {'objects' :  objects})


    
    

    
