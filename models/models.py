from db.db import db

class Restaurant(db.Model):
    __tablename__ = "restaurant"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    recipe_id = db.relationship("Recipes", backref="restaurant", lazy=True)

    def __repr__(self):
        return f"<Restaurant {self.name}>"

class Recipes(db.Model):  
    __tablename__ = "restaurant.recipies"
    
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), unique=True, nullable=False) 
    recipe_cost = db.Column(db.Float, nullable=False)
    
    # Foreign key column to link back to the restaurant
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"<Recipe {self.recipe_name}>"
