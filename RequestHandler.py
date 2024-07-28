from queue import PriorityQueue
from concurrent.futures import ThreadPoolExecutor

from CallbackHandler import CallbackHandler
from Camera import Camera
from CaptureRequest import CaptureRequest


class RequestHandler:
    def __init__(self, camera: 'Camera', callback_handler: 'CallbackHandler'):
        self.request_queue = PriorityQueue()
        self.executor = ThreadPoolExecutor(max_workers=10)  # Can be adjusted based on system capabilities
        self.camera = camera
        self.callback_handler = callback_handler

    def add_request(self, request: 'CaptureRequest'):
        self.request_queue.put(request)
        self.process_requests()

    def process_requests(self):
        while not self.request_queue.empty():
            request = self.request_queue.get()
            self.executor.submit(self.handle_request, request)

    def handle_request(self, request: 'CaptureRequest'):
        self.camera.capture_image(request, self.handle_result)

    def handle_result(self, request: 'CaptureRequest', success: bool, result: str):
        if success:
            self.callback_handler.invoke_success(request, result)
        else:
            self.callback_handler.invoke_failure(request, result)
