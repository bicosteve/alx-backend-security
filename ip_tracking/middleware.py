from django.utils.timezone import now
from django.http import HttpResponseForbidden

from .models import RequestLog, BlockedIP


class IPLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")

        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Access denied!")

        path = request.path
        timestamp = now()

        RequestLog.objects.create(ip_address=ip, timestamp=timestamp, path=path)

        return self.get_response(request)
