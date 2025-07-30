# 🖼️ Metadata Extractor & Privacy Analyzer

A simple, powerful web-based application that lets users upload images and extract hidden metadata (EXIF), such as GPS location, device information, and camera settings. This tool helps raise awareness about privacy risks embedded in image files.

---

## 📌 Features

✅ Upload `.jpg` or `.jpeg` images  
✅ Extract EXIF metadata like date, time, device model, GPS, ISO, aperture, and more  
✅ View metadata in a clean web interface  
✅ Download results in `.json` or `.csv` format  
✅ Automatically detects hidden or suspicious metadata  
✅ Fully offline – no internet or external APIs required  
✅ Supports modern image formats and robust error handling

---

## 🛠️ Technologies Used

- Python 3
- Flask (Web Framework)
- Pillow (for image metadata handling)
- HTML5, CSS3 (for frontend)

---

## 📂 Project Structure
```
metadata_analyzer/
├── app.py
├── uploads/
├── results/
├── templates/
│ ├── index.html
│ └── result.html
├── static/
│ └── style.css
└── README.md
```

## Create a Virtual Environment (optional but recommended)

```
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
```

## Install Dependencies
```
pip install Flask Pillow
```

## Run the App

```
python app.py
```

Go to http://127.0.0.1:5000 in your browser to use the app.

## 🧪 How It Works

a. When a user uploads an image, the app extracts all available EXIF metadata using the Pillow library.

b. GPS and other sensitive fields are decoded and presented in a readable format.

c. The user can download the metadata as a .json or .csv file for record or analysis.

d. The app identifies hidden networks and suspicious metadata entries that could impact privacy.

## 📁 Sample Output

<img width="1920" height="548" alt="Screenshot 2025-07-30 110704" src="https://github.com/user-attachments/assets/78f9bd41-c02e-4f96-bc2e-09c967b54d2a" />

<img width="1920" height="647" alt="Screenshot 2025-07-30 110637" src="https://github.com/user-attachments/assets/e9f8d713-be55-4fc8-87e4-fc136739600c" />

<img width="1920" height="482" alt="Screenshot 2025-07-30 111516" src="https://github.com/user-attachments/assets/7c82456b-b891-45f6-acd6-948a31c6d326" />

<img width="1920" height="937" alt="Screenshot 2025-07-30 112009" src="https://github.com/user-attachments/assets/44174608-8f7f-47ca-829b-df68d53e533f" />

### JSON Preview:
```
{
  "Model": "Canon EOS 80D",
  "DateTime": "2023:11:02 14:22:31",
  "GPSInfo": {
    "GPSLatitude": [12.9716, 0.0, 0.0],
    "GPSLongitude": [77.5946, 0.0, 0.0]
  }
}
```
## 🔐 Privacy Note
This tool does not store images or metadata permanently. All files are processed locally on your system and are deleted upon reload or shutdown.

## 📄 License
This project is open-source and free to use for educational, ethical, and non-commercial purposes.

## 🙋‍♂️ Author
#### Developed by S Kantha Sishanth
