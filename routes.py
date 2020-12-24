from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
from scripts.forms import Login, Register
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '21dc6ebfa6175fda2e66a757eb1c10c8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

database = SQLAlchemy(app)

class User(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(20), unique=True, nullable=False)
    email = database.Column(database.String(20), unique=True, nullable=False)
    image = database.Column(database.String(20), nullable=False, default='default.jpg')
    password = database.Column(database.String(60), nullable=False)
    posts = database.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}')"


class Post(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(20), nullable=False)
    last_update = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    content = database.Column(database.Text, nullable=False)
    image = database.Column(database.String(20))
    video = database.Column(database.String(20))
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"User('{self.title}', '{self.last_update}')"



@app.route('/')
def index():
    """
    This route is for the home page
    """
    return render_template('index.html', title='Kisan Times')

@app.route('/new')
def new():
    """
    This route is for creating new container or tag
    """
    return render_template('new.html', title='New Post')

@app.route('/login', methods=['GEt', 'POST'])
def login():
    """
    This route is for users to login after they register
    """
    form = Login()

    if form.is_submitted():
        flash('Welcome')
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    This route is for regiseration purposes so that a user can post content
    Get all request methods and verify the register form
    """

    form = Register()

    if form.is_submitted():
        print('Validated')
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('index'))

    return render_template('register.html', form=form)