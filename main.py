from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return 'File received successfully', 200
    return 'No file uploaded', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
