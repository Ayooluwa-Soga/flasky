from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)

# index route with route decorators


@app.route('/')
def index():
    return "<h1>This is the home page!</h1>"


@app.route('/user/<name>')
def hello(name):
    return render_template('user.html', name=name)

# custom error pages

# invalid url


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# internal server error


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
