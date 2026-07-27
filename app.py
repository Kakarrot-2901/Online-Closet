from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Demo credentials
USERNAME = "Aditya"
PASSWORD = "1701"

NAME='ANUSHKA'
@app.route('/landing')
def home():
    return render_template('landing.html', name=NAME)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USERNAME and password == PASSWORD:
            print("Login Successful")
            return redirect(url_for('main'))
        else:
            return render_template(
                'Online Wadrobe.html',
                error="Invalid username or password"
            )

    return render_template('Online Wadrobe.html')


@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == "__main__":
    app.run(debug=True)