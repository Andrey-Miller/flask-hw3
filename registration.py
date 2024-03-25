from flask import Flask, flash, redirect, render_template, url_for
from flask_wtf.csrf import CSRFProtect
from form import RegistrationForm
from model import db, User


app = Flask(__name__)
app.config['SECRET_KEY'] = b'000d88cd9d90036ebdd237eb6b0db000'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def register():
    db.create_all()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Пользователь успешно зарегистрирован', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
