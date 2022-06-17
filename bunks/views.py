#Code by Genna Gams based off of tutorial from django https://docs.djangoproject.com/en/2.2/intro/

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Bunk, User

#View for the homepage /bunks
def homepage(request):
    users = User.objects.all()
    return render(request, 'bunks/homepage.html', {'users': users})
    #return HttpResponse("Homepage here")

#View for the homepage /bunks/allbunks
def allbunks(request):
    all_bunks = [str(b) for b in Bunk.objects.all()]
    context = {
        'bunks': all_bunks,
    }
    return render(request, 'bunks/allbunks.html', context)

#View for the homepage /bunks/bunk
def bunk(request):
    users = User.objects.all()
    return render(request, 'bunks/makebunk.html', {'users': users})
    #return HttpResponse("put bunk form here")

#View for the homepage /bunks/<userame>
def personalbunks(request, un):
    curr_user = get_object_or_404(User, username = un)
    print(curr_user.id)
    user_bunks = [str(b) for b in Bunk.objects.filter(to_user = curr_user)]
    return render(request, 'bunks/personalbunks.html', {'user': curr_user, 'bunks': user_bunks})
    #return HttpResponse("All bunks sent to %s" % username)
    
#executes a POST request to /bunks/bunk/submit -- no view created
def submitbunk(request):
    users = User.objects.all()
    try:
        to_choice = users.get(username=request.POST['tochoice'])
        from_choice = users.get(username=request.POST['fromchoice'])
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'bunks/makebunk.html', {
            'users': users,
            'error_message': "You didn't select a choice.",
        })
    else:
        b = Bunk(from_user=from_choice, to_user=to_choice, time=timezone.now())
        b.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('bunks:homepage'))