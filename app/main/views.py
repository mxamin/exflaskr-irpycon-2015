from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Extended Flaskr is Working!</h1>'
