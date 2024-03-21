from transformers import AutoImageProcessor, ViTForImageClassification
import torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification


# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-classification", model="RavenOnur/Sign-Language")

# Load model directly
from transformers import AutoImageProcessor, AutoModelForImageClassification

processor = AutoImageProcessor.from_pretrained("RavenOnur/Sign-Language")
model = AutoModelForImageClassification.from_pretrained("RavenOnur/Sign-Language")


# Path to your image in Google Drive
image_path = r'C:\Users\ragil\OneDrive\Escritorio\UNIVERSIDAD\tercer año\proyecto bigdata2\Git_Signlanguage\Sign-language\abecedario_es'


# Load image using PIL

for x in image_path:
    image = Image.open(image_path)

    inputs = processor(image, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

# model predicts one of the 1000 ImageNet classes
predicted_label = logits.argmax(-1).item()
print(model.config.id2label[predicted_label])