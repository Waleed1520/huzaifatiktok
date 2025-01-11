from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

# Set upload folder
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def home():
    return 'Welcome to the upload server!'

# Handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return f'File uploaded successfully: {file.filename}'

# Serve files from the upload folder
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
