from django.forms import ModelForm
from .models import Space, User
from django.contrib.auth.forms import UserCreationForm


class SpaceForm(ModelForm): # creating a new form for the Space
    class Meta:
       model = Space # the name of the Space specified
       fields = '__all__' # list of fields to include in the form fields, they are required(the founder, name and others under space that are editable)
       exclude = ['founder', 'participants'] #the list of items to exclude from the entry field

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'name','username', 'email','bio','avatar']

class NazlinkUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','name','username','password1','password2']