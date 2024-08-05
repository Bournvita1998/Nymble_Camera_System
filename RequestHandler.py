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
        self.is_processing = False  # Flag to track if a request is being processed

    def add_request(self, request: 'CaptureRequest'):
        with self.lock:
            self.request_queue.put(request)
        self.process_next_request()

    def process_next_request(self):
        with self.lock:
            if not self.is_processing and not self.request_queue.empty():
                request = self.request_queue.get()  # Get the highest urgency request
                self.is_processing = True
                self.executor.submit(self.handle_request, request)

    def handle_request(self, request: 'CaptureRequest'):
        self.camera.capture_image(request, self.handle_result)

    def handle_result(self, request: 'CaptureRequest', success: bool, result: str):
        if success:
            self.callback_handler.invoke_success(request, result)
        else:
            self.callback_handler.invoke_failure(request, result)

        with self.lock:
            self.is_processing = False  # Reset the flag after processing
        self.process_next_request()  # Continue processing the next request in the queue
