#################
# Elvin Canseco
# ec3456
# Final
#
#################

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template('index.html')

#static route
@app.route("/interests")
def assgns():
    return render_template('assignments.html')

#static route
@app.route("/classes")
def clss():
    return render_template('classes.html')

#start the server
if __name__ == "__main__":
    app.run()