from flask import Flask, render_template, request, redirect, send_file
import os
import json
import csv
from werkzeug.utils import secure_filename
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def clean_value(val):
    """Convert PIL EXIF types to JSON-serializable Python types."""
    if isinstance(val, bytes):
        try:
            return val.decode(errors='ignore')
        except:
            return str(val)
    elif hasattr(val, 'numerator') and hasattr(val, 'denominator'):
        try:
            return float(val.numerator) / float(val.denominator)
        except:
            return str(val)
    elif isinstance(val, tuple):
        return [clean_value(x) for x in val]
    elif isinstance(val, dict):
        return {clean_value(k): clean_value(v) for k, v in val.items()}
    else:
        return val

def extract_metadata(image_path):
    """Extract and clean EXIF metadata from image."""
    image = Image.open(image_path)
    info = image._getexif()
    metadata = {}

    if info is None:
        return metadata

    for tag, value in info.items():
        tag_name = TAGS.get(tag, tag)
        if tag_name == "GPSInfo":
            gps_data = {}
            for t in value:
                sub_tag = GPSTAGS.get(t, t)
                gps_data[sub_tag] = clean_value(value[t])
            metadata["GPSInfo"] = gps_data
        else:
            metadata[tag_name] = clean_value(value)

    return metadata

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)

        image = request.files['image']
        if image.filename == '':
            return redirect(request.url)

        if image:
            filename = secure_filename(image.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            image.save(filepath)

            metadata = extract_metadata(filepath)

            # Save metadata to JSON and CSV
            json_path = os.path.join(RESULT_FOLDER, 'metadata.json')
            csv_path = os.path.join(RESULT_FOLDER, 'metadata.csv')

            with open(json_path, 'w') as f:
                json.dump(metadata, f, indent=4)

            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Tag', 'Value'])
                for key, value in metadata.items():
                    writer.writerow([key, value])

            return render_template('result.html', metadata=metadata, filename=filename)

    return render_template('index.html')

@app.route('/download/<filetype>')
def download(filetype):
    if filetype == 'json':
        return send_file(os.path.join(RESULT_FOLDER, 'metadata.json'), as_attachment=True)
    elif filetype == 'csv':
        return send_file(os.path.join(RESULT_FOLDER, 'metadata.csv'), as_attachment=True)
    else:
        return "Invalid file type", 400

if __name__ == '__main__':
    app.run(debug=True)
