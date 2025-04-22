# 🖼️ Image Processing App with Gradio
## 📌 Overview
This project is an interactive web application for performing various image processing operations through a friendly UI built with [Gradio](https://www.gradio.app/). Users can upload an image and apply transformations such as:

- **Geometric transformations:** translation, rotation, and scaling.

- **Colorspace operations:** conversion to grayscale, HSV, LAB, and contrast adjustment.

- **Gamma correction:** adjust image brightness non-linearly.

>💡 This project was proposed as part of the Computer Vision course taught by Professor Helton Maia at UFRN. The original exercise is available [here](https://heltonmaia.com/computervision/chapters/ch1/ch1.html#exercicio-processamento-de-imagens-com-gradio).

## 🚀 Running the App

1.  **Clone the repository:** 
```bash
git clone <repository_url>; cd <your_project_directory>
```
2.  **Install dependencies:** 
```bash
pip install -r requirements.txt
```
3.  **Launch the Gradio app:** 
```bash
python app.py
```
- A local URL (e.g., http://127.0.0.1:7860) will appear in the terminal.
- Open it in your browser to interact with the app.

## 🧠 Architecture
The project follows a modular architecture inspired by the MVC (Model-View-Controller) pattern.
- **View:** The UI (`app.py`) defines the interface using Gradio components like sliders, dropdowns, and buttons.
**Controller:** `controller.py` acts as the bridge between the interface and the processing logic. It determines which operation to apply and passes the necessary arguments.
- **Model:** The `processing/` package contains the core image manipulation logic. The Image class wraps image data and exposes high-level operations.