import os
from flask import Flask, flash, request, redirect, url_for, render_template
# request
from werkzeug.utils import secure_filename
# check the name of file
import cv2
from datetime import datetime as dt


UPLOAD_FOLDER = 'static/uploads/'
# Upload directory
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_folder = "static")

# APP CONFIGURATIONS
app.config['SECRET_KEY']= 'YourSecretKey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Convert to grayscale function
def rgb_to_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Save the uploaded file as name of current time
            dt_now = dt.now().strftime("%Y%m%d%H%M%S%f")
            filename = dt_now + ".jpg"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # PATH to static files
            img_dir = "./static/uploads/"
            path = img_dir + filename
            #Import picture date
            img = cv2.imread(path)
            # if img has date
            if len(img) != 0:
                #Convert to grayscale from uploaded picture
                gray = rgb_to_gray(img)
                #### Save the uploaded file as name of current time
                dt_now = dt.now().strftime("%Y%m%d%H%M%S%f")
                img_name = "gray" + dt_now + ".jpg"
                #PATH to save directory
                img_path = img_dir + img_name
                cv2.imwrite(os.path.join(img_dir + img_name), gray)
        return render_template('index.html', img_path=img_path)


if __name__ == '__main__':
    app.run()
