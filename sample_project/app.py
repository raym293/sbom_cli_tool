from flask import Flask
import requests
import pandas as pd

app = Flask(__name__)

data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'score': [85, 92, 78]
})

@app.route('/')
def index():
    # Make a simple HTTP request to demonstrate requests usage
    _ = requests.get('https://httpbin.org/get')
    # Show a simple HTML table using pandas
    return data.to_html(index=False)

if __name__ == '__main__':
    app.run(debug=True)
