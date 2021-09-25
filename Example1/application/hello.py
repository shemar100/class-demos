from application import app
from application.models import Person

@app.route('/')
def index():
    person = Person.query.first()
    return person.name

    