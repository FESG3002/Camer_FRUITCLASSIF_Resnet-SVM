import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import numpy as np
import joblib
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from io import BytesIO


import tensorflow as tf
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model
import os
from rembg import remove 

# Get the directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))
models_dir = os.path.join(base_dir, '..', 'models')

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

local_weights_file = os.path.join(models_dir, 'poidmodvg5.h5')
base_model = VGG16(weights=local_weights_file, include_top=False)
modelnn = Model(inputs=base_model.input, outputs=base_model.get_layer('block5_pool').output)

def load_and_preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)    
    img_array = preprocess_input(img_array)
    return img_array

class FruitRecognitionApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fruit Recognizer")
        self.geometry("1000x700")  # Increased height to accommodate new elements

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Fruit Recognizer", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Recognize Fruit", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                     command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(3, weight=1)

        self.file_entry = ctk.CTkEntry(self.main_frame, placeholder_text="Selectione image dun fruit a reconaitre", width=400)
        self.file_entry.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="ew")

        self.browse_button = ctk.CTkButton(self.main_frame, text="Browse", command=self.select_file)
        self.browse_button.grid(row=0, column=1, padx=(0, 20), pady=(20, 0))

        self.recognize_button = ctk.CTkButton(self.main_frame, text="Reconaitre", command=self.recognize_fruit)
        self.recognize_button.grid(row=1, column=0, columnspan=2, padx=20, pady=(20, 0))

        self.image_label = ctk.CTkLabel(self.main_frame, text="")
        self.image_label.grid(row=2, column=0, columnspan=2, padx=20, pady=(20, 0))

        self.result_label = ctk.CTkLabel(self.main_frame, text="", font=ctk.CTkFont(size=16, weight="bold"))
        self.result_label.grid(row=3, column=0, columnspan=2, padx=20, pady=(20, 0))

        # New label for prediction
        self.prediction_label = ctk.CTkLabel(self.main_frame, text="", font=ctk.CTkFont(size=14))
        self.prediction_label.grid(row=4, column=0, columnspan=2, padx=20, pady=(10, 0))

        self.metrics_frame = ctk.CTkFrame(self.main_frame)
        self.metrics_frame.grid(row=5, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        # New label for model metrics
        self.model_metrics_label = ctk.CTkLabel(self.main_frame, text="", font=ctk.CTkFont(size=12))
        self.model_metrics_label.grid(row=6, column=0, columnspan=2, padx=20, pady=(10, 0))

        self.model = joblib.load(os.path.join(models_dir, 'svm_model2.pkl'))
        self.class_names = ['ananas', 'avocat','bananes', 'mangues',  'pasteques']

        # Display initial model metrics
        self.display_model_metrics()

    def select_file(self):
        file_path = ctk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
            self.display_image(file_path)

    def display_image(self, file_path):
        img = Image.open(file_path)
        img = img.resize((200, 200), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def recognize_fruit(self):
        file_path = self.file_entry.get()
        if file_path:
            image = Image.open(file_path)
            image_sans_bg = remove(image)
            image_name = file_path.split("/")[len(file_path.split("/")) - 1]
            image_sans_bg.save(f"{image_name}.png")
            img_array = load_and_preprocess_image(f"{image_name}.png")
            features = modelnn.predict(img_array)

            l = [features.flatten()]
            predictions = self.model.predict_proba(l)
            predicted_class = np.argmax(predictions[0])
            confidence = predictions[0][predicted_class]

            result = f"Predicted fruit: {self.class_names[predicted_class]}\nConfidence: {confidence:.2f}"
            self.result_label.configure(text=result)

            # Update prediction label
            prediction_text = f"Prediction: Le fruit sur limage est probablement un {self.class_names[predicted_class]}."
            self.prediction_label.configure(text=prediction_text)

            self.display_metrics(predictions[0])

    def display_metrics(self, predictions):
        for widget in self.metrics_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(self.class_names, predictions)
        ax.set_ylabel('Probability')
        ax.set_title('Probabilities de reconaisanse du fruit')
        plt.xticks(rotation=45, ha='right')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image = Image.open(buffer)
        image = image.resize((500, 225), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        metrics_label = ctk.CTkLabel(self.metrics_frame, image=photo, text="")
        metrics_label.image = photo
        metrics_label.pack(padx=(2,10), pady=10,)

    def display_model_metrics(self):
        # Here you would typically load or calculate your model's metrics
        # For this example, we'll use placeholder metrics
        accuracy = 98.66666666666667
        f1_score = 0.94
        precision = 0.93
        recall = 0.92

        metrics_text = f"Model Metrics:\nAccuracy: {accuracy:.2f}\n"
        self.model_metrics_label.configure(text=metrics_text)

    def sidebar_button_event(self):
        print("Sidebar button clicked")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = FruitRecognitionApp()
    app.mainloop()