# Cameroon Fruit Recognizer ���

A advanced image recognition application tailored for identifying the most frequent fruits in Cameroon using a hybrid deep learning and computer vision approach.

## 📁 Project Structure

- **src/**: Source code for the application and GUI.
- **models/**: Pre-trained models (VGG16 features, SVM classifier).
- **data/**: Dataset and test images.
- **documentation/**: Project reports, methodology details, and old READMEs.
- **notebooks/**: Jupyter notebooks for experimentation and model training.
- **requirements.txt**: List of dependencies for the project.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- TensorFlow, OpenCV, joblib, rembg, customtkinter

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cameroon-fruit-recognizer.git
   cd cameroon-fruit-recognizer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To start the recognition interface:
```bash
python src/interfacefrec.py
```

## 🧠 Methodology

### 📊 Dataset
The models were trained on a dataset composed of:
- **FID30 dataset**: A standard dataset for fruit identification.
- **Manual Collection**: Specialized dataset of Cameroon-specific fruit varieties collected manually to improve local accuracy.

### ⚙️ Preprocessing & Feature Extraction
The application targets **Ananas, Oranges, Bananes, Avocats, and Watermelons**. The pipeline includes:
1.  **Background Removal**: Automated background subtraction to focus on the fruit item.
2.  **Hybrid Feature Extraction**:
    - **CNN (Deep Learning)**: Using VGG16 to extract high-level semantic features.
    - **SIFT (Computer Vision)**: Using Scale-Invariant Feature Transform to capture local texture and shape descriptors.
3.  **Fusion & Learning**: Combined features are fed into an SVM classifier for final prediction.

## 📝 Authors
- Student Group 7 (University Project)

## ⚖️ License
MIT License
