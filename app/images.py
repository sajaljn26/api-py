from dotenv import load_dotenv
from imagekitio import ImageKit
import os 

load_dotenv()

# Temporarily disabled ImageKit until we fix the configuration
# imagekit = ImageKit(
#     private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"),
#     public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
#     url_endpoint=os.getenv("IMAGEKIT_URL_ENDPOINT")
# )
imagekit = None  # Placeholder

