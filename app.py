from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloworld():
	return 'Accepted'


def create_app():
   return app