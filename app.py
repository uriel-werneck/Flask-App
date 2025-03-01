from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Todo-List")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title="Login")

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', title='Create your account')

if __name__ == '__main__':
    app.run(debug=True)