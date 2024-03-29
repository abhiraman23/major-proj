from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
'''from django.db.models import Count'''
#from .models import UserAddModel  # Assuming your model is named UserAddModel''

def admin_login(request):
    if request.method == "POST":
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            name = data.get('name')
            password = data.get('password')
            if name == 'admin' and password == 'admin':
                return JsonResponse({"message": "Hello, world. You're at login index."})
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=400)
        else:
            name = request.POST.get('name')
            password = request.POST.get('password')
            if name == 'admin' and password == 'admin':
                return HttpResponse("Hello, world. You're at login index.")
    return render(request, 'admins/admin_login.html')

'''def achart_page(request, achart_type):
    chart = UserAddModel.objects.values('year').annotate(dcount=Count('organizationtype'))
    return render(request, 'admins/achart_page.html', {'chart_type': achart_type, 'objects': chart})

def admin_analysis(request):
    chart = UserAddModel.objects.values('attackresult', 'method').annotate(dcount=Count('attackresult'))
    return render(request, 'admins/admin_analysis.html', {'objects': chart})'''

def user_details(request):
    obj = UserAddModel.objects.all()
    return render(request, 'admins/user_details.html', {'objects': obj}) 
