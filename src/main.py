# import the Flask library 
from flask import Flask 
  
  
# Create the Flask instance and pass the Flask 
# constructor, the path of the correct module 
app = Flask(__name__) 
  
  
# Default route added using a decorator, for view function 'welcome' 
# We pass a simple string to the frontend browser 
@app.route('/') 
def welcome(): 
    return "Hello! Let us learn about importance of Exercise!"
  
  
# Start with flask web app, with debug as True,# only if this is the starting page 
if(__name__ == "__main__"):
    app.run(debug=True)
