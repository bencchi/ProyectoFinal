from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def inicio(request):
    return render(request, "index.html")


def portfolio(request):
    return render(request, "portfolio-details.html")


def service(request):
    return render(request, "service-details.html")


def starter(request):
    return render(request, "starter-page.html")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def panel_administracion(request):
    return render(request, "panel_admin.html")
