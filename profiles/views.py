from django.contrib.auth.models import User
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect

from feed.models import Post
from followers.models import Follower
from .models import Profile
from .forms import CustomUserChangeForm, ProfileForm, PasswordChangeForm


class ProfileDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        user = self.get_object()
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(author=user).count()
        # context['total_followers'] = ...
        if self.request.user.is_authenticated:
            context['you_follow'] = Follower.objects.filter(following=user, followed_by=self.request.user).exists()
        return context


class FollowView(LoginRequiredMixin, View):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        if "action" not in data or "username" not in data:
            return HttpResponseBadRequest("Missing data")

        try:
            other_user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return HttpResponseBadRequest("Missing user")

        if data['action'] == "follow":
            # Follow
            follower, created = Follower.objects.get_or_create(
                followed_by=request.user,
                following=other_user
            )
        else:
            # Unfollow
            try:
                follower = Follower.objects.get(
                    followed_by=request.user,
                    following=other_user,
                )
            except Follower.DoesNotExist:
                follower = None

            if follower:
                follower.delete()

        return JsonResponse({
            'success': True,
            'wording': "Unfollow" if data['action'] == "follow" else "Follow"
        })


@login_required
def account_settings(request):
    user_form = CustomUserChangeForm(request.POST or None, instance=request.user)
    profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    password_form = PasswordChangeForm(request.user, request.POST or None)

    if request.method == "POST":
        if "update_user" in request.POST and user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profiles:account_settings")
        elif "change_password" in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            return redirect("profiles:account_settings")

    return render(request, "profiles/account_settings.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "password_form": password_form,
    })
