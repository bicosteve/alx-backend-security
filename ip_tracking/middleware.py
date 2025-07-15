from django.utils.timezone import now

from .models import RequestLog


class IPLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")
        path = request.path
        timestamp = now()

        RequestLog.objects.create(ip_address=ip, timestamp=timestamp, path=path)

        return self.get_response(request)
