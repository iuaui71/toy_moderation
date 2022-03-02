from crypt import methods
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def helloworld():
   return '{"response": "Accepted"}'

def create_app():
   return app