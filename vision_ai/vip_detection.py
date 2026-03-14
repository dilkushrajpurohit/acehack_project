# vision_ai/vip_detection.py

from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO("runs/train/vip_beacon_detector/weights/best.pt")

def detect_vip(frame):
    results = model(frame)

    vip_detected = False
    normal_car_count = 0

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            if label == "vip_beacon":
                vip_detected = True
            elif label == "normal_car":
                normal_car_count += 1

    return {
        "vip_detected": vip_detected,
        "normal_car_count": normal_car_count
    }