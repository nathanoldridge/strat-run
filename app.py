''' READING THE DATA FILE 
import os
# Current directory for Flask app
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Current directory for Flask app + file name
# Use this file_path variable in your code to refer to your file 
file_path = os.path.join(APP_ROOT, 'data.csv')
print("Accessing: ", file_path)
print("never actuall read it.")



'''
print("App has started.")
#import yfinance
from flask import Flask
app = Flask(__name__)
 
@app.route('/ticker/<name>')
def hello_name(name):
   return 'You have asked for %s. We have no data.' % name
 
if __name__ == '__main__':
   app.run()

#print("App now shutting down.")

