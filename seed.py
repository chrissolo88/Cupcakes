from models import db,connect_db, Cupcake, CupcakeIngredient, Ingredient
from app import app

db.drop_all()
db.create_all()

cupcakes = [
    Cupcake(flavor="chocolate", size="regular", rating=4.1,image="https://sallysbakingaddiction.com/wp-content/uploads/2017/06/moist-chocolate-cupcakes-3.jpg"),
    Cupcake(flavor="orange creamsicle", size="regular", rating=4.8,image="https://www.thecreativebite.com/wp-content/uploads/2022/02/orange-cupcakes-image-copy-1024x678.jpg"),
    Cupcake(flavor="vanilla", size="regular", rating=4.4,image="https://natashaskitchen.com/wp-content/uploads/2020/05/Vanilla-Cupcakes-3.jpg"),
    Cupcake(flavor="red velvet", size="regular", rating=4,image="https://www.allrecipes.com/thmb/d3swQwV-qjtE5-Bm6YgPS4j2l3o=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/5789703-f0c4b179200b43a5bcd1ef90748c29fe.jpg"),
    Cupcake(flavor="chocolate", size="regular", rating=4)
]

db.session.add_all(cupcakes)
db.session.commit()

ingredients = [
    Ingredient(name='flour'),
    Ingredient(name='cocoa powder'),
    Ingredient(name='baking powder'),
    Ingredient(name='baking soda'),
    Ingredient(name='salt'),
    Ingredient(name='eggs'),
    Ingredient(name='granulated sugar'),
    Ingredient(name='brown sugar'),
    Ingredient(name='canola oil'),
    Ingredient(name='vanilla extract'),
    Ingredient(name='buttermilk'),
    Ingredient(name='butter'),
    Ingredient(name='sour cream'),
    Ingredient(name='orange zest'),
    Ingredient(name='milk'),
    Ingredient(name='orange juice'),
    Ingredient(name='powdered sugar'),
    Ingredient(name='red food coloring'),
    Ingredient(name='cream cheese')
]

db.session.add_all(ingredients)
db.session.commit()

cupcake_ingredients = [
    CupcakeIngredient(cupcake_id=1,ingredient_id=1,quantity='3/4 C'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=2,quantity='1/2 C'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=3,quantity='3/4 tsp'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=4,quantity='1/2 tsp'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=5,quantity='1/4 tsp'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=6,quantity='2 Large'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=7,quantity='1/2 C'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=8,quantity='1/2 C'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=9,quantity='1/3 C'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=10,quantity='2 tsp'),
    CupcakeIngredient(cupcake_id=1,ingredient_id=11,quantity='1/2 C'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=12,quantity='2 C'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=7,quantity='1 1/2 C'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=6,quantity='2 Large'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=13,quantity='3/4 C'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=14,quantity='2.5 Tbsp'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=15,quantity='3/4 C'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=16,quantity='1/2 C'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=10,quantity='3 tsp'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=1,quantity='2 1/2 C'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=5,quantity='1 tsp'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=4,quantity='1/2 tsp'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=3,quantity='1 1/2 tsp'),
    CupcakeIngredient(cupcake_id=2,ingredient_id=17,quantity='4 C'),
    CupcakeIngredient(cupcake_id=3,ingredient_id=1,quantity='1 1/4 C'),
    CupcakeIngredient(cupcake_id=3,ingredient_id=3,quantity='1 1/4 tsp'),
    CupcakeIngredient(cupcake_id=3,ingredient_id=5,quantity='1/2 tsp'),
    CupcakeIngredient(cupcake_id=3,ingredient_id=12,quantity='1/2 C'),
    CupcakeIngredient(cupcake_id=3,ingredient_id=7,quantity='3/4 C'),
    CupcakeIngredient(cupcake_id=3,ingredient_id=6,quantity='2 Large'),
    CupcakeIngredient(cupcake_id=3,ingredient_id=10,quantity='2 tsp'),
    CupcakeIngredient(cupcake_id=3,ingredient_id=11,quantity='1/2 C'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=1,quantity='2 1/2 C'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=2,quantity='1/2 C'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=4,quantity='1 tsp'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=5,quantity='1/2 tsp'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=7,quantity='2 C'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=12,quantity='1 1/4 C'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=6,quantity='4 Large'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=13,quantity='1 C'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=15,quantity='1/2 C'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=18,quantity='1 oz'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=10,quantity='4 tsp'),
    CupcakeIngredient(cupcake_id=4,ingredient_id=19,quantity='8 oz'),
]

db.session.add_all(cupcake_ingredients)
db.session.commit()