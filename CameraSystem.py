from CaptureRequest import CaptureRequest
from RequestHandler import RequestHandler

class CameraSystem:
    def __init__(self, camera: 'Camera', callback_handler: 'CallbackHandler'):
        self.request_handler = RequestHandler(camera, callback_handler)

    def submit_capture_request(self, request: 'CaptureRequest'):
        self.request_handler.add_request(request)

    def shutdown(self):
        # Gracefully shut down the ThreadPoolExecutor to wait for all tasks to complete
        self.request_handler.executor.shutdown(wait=True)
