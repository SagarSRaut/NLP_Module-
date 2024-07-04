# from flask import Flask
# app=Flask(__name__)

# @app.route('/')
# def hello_world():
#     return ('Welcome to home')

# if __name__ == '__main__':
#     # app.run(debug=True)


from flask import Flask
app=Flask(__name__)

@app.route('/<name>')
def world():
    return ('Hello %s' %name)
@app.route('/')
def hello_world():
    return ('this is home sagar')
if __name__ == '__main__':
    app.run(debug=True)