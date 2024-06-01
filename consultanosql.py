from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://jcarroyos:HdBAyK4FfWNHAhu2@cluster0.navzpoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Select the database and collection
db = client['mongodbVSCodePlaygroundDB']
collection = db['sales']

# Count the number of documents in the collection
try:
    num_sales = collection.count_documents({})
    print(f"Number of sales: {num_sales}")
except Exception as e:
    print(e)
