from os import name
from marshmallow import Schema, ValidationError, fields
from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from blog import Blogpost
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cerenyasar:2321@localhost/blog'
db = SQLAlchemy(app)

bp1 = Blogpost(title="article1", subtitle = "subtitle", author = "author", date_created = date.today(), content_text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur in consequuntur possimus nulla vitae unde reiciendis veritatis, praesentium aspernatur, fugiat deserunt autem fuga! Ab sapiente ex sit. Voluptatum id quasi quibusdam itaque deserunt aperiam dolores error dolore, animi eum consectetur nostrum blanditiis officiis at modi enim maxime eaque velit cumque!")
bp2 = Blogpost(title="article2", subtitle = "subtitle", author = "author", date_created = date.today(), content_text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur in consequuntur possimus nulla vitae unde reiciendis veritatis, praesentium aspernatur, fugiat deserunt autem fuga! Ab sapiente ex sit. Voluptatum id quasi quibusdam itaque deserunt aperiam dolores error dolore, animi eum consectetur nostrum blanditiis officiis at modi enim maxime eaque velit cumque!")
bp3 = Blogpost(title="article3", subtitle = "subtitle", author = "author", date_created = date.today(), content_text = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur in consequuntur possimus nulla vitae unde reiciendis veritatis, praesentium aspernatur, fugiat deserunt autem fuga! Ab sapiente ex sit. Voluptatum id quasi quibusdam itaque deserunt aperiam dolores error dolore, animi eum consectetur nostrum blanditiis officiis at modi enim maxime eaque velit cumque!")


db.session.add(bp1)
db.session.add(bp2)
db.session.add(bp3)
db.session.commit()
print("working")