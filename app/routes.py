from flask import render_template, flash, redirect, url_for
from app import app, database as db
from app.scripts.models import User, Post
from app.scripts.forms import Login, Register


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
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        print('Validated')
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('index'))

    return render_template('register.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)