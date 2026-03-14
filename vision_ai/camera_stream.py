# vision_ai/camera_stream.py

import cv2
import requests
from vip_detection import detect_vip

# Open camera (0 = default webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect VIP / normal cars
    data = detect_vip(frame)

    # Draw info on frame
    cv2.putText(
        frame,
        f"VIP Detected: {data['vip_detected']} Normal Cars: {data['normal_car_count']}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255) if data['vip_detected'] else (0, 255, 0),
        2
    )

    cv2.imshow("VIP Detection AI", frame)

    # Send data to backend
    try:
        requests.post(
            "http://127.0.0.1:5000/traffic",
            json=data,
            timeout=0.1
        )
    except:
        pass  # ignore errors for demo

    if cv2.waitKey(1) == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()