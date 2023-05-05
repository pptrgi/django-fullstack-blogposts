from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout

from . forms import RegisterForm


def register_account(request):
	if request.method == 'POST':
		form = RegisterForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('users:login'))
	else:
		form = RegisterForm()
	context = {'form': form}
	return render(request, 'users/register.html', context)


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('blogs:index'))