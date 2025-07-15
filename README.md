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
