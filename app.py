__author__ = "Nathan Oldridge aka ChemistNate"
__version__ = 0.1
__description__ = "A replacement for RunStrat.com"
__website__ = "www.strat.run"

import os

''' READING THE DATA FILE '''
# Current directory for Flask app
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Current directory for Flask app + file name
# Use this file_path variable in your code to refer to your file 
file_path = os.path.join(APP_ROOT, 'data.csv')
print("File Path String: ", file_path)
print("Is that right?")


PORT = os.environ["PORT"]
print("App has started.")
#import yfinance
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/ticker/<tickerSymbol>')
def hello_name(tickerSymbol):
    tickerSymbol = str(tickerSymbol).upper()
    import yfinance as yf
    import getStrats
    hist = yf.Ticker(tickerSymbol).history(period="2y", interval="1d")
    del hist['Volume']
    del hist['Dividends']
    del hist['Stock Splits']
    return render_template('singleTicker.html', tickerX=tickerSymbol, dailyX=getStrats.getDailyStrats(hist), weeklyX=getStrats.getWeeklyStrats(hist))

@app.route('/')
def homepage():
   return '<html><head><title>title</title></head><body>Home page strat.run</body></html>'
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT) # use_reloader=True,  USE THIS FOR PROD
    #app.run(host='127.0.0.1') # USE THIS FOR DEV
    
    
    
#print("App now shutting down.")

