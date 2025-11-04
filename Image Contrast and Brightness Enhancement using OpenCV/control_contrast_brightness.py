import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_contrast_brightness(image, alpha, beta):
    """
    Adjusts contrast and brightness of the image.
    alpha: Contrast control (1.0–3.0)
    beta: Brightness control (0–100)
    """
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted

# Load image
path = 'Screenshot (10).png'
image = cv2.imread(path)
if image is None:
    print("Error loading image.")
    exit()

# Convert to RGB for displaying with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Try different contrast and brightness values
alpha = 3.0     # Contrast (1.0 to 3.0)
beta = 50       # Brightness (0 to 100)

adjusted = adjust_contrast_brightness(image_rgb, alpha, beta)

# Display using matplotlib
plt.imshow(adjusted)
plt.title(f'Contrast: {alpha}, Brightness: {beta}')
plt.axis('off')
plt.show()

# Save the image if you want
cv2.imwrite('adjusted_output.jpg', cv2.cvtColor(adjusted, cv2.COLOR_RGB2BGR))
print("Image saved as adjusted_output.jpg")
