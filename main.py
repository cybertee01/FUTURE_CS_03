from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename

import os
from cryptography.fernet import Fernet


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

# Generate a key once and save it securely. For demo, hardcoded here:
# To generate a key: Fernet.generate_key()
FERNET_KEY = Fernet.generate_key()  # Replace with your actual key
fernet = Fernet(FERNET_KEY)

from wtforms.validators import DataRequired

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[DataRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET', "POST"])
@app.route('/home', methods =['GET', "POST"])

def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        upload_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'])
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_bytes = file.read()
        encrypted = fernet.encrypt(file_bytes)
        filename = secure_filename(file.filename) + '.enc'
        with open(os.path.join(upload_folder, filename), 'wb') as f:
            f.write(encrypted)
        return "File has been uploaded and encrypted."
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)