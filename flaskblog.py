from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cc6f62799e9c8cf9811eb2aa3a1c33fd'
posts = [
    {
        'author': 'Guy Meiri',
        'title': "Blog Post 1",
        'content': "Guygul the great",
        'date_posted': 'Jan 1 2020'},
    {
        'author': 'Balon Meiri',
        'title': "Blog Post 2",
        'content': "Balon the greater",
        'date_posted': 'Jan 1 2020'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='about')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash("login Unsucessful. Please check username and password", "danger")

    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
