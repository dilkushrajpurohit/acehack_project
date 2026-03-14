# vision_ai/train_vip_model.py

from ultralytics import YOLO

# Load YOLOv8 pretrained model (nano for speed)
model = YOLO("yolov8n.pt")

# Train on your custom VIP beacon dataset
# Dataset folder must have 'images/train', 'images/val', 'labels/train', 'labels/val'
# Create 'data.yaml' with your classes and paths
"""
data.yaml example:

train: ./data/images/train
val: ./data/images/val

nc: 2
names: ['normal_car', 'vip_beacon']
"""

model.train(
    data="data.yaml",
    epochs=30,           # hackathon-friendly quick training
    imgsz=640,
    batch=8,
    name="vip_beacon_detector"
)

# After training, the weights are saved in 'runs/train/vip_beacon_detector/weights/best.pt'