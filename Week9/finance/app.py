import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter for formatting currency
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # Get the user ID from session
    user_id = session["user_id"]

    # Query for all the stocks the user holds
    rows = db.execute("SELECT * FROM holding WHERE user_id = ?", user_id)

    # Query for the user's available cash
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash[0]['cash']

    # Initialize sum of assets (cash + stock value)
    sum = cash

    # Update stock info and calculate total value
    for row in rows:
        look_up = lookup(row['symbol'])  # Get stock details using the lookup function
        row['name'] = look_up['name']
        row['price'] = look_up['price']
        row['total'] = row['price'] * row['shares']

        # Add stock total value to sum
        sum += row['total']

        # Format price and total using the USD filter
        row['price'] = usd(row['price'])
        row['total'] = usd(row['total'])

    # Render the index.html template with the stock holdings and cash
    return render_template("index.html", rows=rows, cash=usd(cash), sum=usd(sum))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        # Ensure symbol and shares are provided
        if not request.form.get("symbol"):
            return apology("must provide stock symbol", 400)
        if not request.form.get("shares"):
            return apology("must provide stock shares", 400)

        user_id = session["user_id"]
        symbol = request.form.get("symbol")

        # Validate shares input as a positive integer
        try:
            shares = int(request.form.get("shares"))
            if shares < 1:
                return apology("Invalid share input", 400)
        except ValueError:
            return apology("Shares must be a positive integer", 400)

        # Lookup stock symbol for price
        look_up = lookup(symbol)
        if look_up == None:
            return apology("Provide valid symbol", 400)

        price = look_up["price"]
        cost = price * shares

        # Query user cash balance
        c = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = c[0]["cash"]

        # Check if user has enough cash to buy
        if cash < cost:
            return apology("You do not have enough cash", 400)

        # Check if user already owns this stock and update the number of shares
        check = db.execute(
            "SELECT shares FROM holding WHERE user_id = ? AND symbol = ?", user_id, symbol)

        if len(check) > 0:
            # If user already holds this stock, update the shares count
            db.execute(
                "UPDATE holding SET shares = shares + ? WHERE user_id = ? AND symbol = ?", shares, user_id, symbol)
        else:
            # Otherwise, insert a new record for the stock
            db.execute("INSERT INTO holding(symbol, shares, user_id) VALUES(?, ?, ?)",
                       symbol, shares, user_id)

        # Update the user's cash balance
        db.execute("UPDATE users SET cash = cash - ? WHERE users.id = ?", cost, user_id)

        # Record the transaction in history
        db.execute("INSERT INTO history (user_id, symbol, shares, price, method) VALUES(?, ?, ?, ?, ?)",
                   user_id, symbol, shares, price, "buy")

        # Redirect to homepage
        return redirect("/")

    else:
        # Render the buy form
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Query for transaction history
    rows = db.execute("SELECT * FROM history")

    # Render the history template with the transaction data
    return render_template("history.html", rows=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Check if username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember logged in user
        session["user_id"] = rows[0]["id"]

        # Redirect to homepage
        return redirect("/")

    else:
        # Render login form
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget user session
    session.clear()

    # Redirect to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        # Ensure stock symbol is provided
        if not request.form.get("symbol"):
            return apology("must provide stock symbol", 400)

        symbol = request.form.get("symbol")
        value = lookup(symbol)
        if value == None:
            return apology("Provide valid symbol", 400)

        # Render quoted template with stock information
        return render_template("quoted.html", value=value)
    else:
        # Render the quote form
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # Ensure username, password, and confirmation are provided
        if not request.form.get("username"):
            return apology("must provide username", 400)
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password does not match confirmation", 400)

        username = request.form.get("username")
        password = request.form.get("password")

        # Generate password hash
        hash = generate_password_hash(password)

        # Register user in the database
        try:
            db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, hash)
        except ValueError:
            return apology("username already exists", 400)

        # Redirect to login page
        return render_template("login.html")

    else:
        # Render the registration form
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        # Ensure stock symbol and shares are provided
        if not request.form.get("symbol"):
            return apology("must provide stock symbol", 400)
        if not request.form.get("shares"):
            return apology("must provide stock shares", 400)

        user_id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        if shares < 1:
            return apology("Invalid share input", 400)

        # Validate stock symbol
        if lookup(symbol) == None:
            return apology("Provide valid symbol", 400)

        # Query for the user's current shares
        s = db.execute("SELECT shares FROM holding WHERE user_id = ? AND symbol = ?",
                       user_id, symbol)
        sharecount = s[0]["shares"]

        # Check if user has enough shares to sell
        if sharecount < shares:
            return apology("You do not have this amount of shares", 400)

        # Get stock price and calculate profit
        price = lookup(symbol)["price"]
        profit = price * shares

        # Update shares and cash balance
        db.execute("UPDATE holding SET shares = shares - ? WHERE user_id  = ?", shares, user_id)
        db.execute("UPDATE users SET cash = cash + ? WHERE users.id = ?", profit, user_id)
        db.execute("DELETE FROM holding WHERE shares = 0 AND user_id = ?", user_id)

        # Log the transaction in history
        db.execute("INSERT INTO history (user_id, symbol, shares, price, method) VALUES(?, ?, ?, ?, ?)",
                   user_id, symbol, shares, price, "sell")

        # Redirect to homepage
        return redirect("/")

    else:
        # Render the sell form with user's current stocks
        user_id = session["user_id"]
        stocks = db.execute("SELECT symbol FROM holding WHERE user_id = ?", user_id)
        return render_template("sell.html", stocks=stocks)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Add cash to user's account"""

    if request.method == "POST":
        # Get the amount to add and update user balance
        amount = float(request.form.get("amount"))
        user_id = session["user_id"]
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", amount, user_id)

        # Redirect to homepage
        return redirect("/")
    else:
        # Render the add cash form
        return render_template("add_cash.html")


@app.route("/retrieve_cash", methods=["GET", "POST"])
@login_required
def retrieve_cash():
    """Retrieve cash from user's account"""

    if request.method == "POST":
        # Get the amount to retrieve and check if user has enough cash
        amount = float(request.form.get("amount"))
        user_id = session["user_id"]
        c = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        cash = c[0]["cash"]

        if cash < amount:
            return apology("You don't have that much cash", 400)

        # Update user balance
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", amount, user_id)

        # Redirect to homepage
        return redirect("/")
    else:
        # Render the retrieve cash form
        return render_template("retrieve_cash.html")
