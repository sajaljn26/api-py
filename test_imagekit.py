from imagekitio import ImageKit

# Test initialization
try:
    imagekit = ImageKit(
        private_key="test",
        public_key="test",
        url_endpoint="test"
    )
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
