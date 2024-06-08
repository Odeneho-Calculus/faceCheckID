from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from api.utils import search_by_face, extract_image_urls  # Ensure correct import path

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        error, search_results = search_by_face(filepath)

        if search_results:
            images_with_urls = []
            for result in search_results:
                if 'base64' in result:
                    image_url = result['base64']
                    score = result.get('score', 0)
                    images_with_urls.append((score, [image_url]))
                else:
                    print(f"No 'base64' key in result: {result}")
            return render_template('results.html', images_with_urls=images_with_urls)
        else:
            return render_template('error.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
