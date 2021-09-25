from application import app
# from application.models import Person

@app.route('/')
def index():
    return 'Hello Shemar'

    