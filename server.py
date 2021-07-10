from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', times=3, color="peru")


@app.route('/<int:times>')
def times(times):
    return render_template('index.html', times=times, color="slateblue")

@app.route('/<int:times>/<string:color>')
def colores(times, color):
    return render_template('index.html',
    times=times, color=color)


if __name__=="__main__":
    app.run(debug=True)