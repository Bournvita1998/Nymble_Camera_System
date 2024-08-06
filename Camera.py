from CaptureRequest import CaptureRequest
import time, random

class Camera:
    def capture_image(self, request: 'CaptureRequest', callback):
        # Simulate capturing image with delay
        time.sleep(1)
        try:
            # Randomly determine success or failure
            success = random.choices([True, False], weights=[70, 30])[0]
            if success:
                result = "captured_image_data"
                callback(request, True, result)
            else:
                raise Exception("Capture failed due to random error")
        except Exception as e:
            callback(request, False, str(e))
