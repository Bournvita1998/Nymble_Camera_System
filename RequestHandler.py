from queue import PriorityQueue
from concurrent.futures import ThreadPoolExecutor
from CallbackHandler import CallbackHandler
from Camera import Camera
from CaptureRequest import CaptureRequest
import threading


class RequestHandler:
    def __init__(self, camera: 'Camera', callback_handler: 'CallbackHandler'):
        self.request_queue = PriorityQueue()
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.camera = camera
        self.callback_handler = callback_handler
        self.lock = threading.Lock()
        self.active_requests = set()  # Track active requests to avoid duplicate processing

    def add_request(self, request: 'CaptureRequest'):
        with self.lock:
            self.request_queue.put(request)
            # Only add and process new requests if they aren't already active
            if request.request_id not in self.active_requests:
                self.active_requests.add(request.request_id)
                self.executor.submit(self.process_next_request)

    def process_next_request(self):
        while True:
            with self.lock:
                if not self.request_queue.empty():
                    request = self.request_queue.get()
                else:
                    return  # Exit if no more requests

            self.handle_request(request)

    def handle_request(self, request: 'CaptureRequest'):
        self.camera.capture_image(request, self.handle_result)

    def handle_result(self, request: 'CaptureRequest', success: bool, result: str):
        if success:
            self.callback_handler.invoke_success(request, result)
        else:
            self.callback_handler.invoke_failure(request, result)

        with self.lock:
            self.active_requests.remove(request.request_id)
        self.process_next_request()  # Check if there are more requests to process
