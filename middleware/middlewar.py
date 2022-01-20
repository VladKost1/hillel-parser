from datetime import datetime
from .models import Logger
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_time = None

    def process_request(self, request):
        if '/admin/' in request.path:
            self.start_time = datetime.now()

    def process_response(self, request, response):
        if '/admin/' in request.path:
            delta = datetime.now() - self.start_time
            Logger.objects.create(
                path=request.path,
                method=request.method,
                execution_time=delta
            )
        return response
