from django.contrib import admin

# Register your models here.
from .models import Space, Discussion, Message , User # this is to import the model from the models.py file

admin.site.register(Space) # this is to register the model in the admin page and the admin page will be able to see the model and the fields
admin.site.register(Discussion) # this is to register the Discussion model in the admin page and the admin page will be able to see the model and the fields
admin.site.register(Message) # this is to register the Message model in the admin page and the admin page will be able to see the model and the fields
admin.site.register(User)# register the user from the model.py