from django.shortcuts import render, get_object_or_404
from item.models import Item
from django.contrib.auth.decorators import login_required
from rating.models import Rating
from django.db.models import Avg

# Create your views here.

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    reviews= Rating.objects.filter(members__in=[request.user.id])[0:3]
    average = Rating.objects.filter(members__in=[request.user.id]).aggregate(Avg('score'))
    theuser = request.user
    return render(request, 'dashboard/index.html', {
        'items': items,
        'reviews': reviews,
        'average': average,
        'theuser': theuser,
    })


@login_required
def profile(request):
    return render(request, "dashboard/profile.html")  # Renders the profile page
