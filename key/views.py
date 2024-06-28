# access_management/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import AccessKey
from .serializer import AccessKeySerializer

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def key_list(request):
    keys = AccessKey.objects.filter(user=request.user)
    return render(request, 'access_management/key_list.html', {'keys': keys})

@staff_member_required
def admin_key_list(request):
    keys = AccessKey.objects.all()
    return render(request, 'access_management/admin_key_list.html', {'keys': keys})

@staff_member_required
def revoke_key(request, key_id):
    key = AccessKey.objects.get(id=key_id)
    key.status = 'revoked'
    key.save()
    return redirect('admin_key_list')

@api_view(['GET'])
def key_status(request, email):
    try:
        key = AccessKey.objects.filter(user__email=email, status='active').latest('date_of_procurement')
        serializer = AccessKeySerializer(key)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except AccessKey.DoesNotExist:
        return Response({'error': 'No active key found'}, status=status.HTTP_404_NOT_FOUND)
