from CallbackHandler import CallbackHandler
from Camera import Camera
from CameraSystem import CameraSystem
from CaptureRequest import CaptureRequest
from RequestHandler import RequestHandler

def main():
    # Success and failure callbacks
    def success_callback(image_data):
        print(f"Capture success: {image_data}")

    def failure_callback(error_message):
        print(f"Capture failed: {error_message}")

    # Initialize components
    camera = Camera()
    callback_handler = CallbackHandler()
    request_handler = RequestHandler(camera, callback_handler)
    camera_system = CameraSystem(request_handler)

    # Create capture requests with different urgencies
    high_urgency_request = CaptureRequest(urgency=10, success_callback=success_callback,
                                          failure_callback=failure_callback)
    low_urgency_request = CaptureRequest(urgency=1, success_callback=success_callback,
                                         failure_callback=failure_callback)

    # Submit capture requests
    camera_system.submit_capture_request(high_urgency_request)
    camera_system.submit_capture_request(low_urgency_request)


if __name__ == "__main__":
    main()
