import os

''' READING THE DATA FILE 
# Current directory for Flask app
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Current directory for Flask app + file name
# Use this file_path variable in your code to refer to your file 
file_path = os.path.join(APP_ROOT, 'data.csv')
print("Accessing: ", file_path)
print("never actuall read it.")
'''

PORT = os.environ["PORT"]
print("App has started.")
#import yfinance
from flask import Flask
app = Flask(__name__)
 
@app.route('/ticker/<name>')
def hello_name(name):
   return 'You have asked for %s. We have no data.' % name

@app.route('/')
def homepage():
   return '<html><head><title>title</title></head><body>Home page strat.run</body></html>'
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT) # use_reloader=True,  USE THIS FOR PROD
    #app.run(host='127.0.0.1') # USE THIS FOR DEV
    
    
    
#print("App now shutting down.")

