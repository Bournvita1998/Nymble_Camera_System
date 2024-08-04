from typing import Callable

class CaptureRequest:
    def __init__(self, request_id: int, urgency: int, success_callback: Callable, failure_callback: Callable):
        self.request_id = request_id  # Simple sequential request ID
        self.urgency = urgency
        self.success_callback = success_callback
        self.failure_callback = failure_callback

    def __lt__(self, other: 'CaptureRequest'):
        return self.urgency > other.urgency  # Higher urgency requests are prioritized
