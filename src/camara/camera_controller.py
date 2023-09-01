from flask import Blueprint, render_template, request,redirect,url_for, flash
from sqlalchemy import ScalarResult, select
from .camera_service import CameraService
from ..database.mapped_classes import Camera

def controller(bp:Blueprint, service:CameraService):
    
    @bp.route('/', methods=('GET', 'POST'))
    def crearCamera():
        cameras:ScalarResult[Camera] =[]
        
        if request.method == 'POST':
            cameraName = request.form['cameraName']
            url = request.form['floatingUrl']
            top = request.form['floatingLimTop']
            low = request.form['floatingLimBut']
            sendTime = request.form['sendTime']
            newCamera = Camera(name=cameraName, url=url, limTop=top, limBut=low, sendTime=sendTime)
            service.create(newCamera)
            cameras = service.find()
            return redirect(url_for('camera.crearCamera'))
        
        cameras = service.find()
        return render_template('form_camara.html', names=cameras)
    
    @bp.route("/notify/<notifyCamera>", methods=('GET', 'POST'))
    def notify():
        if request.method == 'POST':
            notifyCamera = request.form['camera']
            print(f'{notifyCamera}')
        return redirect(url_for('camera.notify'))
    
    return bp