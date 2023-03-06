from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from flow.models import CreerCritiqueMod, DemanderCritiqueMod
from flow.forms import CreerCritiqueForm, DemanderCritiqueForm

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
        

     
    return render(request, 'posts.html', context={ 'user' : user, 'liste_critique_crees' : liste_critique_crees, 'liste_critique_demandees' : liste_critique_demandees })

def modify_deleted(request):
    
    user_on = request.user
    critique_demandees = DemanderCritiqueMod.objects.all()
    critique_cree = CreerCritiqueMod.objects.all()
    

    if 'modify_btn_demande' in request.POST :
        post_id = request.POST.get('modify_btn_demande', None)
    
        for critique in critique_demandees:
            if critique.id == int(post_id):
                data = {
                    'titre_demande' : critique.titre,
                    'description' : critique.description,
                    'img_livre' :  critique.img_livre
                }

                form = DemanderCritiqueForm(initial=data)

                
                return render(request, 'modify.html', context={'form' : form})

    if 'deleted_btn_demande' in request.POST : 
        post_id = request.POST.get('deleted_btn_demande', None)
        for critique in critique_demandees:
            if critique.id == int(post_id):
                critique.delete()
                redirect('posts-user')
    
    if 'modify_btn_cree' in request.POST :
        post_id = request.POST.get('modify_btn_cree', None)
        print(post_id)
    
        for critique in critique_cree:
            if critique.id == int(post_id):
                data = {
                    'titre_creer' : critique.titre,
                    'note' : critique.note,
                    'commentaire' :  critique.commentaire
                }

                form = CreerCritiqueForm(initial=data)

                
                return render(request, 'modify.html', context={'form' : form})

    if 'deleted_btn_cree' in request.POST : 
        post_id = request.POST.get('deleted_btn_cree', None)
        for critique in critique_cree:
            if critique.id == int(post_id):
                critique.delete()
                redirect('posts-user')
        
 


    return redirect('posts-user')
