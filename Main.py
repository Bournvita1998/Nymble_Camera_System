import time
from CallbackHandler import CallbackHandler
from Camera import Camera
from CameraSystem import CameraSystem
from CaptureRequest import CaptureRequest

def main():
    # Success and failure callbacks
    def success_callback(request_id, image_data):
        print(f"Request {request_id}: Capture success: {image_data}")

    def failure_callback(request_id, error_message):
        print(f"Request {request_id}: Capture failed: {error_message}")

    # Initialize components
    camera = Camera()
    callback_handler = CallbackHandler()
    camera_system = CameraSystem(camera, callback_handler)

    # Create capture requests with different urgencies
    high_urgency_request = CaptureRequest(request_id=1, urgency=10, success_callback=success_callback,
                                          failure_callback=failure_callback)
    low_urgency_request = CaptureRequest(request_id=2, urgency=1, success_callback=success_callback,
                                          failure_callback=failure_callback)
    new_high_urgency_request = CaptureRequest(request_id=3, urgency=100, success_callback=success_callback,
                                          failure_callback=failure_callback)

    # Submit capture requests
    camera_system.submit_capture_request(low_urgency_request)
    camera_system.submit_capture_request(high_urgency_request)
    camera_system.submit_capture_request(new_high_urgency_request)

    # Shutdown the camera system, waiting until all tasks are completed
    camera_system.shutdown()

if __name__ == "__main__":
    main()
