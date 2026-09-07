from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        request.session['username'] = request.POST.get('username')
        return redirect('accounts:login')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        saved_username = request.session.get('username')

        if not saved_username:
            return render(request, 'login.html', {
                'error': 'Your account does not exist; please create an account first.'
            })

        if saved_username != username:
            return render(request, 'login.html', {
                'error': 'Incorrect username; please try again'
            })

        return redirect('accounts:profile')


class ProfileView(View):
    def get(self, request):

        username = request.session.get('username', 'Guest')
        return render(request, 'profile.html', {'username': username})


def status_view(request):
    data = {
        "status": "Success",
        "message": "The accounts app is running smoothly!",
        "code": 200
    }
    return JsonResponse(data)


class LogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('accounts:profile')
