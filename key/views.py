from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404  # Import Http404
from .models import AccessKey

def home(request):
    return render(request, 'home.html')

@login_required
def key_list(request):
    keys = AccessKey.objects.filter(user=request.user)
    return render(request, 'key_list.html', {'keys': keys})

@login_required
def admin_key_list(request):
    if not request.user.is_superuser:
        return redirect('home')
    keys = AccessKey.objects.all()
    return render(request, 'admin_key_list.html', {'keys': keys})

@login_required
def revoke_key(request, key_id):
    if not request.user.is_superuser:
        return redirect('home')
    key = get_object_or_404(AccessKey, pk=key_id)
    key.delete()
    return redirect('admin_key_list')

def key_status(request, email):
    keys = AccessKey.objects.filter(user__email=email)
    if not keys.exists():
        raise Http404('No active key found')
    status = 'active' if keys.exists() else 'inactive'
    return JsonResponse({'status': status})
