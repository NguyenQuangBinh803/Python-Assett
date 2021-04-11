__author__ = 'Edward J. C. Ashenbert'
__credits__ = ["Edward J. C. Ashenbert"]
__maintainer__ = "Edward J. C. Ashenbert"
__email__ = "nguyenquangbinh803@gmail.com"
__copyright__ = "Copyright 2020"
__status__ = "Vectorizing Image Project"
__version__ = "1.0.1"

import sys
import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('index.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000, ssl_context='adhoc')