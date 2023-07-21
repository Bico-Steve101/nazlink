from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Space, Discussion , Message , User
from .forms import SpaceForm, UserForm, NazlinkUserCreationForm


# Create your views here.

# request tells is the http object tells us the data that is sent to the backend
# the login page with the conditions 
def loginPage(request):
    
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower() # set to lower to match the register (case sensitive)
        password = request.POST.get('password')

        try:
            user = user.object.get(username=username, password=password)
        except:
            messages.error(request, 'OOOps!! sorry but seems like you are not in nazlink....') # this is passed in the nazlink_register page, for all error message

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or password does not exist...')
    context ={'page': page}
    return render(request, 'first/nazlink_register.html', context)
# the user logout
def logoutUser(request):
    logout(request)
    return redirect('home')

# the register page
def registerPage(request): 
    form = NazlinkUserCreationForm()     # the form is passed in the nazlink_register as {{form.as_p}} url name is register
                                         # what happens after a user registers
    if request.method == 'POST':
        form = NazlinkUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # the commit is set to false(frozen) soo that we can get the user object query the input below
            user.username = user.username.lower() # username entered set to lower to match the login page(case sensitive)
            user.save()
            messages.success(request, 'You are now a Nazlink User!...')

            login(request,user) # after the user is saved they are logged in
            return redirect('home')
        else:
            messages.error(request, 'Their was an error during registration!...')

    return render(request, 'first/nazlink_register.html', {'form': form} ) # creating the inbuilt django form for the register page

# the home page 
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    spaces = Space.objects.filter(
        Q(discussion__name__icontains=q) | 
        Q(name__icontains=q) | 
        Q(description__icontains=q))[0:6]               #querying the model manager this is to get all the spaces from the database, the filter method is for the q(space in sidebar)
    discussions = Discussion.objects.all().order_by('name')[0:10]
    spaces_count= spaces.count()
    space_messages = Message.objects.filter(Q(space__discussion__name__icontains=q)).order_by('-modify')[0:6] # modify to the user want
    context = {'spaces': spaces, 'discussions':discussions,  'spaces_count': spaces_count, 'space_messages': space_messages, } # this is the context and it is the data that is passed to the html file
    return render(request, 'first/home.html', context)                                  # the context is the data that is passed to the html file

# spaces where people can interact
def space(request, pk): # pk is the primary key and it is the id of the space
    space = Space.objects.get(id=pk) # this is to get the space from the database
    space_messages = space.message_set.all() # getting all the children of the space in models, that are in Message also in models(under Space)
    
    # getting the chats entered in models/Message
    participants = space.participants.all().order_by('name')
    
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            space = space,
            body = request.POST.get('text')
        ) 
        space.participants.add(request.user)
        return redirect('space', pk=space.id)

    
    context = {'space': space , 'space_messages': space_messages, 'participants':participants , } # passed through the context dic to be displayed blw

    return render(request, 'first/space.html', context) # the context is the data that is passed to the html   

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    spaces = user.space_set.all()
    space_messages = user.message_set.all()
    discussions = Discussion.objects.all()
    spaces_count= spaces.count()
    context = {'user': user, 'spaces':spaces, 'space_messages':space_messages, 'discussions':discussions, 'spaces_count':spaces_count}
    return render(request, 'first/user_profile.html', context)

@login_required(login_url='/login')
def updateProfile(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)  
    return render(request, 'first/edit-profile.html', {'form':form})

@login_required(login_url='/login')
def createSpace(request):
    form = SpaceForm()
    discussions = Discussion.objects.all()
    if request.method == 'POST':
        discussion_name = request.POST.get('discussion')
        discussion, created = Discussion.objects.get_or_create(name=discussion_name)
        
        Space.objects.create(
            founder=request.user,
            discussion=discussion,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'discussions': discussions}
    return render(request, 'first/space_form.html', context)

@login_required(login_url='/login')
def updateSpace(request, pk): # if someone requests to update space
    space = Space.objects.get(id=pk)
    form = SpaceForm(instance = space) # the form comes prefilled when someone requests to edit
    discussions = Discussion.objects.all()
    if request.user != space.founder:
        return HttpResponse('You are not the the creator of the space!!...')


    if request.method == 'POST':
        discussion_name = request.POST.get('discussion')
        discussion, created = Discussion.objects.get_or_create(name=discussion_name)
        space.name = request.POST.get('name')
        space.discussion = discussion
        space.description = request.POST.get('description')
        space.save()
        return redirect('home')

    context = { 'space':space, 'form': form, 'discussions': discussions}
    return render(request,'first/space_form.html',context)


@login_required(login_url='/login')
def deleteSpace(request, pk): # when someone requests to delete a room we get the room using the defined p
    space = Space.objects.get(id=pk)
   
    if request.user != space.founder:
        return HttpResponse('You are not the the creator of the space!!...')
   
    if request.method == 'POST':
        space.delete()
        return redirect('home')

    return render(request, 'first/delete.html', {'obj':space})


@login_required(login_url='/login')
def deleteMessage(request, pk): # when someone requests to delete a room we get the room using the defined p
    message = Message.objects.get(id=pk)
   
    if request.user != message.user:
        return HttpResponse('You are not the the writer of the message!!...')
   
    if request.method == 'POST':
        message.delete()
        return redirect('home')
        

    return render(request, 'first/delete.html', {'obj':message})

def discussionsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    discussions = Discussion.objects.filter(name__icontains=q)
    return render(request, 'first/discussions-page.html', {'discussions':discussions})

def activitiesPage(request):
    space_messages = Message.objects.all()
    return render(request, 'first/activities-page.html', {'space_messages':space_messages})

def spacesTopicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    spaces = Space.objects.filter(
        Q(discussion__name__icontains=q) | 
        Q(name__icontains=q) | 
        Q(description__icontains=q))
    spaces_count= spaces.count()
    context = {'spaces': spaces, 'spaces_count': spaces_count, } 
    return render(request, 'first/topics-page.html', context)

def error_404(request, exception):
    return render(request, "404.html", status=404) 
def error_400(request, exception):
    return render(request, "400.html", status=400) 
def error_403(request, exception):
    return render(request, "403.html", status=403) 
def error_500(request):
    return render(request, "500.html", status=500)                              