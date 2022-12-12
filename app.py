'''ticket_1'''
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///films.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = True
db = SQLAlchemy(app)

class Film(db.Model):
    '''table'''
    ID = db.Column(db.Integer, primary_key = True)
    film_name = db.Column(db.Text)
    film_producer = db.Column(db.Text)
    year = db.Column(db.Integer)
    category = db.Column(db.Text)

@app.route('/')
def show():
    '''output'''
    films = Film.query.all()
    print(films)
    return render_template('main.html', films=films)

@app.route('/edit', methods=['POST', 'GET'])
def edit():
    '''changes'''
    ID = request.form.get('ID')
    film_producer = request.form.get('film_producer')
    if ID != None and film_producer != None:
        db.session.execute(f'UPDATE film SET film_producer = {film_producer} WHERE ID={int(ID)};')
        db.session.commit()
    return render_template('edit.html')

@app.route('/remove', methods=['POST', 'GET'])
def remove():
    '''remove'''
    ID = request.form.get('ID')
    if ID != None:
        db.session.execute(f'DELETE FROM film WHERE id = {ID};')
        db.session.commit()
    return render_template('remove.html')


if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
