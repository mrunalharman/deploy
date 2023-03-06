from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        return render_template('success.html', firstname = firstname, lastname = lastname)
    return render_template('home.html')
    

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True, threaded = True)