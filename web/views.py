from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

from web.forms import RegistrationForm, AuthForm, PostForm
from web.models import Post

User = get_user_model()


def main_view(request):
    posts = Post.objects.all()
    return render(request, "web/main.html", {
        'posts': posts
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request, "web/registration.html", {
        "form": form, "is_success": is_success
    })


def auth_view(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Неверный логин или пароль")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/auth.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("main")


def post_edit_view(request, id=None):
    post = Post.objects.get(id=id) if id is not None else None
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(data=request.POST, instance=post, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, "web/post_form.html", {"form": form})
