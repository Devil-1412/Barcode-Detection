import cv2
from ultralytics import YOLOv10

model = YOLOv10(r"C:\Users\hp\Documents\Computer Vision\best.pt")


# Initialize video capture (0 for the first webcam device)
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")
while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Perform inference
    results = model(source=frame, conf=0.25)
    
    # Process the results
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = box.cls[0]
            label = f"{model.names[int(cls)]}: {conf:.2f}"
            color = (0, 255, 0)
            
            # Draw rectangle and put tqext
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    # Display the frame
    cv2.imshow('Real-Time Detection', frame)

    # Break the loop with 'q' key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
