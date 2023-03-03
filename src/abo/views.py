from django.shortcuts import render
from login.models import User
# Create your views here.
def abonnement(request):
    utilisateur = User.objects.all()
    print(utilisateur)
    return render(request, 'abonnement.html', context={'utilisateur' : utilisateur})