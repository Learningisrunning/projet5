from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flow.models import CreerCritiqueMod, DemanderCritiqueMod

# Create your views here.
@login_required
def post_user(request):
    critique_crees = CreerCritiqueMod.objects.all()
    critique_demandees = DemanderCritiqueMod.objects.all()
    user = request.user 
    liste_critique_crees = []
    liste_critique_demandees = []

    for i in range(len(critique_crees)): 
        if user.username == critique_crees[i].createur:
            liste_critique_crees.append(critique_crees[i])

    for j in range(len(critique_demandees)): 
        if user.username == critique_demandees[j].createur:
            liste_critique_demandees.append(critique_demandees[j])
        #faire le test ici et créer les liste des demande et critique crees

     
    return render(request, 'posts.html', context={ 'user' : user, 'liste_critique_crees' : liste_critique_crees, 'liste_critique_demandees' : liste_critique_demandees })