from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Capsule

@login_required
def index(request): 
    current_user = request.user
    capsules = Capsule.objects.filter(sender=current_user)  
    return render(request, "capsules/index.html", {"capsules": capsules}) 

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
            return redirect("home")
        except Exception as e:
            print(f"Error creating capsule: {e}")
            return HttpResponse(f"Error: Could not create capsule: {e}")
    else:
        return render(request, "capsules/create.html")
    
@login_required
def capsule_detail(request, title):
    capsule = get_object_or_404(Capsule, sender=request.user, capsule_title=title)
    return render(request, "capsules/detail.html", {"capsule": capsule})

@login_required
def update_capsule(request, title):
    capsule = get_object_or_404(Capsule, sender=request.user, capsule_title=title)

    if request.method == "POST":
        capsule.capsule_title = request.POST.get("capsule_title")
        capsule.content = request.POST.get("capsule_content")
        capsule.recipient = request.POST.get("recipient")
        capsule.delivery_date = request.POST.get("delivery_date")

        try:
            capsule.save()
            return redirect("capsule_detail", title=capsule.capsule_title)
        except Exception as e:
            print(f"Error updating capsule {e}")
            return render(request, "capsules/update.html", {"capsule": capsule, "error": f"Cannot update capsule: {e}"})
    else: 
        return render(request, "capsules/update.html", {"capsule": capsule})