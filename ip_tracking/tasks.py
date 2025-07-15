from django.utils.timezone import now, timedelta
from celery import shared_task

from .models import RequestLog, SuspiciousIP

SENSITIVE_PATHS = ["/admin", "/login"]
THRESHOLD = 100


@shared_task
def detect_suspicious_ips():
    one_hour_ago = now() - timedelta(hours=1)
    logs = RequestLog.objects.filter(timestamp__gte=one_hour_ago)

    ip_activity = {}

    for log in logs:
        ip = log.ip_address
        ip_activity.setdefault(ip, {"count": 0, "flagged": False})
        ip_activity[ip]["count"] += 1

        if log.path in SENSITIVE_PATHS:
            SuspiciousIP.objects.get_or_create(
                ip_address=ip,
                defaults={"reason": f"Accessed sensitive path: {log.path}"},
            )
            ip_activity[ip]["flagged"] = True

    for ip, data in ip_activity.items():
        if data["count"] > THRESHOLD and not data["flagged"]:
            SuspiciousIP.objects.get_or_create(
                ip_address=ip,
                defaults={"reason": f"Exceeded {THRESHOLD} requests in one hour"},
            )
