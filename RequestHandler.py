from queue import PriorityQueue
from concurrent.futures import ThreadPoolExecutor
from CallbackHandler import CallbackHandler
from Camera import Camera
from CaptureRequest import CaptureRequest
import threading

class RequestHandler:
    def __init__(self, camera: 'Camera', callback_handler: 'CallbackHandler'):
        self.request_queue = PriorityQueue()
        self.executor = ThreadPoolExecutor(max_workers=2)  # Allow multiple concurrent workers
        self.camera = camera
        self.callback_handler = callback_handler
        self.lock = threading.Lock()  # To ensure thread safety

    def add_request(self, request: 'CaptureRequest'):
        with self.lock:
            self.request_queue.put(request)
        self.process_requests()

    def process_requests(self):
        while not self.request_queue.empty():
            with self.lock:
                request = self.request_queue.get()
            # Process request in a thread
            self.executor.submit(self.handle_request, request)

    def handle_request(self, request: 'CaptureRequest'):
        self.camera.capture_image(request, self.handle_result)

    def handle_result(self, request: 'CaptureRequest', success: bool, result: str):
        if success:
            self.callback_handler.invoke_success(request, result)
        else:
            self.callback_handler.invoke_failure(request, result)
