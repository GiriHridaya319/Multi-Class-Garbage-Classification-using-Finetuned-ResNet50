# 🧠🚮 Multi-Class Garbage Classification with ResNet50, FastAPI & Docker

A deep learning-powered web application for intelligent garbage classification. Built using a fine-tuned ResNet50 model, served via FastAPI, and fully containerized with Docker for seamless deployment.

---

## 🚀 Features

- ⚡ FastAPI backend for speed and simplicity
- 🧠 Deep learning model (ResNet50 trained with PyTorch)
- 📦 Dockerized for easy deployment
- 🌐 Simple drag & drop UI (HTML + Bootstrap)
- 🔍 Predicts garbage category and shows top 3 predictions with confidence

---

## 🧠 Model Info

- Model: `garbage_resnet50_final_model.pth`
- Framework: PyTorch
- Classes:
```

\[
"white-glass", "trash", "shoes", "plastic", "paper", "metal",
"green-glass", "clothes", "cardboard", "brown-glass",
"biological", "battery"
]

```

---

## 📁 Project Structure

```

garbage-classification/
├── app/
│   ├── main.py             # FastAPI entry point
│   ├── model.py            # Classifier logic and model loading
│   ├── utils.py            # Validation and helper functions
│   ├── templates/
│   │   └── index.html      # UI page
│   └── static/
│       ├── css/
│       │   └── styles.css  # Optional custom styles
│       └── js/
│           └── script.js   # JS for frontend interactivity
├── garbage\_resnet50\_final\_model.pth
├── requirements.txt
├── Dockerfile
└── README.md

````

---

## 🧰 Installation (without Docker)

1. **Clone the repository**

```bash
git clone https://github.com/your-username/garbage-classification.git
cd garbage-classification
````

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the FastAPI server**

```bash
uvicorn app.main:app --reload
```

5. **Visit the App**

Open in browser: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Run with Docker (Recommended)

### 1. **Build Docker image**

```bash
docker build -t hridayagirii/garbage-classifier-ui .
```

> 🔁 Rebuild the image anytime you change code or files.

### 2. **Run Docker container**

```bash
docker run -p 8000:8000 hridayagirii/garbage-classifier-ui
```

### 3. **Open in browser**

* UI: [http://localhost:8000](http://localhost:8000)
* API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📷 Using the Web App

1. Drag & drop or click to upload an image.
2. Click **"Classify Image"**.
3. See the predicted garbage class, confidence, and top 3 predictions.

---

## 🔌 API Endpoints

### `POST /predict`

* Accepts: `multipart/form-data` image file (`file`)
* Returns:

```json
{
  "class": "plastic",
  "confidence": 92.54,
  "top_three": [
    ["plastic", 92.54],
    ["metal", 3.12],
    ["trash", 1.75]
  ]
}
```

### `GET /health`

* Returns server status & timestamp.

---

## 🛠️ Development Notes

* Built using FastAPI and Uvicorn
* Docker image uses `python:3.9-slim`
* Prediction uses `.pth` model (ensure the path is correct in `model.py`)
* Handles image validation and preprocessing

---

## 📤 Pushing to Docker Hub

1. Login:

```bash
docker login
```

2. Tag and push:

```bash
docker tag garbage-classifier-ui your-dockerhub-username/garbage-classifier-ui
docker push your-dockerhub-username/garbage-classifier-ui
```

---

## 👨‍💻 Contributing

Pull requests are welcome! Feel free to open issues or suggest improvements.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

* FastAPI for backend
* PyTorch + torchvision
* Bootstrap for UI

```



![image](https://github.com/user-attachments/assets/22e48147-7264-45b4-9968-7c0323bab911)

![image](https://github.com/user-attachments/assets/fa93981d-7c8b-4740-a589-b1e760e23bc4)

![image](https://github.com/user-attachments/assets/535675ae-6a7f-4681-806e-74cbf9a00443)




