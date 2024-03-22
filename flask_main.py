from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/contacts/')
def contacts():
    developer_name = "Frederic Rich"
    description = "О нас"
    return render_template('contacts.html', name = developer_name)
    return render_template('info.html', desc = description)


if __name__ == "__main__":
    app.run(debug=True)