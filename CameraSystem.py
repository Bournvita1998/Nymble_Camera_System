from CaptureRequest import CaptureRequest
from RequestHandler import RequestHandler

class CameraSystem:
    def __init__(self, request_handler: 'RequestHandler'):
        self.request_handler = request_handler

    def submit_capture_request(self, request: 'CaptureRequest'):
        self.request_handler.add_request(request)
