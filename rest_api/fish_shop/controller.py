from main import app

@app.route('/')
def index():
    return "Hooray";

@app.route('/<id>')
def get_fish(id):
    print(id)
    return "my fish is gorgeous"
@app.route('/fish', methods=["GET"])
def fish_get():
    return "Get_Method check"

@app.route('/fish', methods=["POST"])
def create_fish():
    return "Post_method_check"
