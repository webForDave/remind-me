from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Capsule

def index(request): 
    return render(request, "capsules/index.html")

@login_required
def create_capsule(request):
    if request.method == "POST":
        title = request.POST.get("capsule_title")
        content = request.POST.get("capsule_content")
        current_user = request.user
        recipient = request.POST.get("recipient")
        delivery_date = request.POST.get("delivery_date")

        try:
            Capsule.objects.create(
                capsule_title = title,
                capsule_content = content,
                sender = current_user,
                recipient = recipient,
                delivery_date = delivery_date,
            )
            return redirect("/capsule/")
        except Exception as e:
            print(f"Error creating capsule: {e}")
            return HttpResponse(f"Error: Could not create capsule: {e}")
    else:
        return render(request, "capsules/create.html")
    
