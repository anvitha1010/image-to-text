import pytesseract
from PIL import Image
from tkinter import Tk, filedialog

# Function to select image from gallery
def select_image():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()  # Open file dialog to select image
    root.destroy()  # Destroy the root window
    return file_path

# Load the image
image_path = select_image()
if image_path:
    image = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    extracted_text = pytesseract.image_to_string(image)

    # Print the extracted text
    print(extracted_text)
