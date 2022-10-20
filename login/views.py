from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate

# Create your views here.

def inicioSesion(request):

    if request.POST == {}:
        return render(request, "login_form.html")
    else:
        try:

            username=request.POST["user"]
            password=request.POST["pass"]

            user = authenticate(username = username, password = password)

            if user:

                login(request, user)

                return redirect("inicio") 

            else:
                return render(request, "login_form.html", {"resultado": "no fue posible iniciar sesión."})

        except:
            return render(request, "login_form.html", {"resultado": "no fue posible iniciar sesión."})