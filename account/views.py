from django.shortcuts import render, redirect
from django.views import View


from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



class UserCreateView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(
            request,
            'account/user_form.html',
            context={
                'form': form,
            }
        )

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect("account:user-create")