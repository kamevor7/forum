from django.contrib import auth, messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from blog.form import BlogForm, ClimbingAreaForm
from blog.models import Blog, ClimbingAreas


def index(request):
    return render(request, 'blog/index.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],
                                 password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['conf_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'registration/signup.html',
                              {'error': 'Username Unavailable! '
                                        'Please Try a Different Username '
                                        'or Proceed to Log In!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],
                                                password=request.POST['password'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                email=request.POST['email'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'registration/signup.html',
                          {'error': 'Unmatched Password!'
                                    'Please Try Again'})
    else:
        return render(request, 'registration/signup.html')


def profile(request):
    return render(request, 'blog/profile.html')


class UserEditView(generic.UpdateView):
    model = User
    template_name = 'blog/edit_profile.html'
    fields = (
        'username',
        'first_name',
        'last_name',
        'email',
    )
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


@login_required()
def user_list(request):
    users = User.objects
    return render(request, 'blog/user_list.html', {'users': users})


@staff_member_required
def del_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return redirect('user_list')
    except User.DoesNotExist:
        return redirect('blog/user_list.html')


@staff_member_required
def upgrade_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.is_staff = True
        user.save()
        return redirect('user_list')
    except User.DoesNotExist:
        return redirect('blog/user_list.html')


@staff_member_required
def downgrade_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.is_staff = False
        user.save()
        return redirect('user_list')
    except User.DoesNotExist:
        return redirect('blog/user_list.html')


@staff_member_required
def suspend_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()
        return redirect('user_list')
    except User.DoesNotExist:
        return redirect('blog/user_list.html')


@staff_member_required
def activate_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return redirect('user_list')
    except User.DoesNotExist:
        return redirect('blog/user_list.html')

# Starting Blog


@login_required()
def blogs(request):
    post = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'post': post})


@login_required()
def detail(request, blogs_id):
    post_detail = get_object_or_404(Blog, pk=blogs_id)
    return render(request, 'blog/blog_detail.html', {'post_detail': post_detail})


def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.publication_date = timezone.now()
            post.save()
            return redirect('blog')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = BlogForm()
    return render(request, 'blog/add_post.html', {'form': form})


@login_required()
def post_edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.publication_date = timezone.now()
            post.save()
            return render(request, 'blog/blog_list.html', {'posts': post})
    else:
        form = BlogForm(instance=post)
        return render(request, 'blog/edit_post.html', {'form': form})


@login_required()
def post_delete(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('blog')


def climbing_areas(request):
    post = ClimbingAreas.objects.all()
    return render(request, 'blog/climbing_areas.html', {'post': post})


def add_climbing_area_post(request):
    if request.method == 'POST':
        form = ClimbingAreaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('climbing_areas')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ClimbingAreaForm()
        return render(request, 'blog/add_climbing_area_post.html', {'form': form})
