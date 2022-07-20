from flask import redirect, render_template, url_for

from market import app, db
from market.forms import RegisterForm
from market.models import Item, User


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password_hash=form.password.data,
        )
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("market_page"))

    if form.errors != {}:
        for error_message in form.errors.values():
            print(f"There was an error: {error_message}")

    return render_template("register.html", form=form)
