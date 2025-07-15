# alx-backend-security

```bash
0. Task 0: Basic IP Logging Middleware

Objective:
    Implement middleware to log the IP address, timestamp, and path of every incoming request.

Instructions
    Create ip_tracking/middleware.py with a middleware class that logs request details.
    Defineip_tracking/models.py with a RequestLog model (fields: ip_address,timestamp, path).
    Register the middleware in settings.py.
Repo:
    GitHub repository: alx-backend-security
    File: ip_tracking/middleware.py, ip_tracking/models.py
```

```bash
1. Task 1: IP Blacklisting

Objective:
    Implement IP blocking based on a blacklist.

Instructions
    Create ip_tracking/models.py with a BlockedIP model (field: ip_address).
    Modify ip_tracking/middleware.py to block requests from IPs in BlockedIP. Return 403 Forbidden.
    Create ip_tracking/management/commands/block_ip.pyto add IPs toBlockedIP.

Repo:
    GitHub repository: alx-backend-security
    File: ip_tracking/middleware.py, ip_tracking/management/commands/block_ip.py
```

```bash
2. Task 2: IP Geolocation Analytics

Objective:
    Enhance logging with geolocation data (country, city).

Instructions
    Install django-ipgeolocation.
    Extend RequestLog in ip_tracking/models.py with country and city fields.
    Update ip_tracking/middleware.py to populate these fields using the geolocation API. Cache results for24 hours.
Repo:
    GitHub repository: alx-backend-security
    File: ip_tracking/models.py, ip_tracking/middleware.py
```

```bash
3. Task 3: Rate Limiting by IP

Objective:
    Implement rate limiting to prevent abuse.

Instructions
    Install django-ratelimit.
    Configure rate limits: 10 requests/minute (authenticated), 5 requests/minute (anonymous).
    Apply the rate limit to a sensitive view (e.g., login) in ip_tracking/views.py. Configure in settings.py.
Repo:
    GitHub repository: alx-backend-security
    Directory: ip_tracking
    File: ip_tracking/views.py, settings.py
```

```bash
4. Task 4: Anomaly Detection

Objective:
    Implement anomaly detection to flag suspicious IPs.

Instructions
    Create a Celery task inip_tracking/tasks.py to run hourly.
    The task should flag IPs exceeding 100 requests/hour or accessing sensitive paths (e.g., /admin, /login).
    Createip_tracking/models.pywith a SuspiciousIP model (fields: ip_address, reason).

Repo:
    GitHub repository: alx-backend-security
    Directory: ip_tracking
    File: ip_tracking/tasks.py, ip_tracking/models.py
```
