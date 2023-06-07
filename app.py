# Import the required libraries
from flask import Flask, render_template, request, redirect, url_for
from joblib import load
import pickle

# Load the pipeline object
# pipeline = load("fake_news_classification.joblib")
with open('fake_news_classification.pkl', 'rb') as f:
    pipeline = pickle.load(f)

# Function to get the result for a particular text query


def requestResults(name):
    check = pipeline.predict(name)
    out = "Fake News" if check == 1 else "Real News"
    return str(out)


# Start flask
app = Flask(__name__)

# Render default webpage


@app.route('/')
def home():
    return render_template('home.html')

# When post method is detected, redirect to success function


@app.route('/', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', name=user))

# Get the data for the requested query


@app.route('/success/<name>')
def success(name):
    return str(requestResults([name]))


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
