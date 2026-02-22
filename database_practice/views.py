from django.shortcuts import render,redirect
from .models import registration

def func1(request):
    count = 0
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")


        registration.objects.create(
            name=name,
            phone=phone,
            email=email,
            username = username,
            password = password
        )
    return render(request, "form.html", {"count": count})

def login_view(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = registration.objects.get(username=username)
        if(user.password == password):

            request.session['user_id'] = user.id
            return redirect('dashboard')

        else:
            message = "Login Failed!!! Please check username and password!!!"

    return render(request, "view.html", {"message": message})

def dashboard(request):

    user_id = request.session.get('user_id')
    user = registration.objects.get(id=user_id)
    return render(request, "dashboard.html", {"user": user})

def update_user(request,id):

    count = 1
    user = registration.objects.get(id=id)
    if request.method == "POST":
        user.username = request.POST.get("username")
        user.name = request.POST.get("name")
        user.phone = request.POST.get("phone")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.save()
        request.session['user_id'] = id
        return redirect('dashboard')

    return render(request, "form.html", {"count": count, "user": user})

def delete_user(request,id):

    user = registration.objects.get(id=id)
    user.delete()
    return redirect('form')


