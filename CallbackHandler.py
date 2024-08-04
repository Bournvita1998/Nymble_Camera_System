from CaptureRequest import CaptureRequest
import threading

class CallbackHandler:
    def __init__(self):
        self.lock = threading.Lock()

    def invoke_success(self, request: 'CaptureRequest', result: str):
        with self.lock:
            request.success_callback(request.request_id, result)

    def invoke_failure(self, request: 'CaptureRequest', error_message: str):
        with self.lock:
            request.failure_callback(request.request_id, error_message)
