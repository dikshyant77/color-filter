import cv2

def cartoon_filter(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,7)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(frame, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def pencil_sketch(frame):
    gray, sketch = cv2.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    return sketch

def watercolor_filter(frame):
    return cv2.stylization(frame, sigma_s =60, sigma_r= 0.6)

cap = cv2.VideoCapture(0)
filter_type = "original"

print("Press key to apply filters")
print("c - Cartoon")
print("p - Pencil Sketch")
print("w - WaterColor")
print("o - Original")
print("s - Save snapshot")
print("q - Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if filter_type == "c":
        output = cartoon_filter(frame)
        label = "Cartoon"
    elif filter_type == "p":
        output = pencil_sketch(frame)
        label = "Pencil Sketch"
    elif filter_type == "w":
        output = watercolor_filter(frame)
        label = "watercolor"
    else:
        output = frame
        label = "Original"

    cv2.putText(output, f"Filter: {label}", (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)
    cv2.imshow("Artistic Filters Demo", output)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("c"):
        filter_type = "c"
    elif key == ord("p"):
        filter_type = "p"
    elif key == ord("w"):
        filter_type = "w"
    elif key == ord("o"):
        filter_type = "original"
    elif key == ord("s"):
        cv2.imwrite("snapshot.png", output)
        print("Snapshot saved as snapshot.png")
    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()