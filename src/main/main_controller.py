from flask import Blueprint, render_template


def controller(bp:Blueprint):
    
    @bp.route("/")
    def index():
        return render_template('index.html')
    
    # @bp.route('/profile')
    # def profile():
    #     return 'Profile'
    
    return bp