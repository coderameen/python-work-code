#FLASK
'''
FLASK:" Flask is an web application framework used to control components like front-end, back-end and database"

* we can use flask to develop machine learning projects and deep learning projects
* To install flask we need to use command
"pip install Flask"   (command prompt)


from flask import Flask
#initialize the app
app = Flask(__name__)

#route to the path in browser
@app.route("/")
def home():
    return "Hello this is my home page!!"

if __name__=='__main__':
    app.run()

#-------------------------------------------

from flask import Flask

app  =  Flask(__name__)

@app.route("/")
def home():
    return "Home page"
@app.route("/hello")
def hello():
    return "Hello Alen!!!"

if __name__=='__main__':
    app.run()

        '''

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "This is my home page"
@app.route("/login")
def login():
    return "Welcome Alen, you successfully logged in!!!"

@app.route("/logout")
def logout():
    #return "logged out!!! Thank you!!"
    return redirect(url_for("home"))

if __name__=='__main__':
    app.run()