from ultralytics import YOLO
import cv2
model = YOLO("best.pt")   #path of the trained model
results = model.predict(source="0", show=True)
print(results)