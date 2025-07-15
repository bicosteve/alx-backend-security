from django.shortcuts import render
from django_ratelimit.decorators import ratelimit
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@ratelimit(key="ip", rate="10/m", method="POST", block=True)
@login_required
def login_sensitive_view(request):
    return HttpResponse("Authentication access granted")


@ratelimit(key="ip", rate="5/m", method="POST", block=True)
def anonymous_sensitive_view(request):
    if request.user.is_authenticated:
        return HttpResponse("Already authenticated")
    return HttpResponse("Anonymous access granted.")
