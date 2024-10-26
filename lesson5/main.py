# WHY = we need to be able to collect data from users!
# 1. utilize route variables to get data from the URL

# standard flask boilerplate

# import the Flask server object
from flask import Flask, request

# create new Flask instance and assign it a root directory of the 
# working file (should be named 'main.py')
app = Flask(__name__)

#create some routes
@app.route('/')
def displayHomepage():
    return "<h1>Welcome to your first Website!</h1>"

@app.route('/route1')
def route1Info():
    return "<h3>Congrats on making route1!</h3>"

# <> denote a route variable
@app.route('/profile/<users_name>')
def profile(users_name):
    return "<h2>Hello " + users_name + "!</h2>"

@app.route('/date/<month>/<day>/<year>')
def displayGivenDate(month, day, year):
    return f"{month} / {day} / {year}"

# creating a <form>!
formData = f"""
    <form action="/results" method="GET">
        What's your favorite pizza flavor?
        <input type="text" name="pizza_flavor">
        <br>
        What's your favorite crust type?
        <input type="text" name="crust">
        <input type="submit" value="submit pizza!">
    </form>
    """

@app.route('/formExample')
def firstForm():
    return formData

@app.route('/results', methods=['GET'])
def simple_pizza_results():
    pizza_flavor = request.args.get("pizza_flavor")
    crust = request.args.get("crust")
    return f"<h3>{crust} - crust {pizza_flavor} pizza has been ordered!</h3>"

# the server can be accessed in your web browser using the URL localhost:3000/
if __name__ == '__main__':
    app.run(debug=True, port=3000)