
from PIL import Image, ImageDraw

# Get prompt from user
prompt = input("Enter image prompt: ")

# Create a blank image
image = Image.new("RGB", (800, 500), "white")
draw = ImageDraw.Draw(image)

# Draw a simple generated scene
draw.rectangle((0, 0, 800, 350), fill="skyblue")
draw.rectangle((0, 350, 800, 500), fill="green")
draw.ellipse((600, 50, 720, 170), fill="yellow")

# Add prompt text to image
draw.text((50, 220), "Generated Image", fill="black")
draw.text((50, 250), "Prompt: " + prompt, fill="black")

# Save image
image.save("generated_image.png")

print("Image generated successfully!")
print("Output: generated_image.png")