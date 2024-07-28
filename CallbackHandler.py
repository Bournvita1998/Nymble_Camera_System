from CaptureRequest import CaptureRequest


class CallbackHandler:
    @staticmethod
    def invoke_success(request: 'CaptureRequest', result: str):
        request.success_callback(result)

    @staticmethod
    def invoke_failure(request: 'CaptureRequest', error_message: str):
        request.failure_callback(error_message)
