import pymongo
from pymongo import MongoClient
from important import mongodb

from flask import Flask, render_template, request


app = Flask(__name__)

# Connect to MongoDB Atlas
mongo_client = MongoClient(mongodb["link"])

# Select database
database = mongo_client["Pythontest"]

# Select collection
products = database["Product"]


# Display HTML form
@app.route("/")
def home():
    return render_template("product_form.html")


# Receive submitted form data
@app.route("/submit", methods=["POST"])
def submit():

    # Get data submitted from HTML
    product_name = request.form.get("product_name")
    quantity = request.form.get("quantity")
    unit_price = request.form.get("unit_price")
    payment_method = request.form.get("payment_method")
    district = request.form.get("district")

    # Create MongoDB document
    data = {
        "product_name": product_name,
        "quantity": int(quantity),
        "unit_price": float(unit_price),
        "payment_method": payment_method,
        "district": district
    }

    # Insert data into MongoDB
    result = products.insert_one(data)

    # Display success message
    return render_template(
        "product_form.html",
        message="Product submitted successfully!"
    )


if __name__ == "__main__":
    app.run(debug=True)
