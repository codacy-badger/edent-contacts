from chalice import Chalice

app = Chalice(app_name='edent-contacts')


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/hello/{name}')
def hello_name(name):
    return {'hello': name}


@app.route('/users', methods=['POST'])
def create_user():
    user_as_json = app.current_request.json_body
    return {'user': user_as_json}
