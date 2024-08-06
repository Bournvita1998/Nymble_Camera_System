from CaptureRequest import CaptureRequest
from RequestHandler import RequestHandler
import time

class CameraSystem:
    def __init__(self, camera: 'Camera', callback_handler: 'CallbackHandler'):
        self.request_handler = RequestHandler(camera, callback_handler)

    def submit_capture_request(self, request: 'CaptureRequest'):
        self.request_handler.add_request(request)

    def shutdown(self, timeout: int = 30):
        # Gracefully shut down the ThreadPoolExecutor to wait for all tasks to complete
        self.request_handler.executor.shutdown(wait=True)

        # Wait until the request queue is empty and all active requests are completed
        start_time = time.time()
        while (not self.request_handler.request_queue.empty() or
               self.request_handler.active_requests) and (time.time() - start_time < timeout):
            time.sleep(0.1)  # Sleep briefly to avoid busy-waiting

        # Log or handle the case where not all requests were processed
        if not self.request_handler.request_queue.empty() or self.request_handler.active_requests:
            print("Warning: Not all requests were processed before shutdown.")
