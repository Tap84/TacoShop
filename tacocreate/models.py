from django.db import models
from django.contrib.auth.models import User
from django import forms
from multiselectfield import MultiSelectField
import requests



def get_list_of_json_from_url(url, tag):
    item_json = requests.get(url).json()
    item_list = []
    for item in item_json:
        item_list.append(item[tag])
    return item_list

shells_list = get_list_of_json_from_url("https://ct-tacoapi.azurewebsites.net/shells", "name")
base_layer_list = get_list_of_json_from_url("https://ct-tacoapi.azurewebsites.net/baseLayers", "name")
mixins_list = get_list_of_json_from_url("https://ct-tacoapi.azurewebsites.net/mixins", "name")
condiments_list = get_list_of_json_from_url("https://ct-tacoapi.azurewebsites.net/condiments", "name")
seasonings_list = get_list_of_json_from_url("https://ct-tacoapi.azurewebsites.net/seasonings", "name")
SHELL_CHOICES = tuple((x,x)for x in shells_list)
BASE_LAYER_CHOICES = tuple((x,x)for x in base_layer_list)
MIXINS_CHOICES = tuple((x,x)for x in mixins_list)
CONDIMENTS_CHOICES = tuple((x,x)for x in condiments_list)
SEASONINGS_CHOICES = tuple((x,x)for x in seasonings_list)


class Taco(models.Model):
    shell_choice = models.CharField(max_length=100, choices=SHELL_CHOICES)
    base_layer_choice = models.CharField(max_length=100, choices=BASE_LAYER_CHOICES)
    mixin_choice = MultiSelectField(max_length=100, choices=MIXINS_CHOICES, max_choices=2)
    condiment_choice = MultiSelectField(max_length=100, choices=CONDIMENTS_CHOICES,max_choices=3)
    seasoning_choice = models.CharField(max_length=100, choices=SEASONINGS_CHOICES)
    
    def __str__(self):
        return f"{self.shell_choice}:{self.base_layer_choice}:{self.mixin_choice}:{self.condiment_choice}:{self.seasoning_choice}"