from flask import Flask, request, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db, Cupcake,  CupcakeIngredient, Ingredient
from secrets import SECRET_KEY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = SECRET_KEY

connect_db(app)

@app.route('/')
def index_page():
    todos = Cupcake.query.all()
    return render_template('home.html')

@app.route('/api/cupcakes')
def list_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize(), ingredients=cupcake.ingredient_list)

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    image = request.json.get("image") if "image" in request.json else None
    new_cupcake = Cupcake(flavor=request.json["flavor"],size=request.json["size"],rating=request.json["rating"],image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json,201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.query(Cupcake).filter_by(id=id).update(request.json)
    db.session.commit()
    cupcake = Cupcake.query.get_or_404(id)
    response_json = jsonify(cupcake=cupcake.serialize())
    return (response_json,201)

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return (jsonify(message='deleted'),201)