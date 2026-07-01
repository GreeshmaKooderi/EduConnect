from django.shortcuts import render,redirect
from django.views import View

from .forms import RegisterForm
from .models import CustomUser

from django.contrib.auth.views import LoginView

class RegisterView(View):

    def get(self,request):

        form = RegisterForm()

        return render(
            request,
            'register.html',
            {'form':form}
        )

    def post(self,request):

        form = RegisterForm(request.POST)

        if form.is_valid():

            user=form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            return redirect('login')

        return render(
            request,
            'register.html',
            {'form':form}
        )
        
        
class UserLoginView(LoginView):

    template_name='login.html'
    
    from django.shortcuts import redirect

    def dashboard_redirect(request):

        if request.user.user_type == 'teacher':
            return redirect('teacher-dashboard')

        elif request.user.user_type == 'student':
            return redirect('student-dashboard')

        else:
            return redirect('parent-dashboard')