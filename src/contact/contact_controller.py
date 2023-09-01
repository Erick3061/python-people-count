from flask import Blueprint, render_template, request,redirect,url_for, flash
from sqlalchemy import ScalarResult, select
from .contact_service import ContactService
from ..database.mapped_classes import Contact

def controller(bp:Blueprint, service:ContactService):
    
    @bp.route('/', methods=('GET', 'POST'))
    def crearContact():
        contacts:ScalarResult[Contact] =[]

        if request.method == 'POST':
            name = request.form['contactName']
            email = request.form['contactEmail']
            newContact = Contact(name=name, email=email)
            service.create(newContact)
            contacts = service.find()
            redirect(url_for('contact.crearContact'))
        
        contacts = service.find()
        return render_template('form_contact.html', emails=[contact.email for contact in contacts])
    
    @bp.post("/many")
    def deleteMany():
        delContact = request.form.getlist('delEmail')
        if len(delContact) != 0:
            service.deleteMore(delContact)
        return redirect(url_for('contact.crearContact'))
    return bp