from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return ('Welcome to flask application')
@app.route('/hello')
def hello_world():
    return ('Welcome to CDAC ')
@app.route('/welcome')
def hello_world():
    return ('this is welcome page')

if __name__ == '__main__':
    app.run(debug=True)