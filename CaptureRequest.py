from typing import Callable


class CaptureRequest:
    def __init__(self, urgency: int, success_callback: Callable, failure_callback: Callable):
        self.urgency = urgency
        self.success_callback = success_callback
        self.failure_callback = failure_callback

    def __lt__(self, other: 'CaptureRequest'):
        return self.urgency > other.urgency  # Higher urgency requests are prioritized
