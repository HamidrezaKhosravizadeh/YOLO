from ultralytics import YOLO
import cv2
import numpy as np

# مدل YOLO
model = YOLO("sorom.pt")

# دوربین
cap = cv2.VideoCapture(0)

# متغیر برای اختصاص ID به اشیاء
# object_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # پردازش تصویر با مدل
    results = model(frame)

    # شمارش تعداد اشیاء
    object_count = 0

    for r in results:
        if len(r) > 0:
            for box in r.boxes:
                object_count += 1  # افزایش تعداد اشیاء

                # مختصات مستطیل
                y1, y2, y3, y4 = map(int, box.xyxy[0].numpy())

                # نام شیء
                class_id = int(box.cls[0])
                class_name = model.names[class_id]

                # اختصاص ID به شیء
                # object_id += 1

                # رسم مستطیل دور شیء
                cv2.rectangle(frame, (y1, y2), (y3, y4), (255, 0, 0), 2)

                # نمایش نام شیء و ID
                label = f"{class_name}" #ID:{object_id}"
                cv2.putText(frame, label, (y1, y2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # نمایش تعداد اشیاء در تصویر
    cv2.putText(frame, f"Objects: {object_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # نمایش تصویر
    cv2.imshow('Webcam', frame)

    # خروج با فشردن کلید Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
