import cv2

# قراءة الصورة
img = cv2.imread("color.jpg")

# التأكد من أن الصورة تم تحميلها
if img is None:
    print("Error: Could not read the image.")
    exit()

# تحويل الصورة من BGR إلى HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# تحديد نطاق اللون الأخضر
lower_green = (35, 50, 50)
upper_green = (85, 255, 255)

# إنشاء قناع للون الأخضر
mask = cv2.inRange(hsv, lower_green, upper_green)

# عرض الصورة الأصلية والقناع
cv2.imshow("Original Image", img)
cv2.imshow("Green Color", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()