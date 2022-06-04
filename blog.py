from os import name
from marshmallow import Schema, ValidationError, fields
from flask import Flask, render_template, url_for, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_url_path='/static/', static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/blog'
db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(300))
    subtitle = db.Column(db.String(300))
    author = db.Column(db.String(100))
    date_created = db.Column(db.DateTime)
    content_text = db.Column(db.Text)

class Subscribers(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    email = db.Column(db.String(300), unique = True)


def not_blank(data):
    if not data:
        raise ValidationError("Data not provided.")


class SubscribersSchema(Schema):
    id_ = fields.Integer()
    name = fields.Str(required=True, validate=not_blank)
    email = fields.Email(required=True)


@app.route('/index')
def index():
    blogposts= Blogpost.query.all()
    return render_template('index.html', blogposts=blogposts)

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/subscribe', methods=['POST','GET'])
def subscribe():


    if request.method == 'POST':

        subscriber = Subscribers()
        subscriber.name = request.form['name']
        subscriber.email = request.form['email']

        db.session.add(subscriber)
        db.session.commit()

        return 'success'

    else:
        return render_template('subscribe.html')

@app.route('/post/<int:id>')
def post(id):
    # blogposts= db.session.query.all().filter(id=id)
    blogpost= Blogpost.query.get_or_404(id)
    return render_template('post.html', blogpost=blogpost) 

# @app.route("/static/<path:path>")
# def static_dir(path):
#     return send_from_directory("static", path)

if __name__ == "__main__":
    app.run(debug=True)


