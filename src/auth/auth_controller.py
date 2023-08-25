from flask import Blueprint, render_template, request,redirect,url_for, flash
from .auth_service import Service


def controller(bp:Blueprint, service:Service):
    
    @bp.route('/', methods=('GET', 'POST'))
    def auth():
        if request.method == 'POST':
            error = None
            username = request.form['username']
            password = request.form['password']
            
            if not username:
                error = 'Username is required.'
            elif not password:
                error = 'Password is required.'
            
            # return redirect(url_for("main"))
            
            # if error is None: 
            #         print (error) 
            
            # flash(error)
            # redirect(url_for("auth.auth"))
            return {}
        
        return render_template('auth.html')
        

    @bp.route('/signup')
    def signup():
        return 'Signup'

    @bp.route('/logout')
    def logout():
        return 'Logout'
    
    return bp