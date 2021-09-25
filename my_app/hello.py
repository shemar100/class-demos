from my_app import app

@app.route('/')
def index():
    return 'Hello Shemar'
