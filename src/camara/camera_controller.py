from flask import Blueprint, render_template, request,redirect,url_for, flash
from .camera_service import CameraService

def controller(bp:Blueprint, service:CameraService):
    
    @bp.route('/', methods=('GET', 'POST'))
    def crearCamera():
        if request.method == 'POST':
            print("funciona")
            cameraName = request.form['cameraName']
            url = request.form['floatingUrl']
            top = request.form['floatingLimTop']
            low = request.form['floatingLimBut']
            sendTime = request.form['sendTime']
            print(f'Nombre de la camara: {cameraName}')
            print(f'Url de la camara: {url}')
            print(f'El limite maximo es: {top}')
            print(f'El limite maximo es: {low}')
            print(f'Tiempo entre alertas una vez activo el evento {sendTime} minutos')
            return redirect(url_for('camera.crearCamera'))
        return render_template('form_camara.html')
        

    @bp.route('/signup')
    def signup():
        return 'Signup'

    @bp.route('/logout')
    def logout():
        return 'Logout'
    
    return bp