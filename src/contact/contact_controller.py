from flask import Blueprint, render_template, request,redirect,url_for, flash
from .contact_service import ContactService
from ..database.mapped_classes import Contact

def controller(bp:Blueprint, service:ContactService):
    
    @bp.route('/', methods=('GET', 'POST'))
    def crearContact():
        error = None
        if request.method == 'POST':
            print("funciona")
            name = request.form['contactName']
            email = request.form['contactEmail']
            newContact = Contact(name=name, email=email)
            respuesta = service.create(newContact)
            # if type(respuesta) is str:
            #     error = respuesta
            # else:
            #     error = None
            error = respuesta
            print(respuesta)
            redirect(url_for('contact.crearContact'))
        return render_template('form_contact.html', error = error)
    
    return bp