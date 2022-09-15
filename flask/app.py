from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def helloworld():
    data = request.form.to_dict()
    return render_template('index.html', title='ACCEPTED', comment=data['comment'])

def create_app():
    return app
