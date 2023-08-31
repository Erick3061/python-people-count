from flask import Blueprint, render_template, request,redirect,url_for, flash
from sqlalchemy import ScalarResult
from .contact_service import ContactService
from ..database.mapped_classes import Contact

def controller(bp:Blueprint, service:ContactService):
    
    @bp.route('/', methods=('GET', 'POST'))
    def crearContact():
        contacts:ScalarResult[Contact] =[]

        if request.method == 'POST':
            print("funciona")
            name = request.form['contactName']
            email = request.form['contactEmail']
            newContact = Contact(name=name, email=email)
            service.create(newContact)
            contacts = service.find()
            redirect(url_for('contact.crearContact'))
        
        contacts = service.find()
        return render_template('form_contact.html', emails=[contact.email for contact in contacts])
    
    @bp.delete("/many")
    def deleteMany():
        print('entro a elimanar varios')
        print()
        return {}
    return bp