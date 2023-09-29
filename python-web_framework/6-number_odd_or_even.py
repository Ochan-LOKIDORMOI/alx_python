'''
Write a script that starts a 
Flask web application: The application
must run on port the default port 
and must run on 0.0.0.0
'''
# import flask module
from glob import escape
from flask import Flask, render_template


# define a flask instance
app = Flask(__name__)
# set strict_s;ashes flag to false

# create a route for index
@app.route('/')
# a function for
def hello():
    '''
    a function definition that return
    a strin hello... on a get request 
    to a router page
    param: 
        type: NONE
    Return:
        type: String
    '''
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    '''
    a function definition that return
    a strin hello... on a get request 
    to a router page
    param: 
        type: NONE
    Return:
        type: String
    '''
    return "HBNB"

@app.route('/c/<text>')
def hbnb_C_is_fun(text):
    '''
    a function definition that return
    a strin hello... on a get request 
    to a router page
    param: 
        type: type
    Return:
        type: String
    '''
    return f"C {text.replace('_', ' ')}"

@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    '''
    this return a default text is cool
    if no param is passed
    param:
        type: string
    Return:
        type: string
    '''
    return f"Python {escape(text.replace('_', ' '))}"

@app.route('/number/<int:n>')
def hello_id(n):
    '''
    Funtion tha return the int param passed
    Param:
        type:
    Return:
        type: string + value pass
    '''
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def hello_number_templates(n):
    '''
    Funtion that pass a param to a defines templates
    Param:
        type: int
    return:
        HTML with the value passed
    '''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_or_odd(n):
    if n%2 == 0:
        msg = 'even'
    else:
        msg ='odd'
    return render_template('6-number_odd_or_even.html', n=n, msg=msg)

if __name__=='__main__':
    # for every route
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', debug=True)
