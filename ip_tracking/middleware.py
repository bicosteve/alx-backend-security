from django.utils.timezone import now
from django.http import HttpResponseForbidden
from django.core.cache import cache
from django_ip_geolocation.decorators import with_ip_geolocation

from .models import RequestLog, BlockedIP


class IPLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @with_ip_geolocation
    def __call__(self, request):
        ip = request.META.get("REMOTE_ADDR")

        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Access denied!")

        path = request.path
        timestamp = now()
        geo = request.geo

        RequestLog.objects.create(
            ip_address=ip,
            timestamp=timestamp,
            path=path,
            country=geo.get("country_name", ""),
            city=geo.get("city", ""),
        )

        return self.get_response(request)
