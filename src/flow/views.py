from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from flow.forms import DemanderCritiqueForm, CreerCritiqueForm
from flow.models import CreerCritiqueMod, DemanderCritiqueMod
from login.models import User

# Create your views here.
@login_required
def accueil(request):
     critique_cree = CreerCritiqueMod.objects.all()
     critique_demandee = DemanderCritiqueMod.objects.all()
     users_data = User.objects.all()
     user_active = request.user
     liste_follows = []
     liste_critique_demandee_user_active = []

     for user in users_data:
          if user_active.username == user.username:
               user_active_data = user
               break
     
     for follows in user_active_data.follows.all():
          liste_follows.append(follows)

     for critique in critique_demandee:
          if len(liste_follows) != 0 :
               for follows in liste_follows:
                    if critique.createur.username == user_active.username or critique.createur.username == follows.username:
                         liste_critique_demandee_user_active.append(critique)
          else: 
               if critique.createur == user_active.username:
                         liste_critique_demandee_user_active.append(critique)


     numero = ""
     return render(request, 'accueil.html', context={'critique_cree' : critique_cree, 'critique_demandee' : liste_critique_demandee_user_active, 'numero' : numero})

@login_required
def demander_critique(request):
     form_demander_critique = DemanderCritiqueForm()
     message = " "
     user = request.user
     print(user.username)
     if request.method == "POST":
          form_demander_critique = DemanderCritiqueForm(request.POST, request.FILES)
          if form_demander_critique.is_valid():
               demander_critique = DemanderCritiqueMod()
               demander_critique.titre = form_demander_critique.cleaned_data['titre_demande']
               demander_critique.description = form_demander_critique.cleaned_data['description']
               demander_critique.img_livre = form_demander_critique.cleaned_data['img_livre']
               demander_critique.createur = user
               demander_critique.save()
          
               return redirect('accueil')
     
          else:
               message = "Veuillez respecter les conditions"

     return render(request, 'demander_critique.html', context={'form_demander_critique' : form_demander_critique, 'message' : message})

@login_required
def creer_critique(request):
     form_creer_critique = CreerCritiqueForm()
     form_demander_critique = DemanderCritiqueForm()
     numero_critique_rep = request.POST.get('critique_numero', None)
     data_demande_critique = DemanderCritiqueMod.objects.all()
     datas = ""
     user = request.user
     if numero_critique_rep != None:
          for i in range(len(data_demande_critique)):
               if data_demande_critique[i].id == int(numero_critique_rep):
                    datas = data_demande_critique[i]
                    break
     else: 
          pass

     message = ' '
     if request.method == 'POST' and numero_critique_rep == None:
          form_demander_critique = DemanderCritiqueForm(request.POST, request.FILES)
          form_creer_critique = CreerCritiqueForm(request.POST)
          
          if all ([form_creer_critique.is_valid(), form_demander_critique.is_valid()]):
               
                
               creer_critique = CreerCritiqueMod()
               creer_critique.titre = form_creer_critique.cleaned_data['titre_creer']
               creer_critique.note = form_creer_critique.cleaned_data['note']
               creer_critique.commentaire = form_creer_critique.cleaned_data['commentaire']
               creer_critique.createur = user
               creer_critique.save()

               demander_critique = DemanderCritiqueMod()
               demander_critique.titre = form_demander_critique.cleaned_data['titre_demande']
               demander_critique.description = form_demander_critique.cleaned_data['description']
               demander_critique.img_livre = form_demander_critique.cleaned_data['img_livre']
               demander_critique.reponse_critique = creer_critique
               demander_critique.createur = user
               demander_critique.save()
              

               return redirect('accueil')
          else:
               message = "Veuillez respecter les conditions"
     elif request.method == 'POST' and numero_critique_rep != None: 
           form_creer_critique = CreerCritiqueForm(request.POST)
           if form_creer_critique.is_valid():

               creer_critique = CreerCritiqueMod()
               creer_critique.titre = form_creer_critique.cleaned_data['titre_creer']
               creer_critique.note = form_creer_critique.cleaned_data['note']
               creer_critique.commentaire = form_creer_critique.cleaned_data['commentaire']
               creer_critique.createur = user
               creer_critique.save()

               datas.reponse_critique = creer_critique
               datas.save()
               
               return redirect('accueil')
           else : 
                message = "Veuillez respecter les conditions"
     

                


     return render(request, 'creer_critique.html', context={'form_creer_critique' : form_creer_critique, 'form_demander_critique' : form_demander_critique,  'message' : message})

@login_required
def reponse_demande_critique(request):


     numero_critique_rep = request.POST.get('critique_rep', None)
     data_demande_critique = DemanderCritiqueMod.objects.all()
     datas = ""

     for i in range(len(data_demande_critique)):
         if data_demande_critique[i].id == int(numero_critique_rep):
              datas = data_demande_critique[i]
              break

     print(datas)
     form_creer_critique = CreerCritiqueForm()

     return render(request, 'creer_critique.html', context={'form_creer_critique' : form_creer_critique, 'numero_critique_rep' : numero_critique_rep,  "data" : datas })

