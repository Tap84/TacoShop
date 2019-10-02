from django.shortcuts import render,HttpResponse,get_object_or_404
from .forms import TacoForm
from .models import Taco
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import SHELL_CHOICES,BASE_LAYER_CHOICES,MIXINS_CHOICES,CONDIMENTS_CHOICES,SEASONINGS_CHOICES
import random
# Create your views here.

def tacoCreation(request):
    
    if request.method == "POST":
        #Check if the request was delete
        delete_check = request.POST.get('delete', None)
        #Check if the request was random
        random_check = request.POST.get('random', None)
        
        if delete_check:
            Taco.objects.filter(id=delete_check).first().delete()
        if random_check:
            #Fill random fields of the random taco
            fantastaco = Taco()
            fantastaco.shell_choice=random.choice(SHELL_CHOICES)[0]
            fantastaco.base_layer_choice=random.choice(BASE_LAYER_CHOICES)[0]
            fantastaco.mixin_choice=random.choice(MIXINS_CHOICES)[0]
            fantastaco.condiment_choice=random.choice(CONDIMENTS_CHOICES)[0]
            fantastaco.seasoning_choice=random.choice(SEASONINGS_CHOICES)[0]
            #save random taco as object in db
            fantastaco.save()   
        else:
            form = TacoForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
    form = TacoForm()
    template_name = "tacocreate/home.html"
    tacos = list(Taco.objects.all())
    context = {
        "form":form,
        "list":tacos
    }
    return render(request, template_name, context)

