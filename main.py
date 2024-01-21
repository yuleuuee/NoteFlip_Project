from website import create_app
from flask import Flask
# here "website" becomes the package name


app = create_app()
if __name__ == '__main__': # this means only if we run this file directly , we can run the web server
    app.run(debug=True) 
    # app.run() : will run our flask application
    # debug=true : everytime we make a change to our python code ,it will automatically re-run the web server 