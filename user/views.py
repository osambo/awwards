from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})
@login_required
def profile(request):
    if request.method == 'POST':
        form_user = UserUpdateForm(request.POST, instance=request.user)
        form_profile = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if form_user.is_valid() and form_profile.is_valid():
            form_user.save()
            form_profile.save()

            messages.success(request, f'Your account has been updated successfully!')
            return redirect('profile')
    else:
        form_user = UserUpdateForm(instance=request.user)
        # import pdb;pdb.set_trace()
        form_profile = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'form_user': form_user,
        'form_profile': form_profile
    }
    return render(request, 'user/profile.html', context)
