import base64
import io
from imageio import imread

def base64_to_image(b64_string):
    """Converting base64 string to cv2 image.

        Args:
            b64_string: Representing the base64 encoded image.
        
        Return:
            A cv2 image, that we decoded from the base64 string,
            stored in a numpy array.
    """
    # reconstruct image as a numpy array
    decoded_string = base64.b64decode(b64_string)
    img = imread(io.BytesIO(decoded_string))

    return img