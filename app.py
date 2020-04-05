import os
import json
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, make_response

from werkzeug.utils import secure_filename
import filecmp

# Config
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
MAX_CONTENT_SIZE_MB = 120

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Setup the app 
app = Flask(__name__, static_url_path="/static")
app.debug = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_SIZE_MB * 1024 * 1024

@app.route('/', methods=['GET', 'POST'])
def index():

    # When a new POST request is received 
    # if (request.method == 'POST'):

    #     # Check if a file is attached 
    #     if ('file' not in request.files):
    #         print('No file attached in request')
    #         return render_template('index.html')  

    #     # Check if valid file 
    #     file = request.files['file']
    #     if (not file or file.filename == ''):
    #         print('No file selected')
    #         return render_template('index.html')  

    #     # Make sure the filename is safe
    #     filename = secure_filename(file.filename)

    #     # Save the file to the upload folder 
    #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    #     return render_template('index.html')   

    return render_template('index.html')    

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)