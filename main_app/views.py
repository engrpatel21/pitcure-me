from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile

# Create your views here.
def home(request):
    return render(request, 'home.html')

def profile(request):
    profile = Profile.objects.get(user=request.user)
    print(request.user)
    return render(request, 'profile/profile.html', {'profile': profile})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      p = Profile(user = user)
      p.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class ProfileUpdate( UpdateView):
    model = Profile
    fields = ['bio', 'pic']
    success_url = '/profile/'

class ProfileCreate(CreateView):
    model = Profile
    fields = '__all__'
    success_url='/profile/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)