import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('Screenshot (13).png')  

# Resize
resized = cv2.resize(image, (300, 300))

# Apply Gaussian blur
blurred = cv2.GaussianBlur(resized, (5, 5), 0)

# Convert to grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)


# Edge detection
edges = cv2.Canny(blurred, 50, 150)

# Show results using matplotlib
titles = ['Original', 'Grayscale', 'Blurred', 'Edges']
images = [cv2.cvtColor(resized, cv2.COLOR_BGR2RGB), gray, blurred, edges]

plt.figure(figsize=(10, 6))
for i in range(4):
    plt.subplot(2, 2, i + 1)
    cmap = 'gray' if len(images[i].shape) == 2 else None
    plt.imshow(images[i],cmap=cmap)
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()
