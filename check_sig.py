import inspect
from imagekitio import ImageKit

sig = inspect.signature(ImageKit.__init__)
print("ImageKit.__init__ signature:")
print(sig)
print("\nParameters:")
for param_name, param in sig.parameters.items():
    print(f"  {param_name}: {param.annotation}")
