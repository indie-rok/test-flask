from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and view function
@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/json')
def json():
    return {"my_message": "cool", "value": 10}

@app.route('/html')
def html():
    return "<h1>You can also return HTML</h1>"

# Run the Flask web server
if __name__ == '__main__':
    app.run(debug=True)
