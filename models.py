from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    __tablename__ = "cupcakes"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.Text, nullable=False, default="https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg")
    ingredients = db.relationship('Ingredient',secondary="cupcakes_ingredients", backref="cupcakes")
    quantities = db.relationship('CupcakeIngredient', backref="cupcakes")
    
    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
    
    def __repr__(self):
        return f"<Cupcake {self.id} flavor={self.flavor} size={self.size} >"
    
    @property
    def ingredient_list(self):
        res = db.session.query(Ingredient.name,CupcakeIngredient.quantity).join(Ingredient).filter(CupcakeIngredient.cupcake_id==self.id).all()
        return res


class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
class CupcakeIngredient(db.Model):
    __tablename__ = "cupcakes_ingredients"
    cupcake_id = db.Column(db.Integer,db.ForeignKey('cupcakes.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer,db.ForeignKey('ingredients.id'), primary_key=True)
    quantity = db.Column(db.Text, nullable=False)