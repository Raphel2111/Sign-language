from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image
import os


processor = AutoImageProcessor.from_pretrained("RavenOnur/Sign-Language")
model = AutoModelForImageClassification.from_pretrained("RavenOnur/Sign-Language")


directory = '/content/Imagenes'

image_files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]


for image_file in image_files:

    image_path = os.path.join(directory, image_file)
    

    image = Image.open(image_path)
    
 
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_label = logits.argmax(-1).item()
    label = model.config.id2label[predicted_label]
    

    print(f"en la imagen {image_file}, la etiqueta es: {label}")

