from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route (homepage)
@app.route('/')
def home():
    return "Hello, Flask! 👋 This is your first web app."

# Run the app
if __name__ == '__main__':
    app.run(debug=True)