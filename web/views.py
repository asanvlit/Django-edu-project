from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, Max, Min, Q
from django.db.models.functions import TruncDate
from django.shortcuts import render, redirect, get_object_or_404

from web.forms import RegistrationForm, AuthForm, PostForm, PostTagForm, PostFilterForm
from web.models import Post, PostTag

User = get_user_model()


@login_required
def main_view(request):
    posts = Post.objects.filter(user=request.user).order_by('-created_at')

    filter_form = PostFilterForm(request.GET)
    filter_form.is_valid()
    filters = filter_form.cleaned_data

    if filters['search']:
        posts = posts.filter(art_type__icontains=filters['search'])

    if filters['hours_spent'] is not None:
        if filters['hours_spent']:
            posts = posts.filter(hours_spent__lt=25)
        elif not filters['hours_spent']:
            posts = posts.filter(hours_spent__gt=24)

    if filters['published_at_after']:
        posts = posts.filter(created_at__gte=filters['published_at_after'])

    if filters['published_at_before']:
        posts = posts.filter(created_at__lte=filters['published_at_before'])

    total_count = posts.count()
    posts = posts.prefetch_related("tags").select_related("user").annotate(
        tags_count=Count("tags")
    )
    page_number = request.GET.get("page", 1)
    paginator = Paginator(posts, per_page=10)

    return render(request, "web/main.html", {
        'posts': paginator.get_page(page_number),
        'form': PostForm(),
        'filter_form': filter_form,
        'total_count': total_count
    })


@login_required
def analytics_view(request):
    overall_stat = Post.objects.aggregate(
        count=Count("id"),
        max_date=Max("created_at"),
        min_date=Min("created_at")
    )
    days_stat = (
        Post.objects.exclude(hours_spent__isnull=True)
        .annotate(date=TruncDate("created_at"))
        .values("date")
        .annotate(
            count=Count("id"),
            more_one_day_spent_count=Count("id", filter=Q(hours_spent__gt=24)),
        )
        .order_by('-date')
    )

    return render(request, "web/analytics.html", {
        "overall_stat": overall_stat,
        'days_stat': days_stat
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


@login_required
def post_edit_view(request, id=None):
    post = get_object_or_404(Post, user=request.user, id=id) if id is not None else None
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES, instance=post, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, "web/post_form.html", {"form": form})


@login_required
def post_delete_view(request, id):
    post = get_object_or_404(Post, user=request.user, id=id)
    post.delete()
    return redirect('main')


@login_required
def tags_view(request):
    tags = PostTag.objects.filter(user=request.user)
    form = PostTagForm()
    if request.method == 'POST':
        form = PostTagForm(data=request.POST, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect('tags')
    return render(request, "web/tags.html", {"tags": tags, "form": form})


@login_required
def tags_delete_view(request, id):
    tag = get_object_or_404(PostTag, user=request.user, id=id)
    tag.delete()
    return redirect('tags')
