from flask import Blueprint, render_template, request,redirect,url_for, flash
from .camera_service import CameraService
from ..database.mapped_classes import Camera

def controller(bp:Blueprint, service:CameraService):
    
    @bp.route('/', methods=('GET', 'POST'))
    def crearCamera():
        if request.method == 'POST':
            cameraName = request.form['cameraName']
            url = request.form['floatingUrl']
            top = request.form['floatingLimTop']
            low = request.form['floatingLimBut']
            sendTime = request.form['sendTime']
            newCamera = Camera(name=cameraName, url=url, limTop=top, limBut=low, sendTime=sendTime)
            service.create(newCamera)
            return redirect(url_for('camera.crearCamera'))
        return render_template('form_camara.html')
        

    @bp.route('/signup')
    def signup():
        return 'Signup'

    @bp.route('/logout')
    def logout():
        return 'Logout'
    
    return bp