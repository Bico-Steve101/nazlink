from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=100, null=True)
    email=models.EmailField(unique=True, null=True)
    bio=models.TextField(null=True)

    
    avatar = models.ImageField(null=True, default="Profile-Avatar.png")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


# Create your models here.
# anytime you make changes to the models you have to make migrations and migrate them to the database 
# this is the model for the space and the information that will be stored in the database, the class is the table and the attributes are the fields
# models have id by default they are the primary key but we can add our own ids by adding the id field or uuid field

class Discussion(models.Model):  # this is the discussion table
    name = models.CharField(max_length=200) # this is the name of the discussion    

    def __str__(self):
        return self.name



class Space(models.Model): # this is the space table
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, ) # this is the foreign key and it is the relationship between the space and the user when deleting the user the spaces will not be deleted and the null and blank are for the admin page and the form and they are not required
    discussion = models.ForeignKey(Discussion, on_delete=models.SET_NULL, null=True, )  # this is the foreign key and it is the relationship between the discussion and the space when deleting the discussion the spaces will not be deleted and the null and blank are for the admin page and the form and they are not required
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) # null and blank are for the admin page and the form and they are not required
    participants = models.ManyToManyField(User, related_name="participants",  blank=True) # the participants can have many attributes hence many to many fields
    modify = models.DateField(auto_now=True) # this is the date that the space was modified
    created = models.DateTimeField(auto_now_add=True) # this is the date that the space was created and it will be added automatically when the space is created and does not change


    class Meta:
        ordering = ['-modify','-created'] # ordering the space from newest to oldest

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True) # this is the user that is sending the message and it is the user that is logged in and it is the user that created the space and it is the user that is the founder of the space and it is the user that is the participant in the space and it is the user that is the sender of the message and it is the user that is the author of the message and it is the user that is the creator of the message the null and blank are for the admin page and the form and they are not required
    space = models.ForeignKey(Space, on_delete=models.CASCADE) # this is the foreign key and it is the relationship between the space and the message when deleting the space the messages will be deleted
    body = models.TextField() # this is the message body and it is the text that the user will send in the space 
    modify = models.DateField(auto_now=True) # this is the date that the space was modified
    created = models.DateTimeField(auto_now_add=True) # this is the date that the space was created and it will be added automatically when the space is created and does not change    

    class Meta:
        ordering = ['modify','created'] # ordering the space from newest to oldest

    def __str__(self): 
        return self.body[:55] # this is to return the first 55 characters of the message body and not the whole message body