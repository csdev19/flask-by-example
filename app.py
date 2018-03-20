from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
	return "Hola Allison :v"

@app.route('/<name>')
def hello_name(name):
	return "Hola {}!".format(name)


if __name__ == '__main__':
	app.run()