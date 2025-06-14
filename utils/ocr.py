import base64 
from PIL import Image 
from io import BytesIO 
import pytesseract 
 
def extract_text_from_base64(base64_string): 
    image_data = base64.b64decode(base64_string) 
    image = Image.open(BytesIO(image_data)) 
    return pytesseract.image_to_string(image) 
