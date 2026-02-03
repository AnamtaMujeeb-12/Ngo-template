from flask import Flask, render_template

# create Flask object
app = Flask(__name__)

# root route
@app.route("/")
def home():
    return render_template("index.html")

# other routes
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/donate")
def donate():
    return render_template("donate.html")

@app.route("/causes")
def causes():
    return render_template("causes.html")

@app.route("/events")
def events():
    return render_template("event.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

# main check
if __name__ == "__main__":
    app.run()   # use debug only during development
