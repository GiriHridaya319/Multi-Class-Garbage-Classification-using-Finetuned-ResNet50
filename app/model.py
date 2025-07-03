import torch
import torchvision.transforms as transforms
from PIL import Image
import io
import os
from torchvision.models import resnet50

# Define the classes for garbage classification
# You should replace this with your actual classes
classes = [
    "white-glass",
    "trash",
    "shoes",
    "plastic",
    "paper",
    "metal",
    "green-glass",
    "clothes",
    "cardboard",
    "brown-glass",
    "biological",
    "battery"
]
# Define the same transforms you used for validation during training
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.1, contrast=0.1, saturation=0.1, hue=0.1),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

class GarbageClassifier:
    def __init__(self):
        # Determine the device
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")
        
        # Initialize the model
        self.model = resnet50(pretrained=False)
        # Modify the final fully connected layer for your number of classes
        num_classes = len(classes)
        self.model.fc = torch.nn.Linear(self.model.fc.in_features, num_classes)
        
        # Load the trained weights
        model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 
                                 "garbage_resnet50_final_model.pth")
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model = self.model.to(self.device)
        self.model.eval()
        print("Model loaded successfully!")
        
    def predict(self, image_bytes):
        # Convert bytes to image
        img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        
        # Preprocess the image
        img_tensor = data_transforms['val'](img).unsqueeze(0).to(self.device)
        
        # Make prediction
        with torch.no_grad():
            outputs = self.model(img_tensor)
            probs = torch.nn.functional.softmax(outputs, dim=1)[0]
            
            # Get top 3 predictions
            top_probs, top_classes = torch.topk(probs, 3)
            results = [(classes[i], p.item() * 100) for i, p in zip(top_classes, top_classes)]
            
            # Get the top prediction
            _, preds = torch.max(outputs, 1)
            predicted_class = classes[preds[0]]
            confidence = probs[preds[0]].item() * 100
            
            # Return top 3 predictions and the top one
            top_results = [(classes[i], p.item() * 100) for i, p in zip(top_classes, top_probs)]
            
            return {
                "class": predicted_class,
                "confidence": confidence,
                "top_three": top_results
            }