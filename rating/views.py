from django.shortcuts import render, get_object_or_404,redirect
from item.models import Item
from django.contrib.auth.decorators import login_required
from .models import Rating
from django.http import JsonResponse
from.forms import RatingMessageForm
from django.db.models import Avg




# Create your views here.
@login_required
def index(request, pk):
    #obj = Rating.objects.filter(pk=pk).order_by("?").first()
    obj=Rating.objects.filter(members__in=[pk,request.user.id]).order_by("?").first()
    if request.method  == 'POST':
        form = RatingMessageForm(request.POST, request.FILES, instance=obj)
        
        if form.is_valid():
            form.save()
            
            return redirect('rating:index',pk=pk)
    else:
        form = RatingMessageForm(instance=obj)
        
    context ={
            'object': obj,
            'pk': pk,
            'form': form,
    }  
    return render(request, 'rating/index.html', context)

@login_required
def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        print(val)
        obj = Rating.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})

