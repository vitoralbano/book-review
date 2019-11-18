from flask import Blueprint, render_template, abort, request

routes_web = Blueprint(
    'web', __name__, 
    template_folder='templates', 
    url_prefix=''
    )

@routes_web.route('/')
def home():
    return render_template('home.html')

@routes_web.route('/register', methods=("POST", "GET"))
def register():
    if request.method.lower() == "POST":
        return render_template('register.html')
    else:
        return render_template('register.html')