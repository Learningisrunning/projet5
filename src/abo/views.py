from django.shortcuts import render, redirect
from login.models import User
# Create your views here.
def abonnement(request):
    User_on = request.user
    
    abonnements = []
    abonnes = []

    abonnements = User_on.follows.all()
    abonnes = User_on.followers.all()
    
    return render(request, 'abonnement.html', context={'abonnements' : abonnements, 'abonnes' : abonnes })

def unfollow(request):
    follower_to_unfollow = request.POST.get('unfollow_btn', None)
    print(follower_to_unfollow)
    user_on = request.user
    liste_follows = user_on.follows.all()
    print(liste_follows)

    for follow in liste_follows:
        if follow.id == int(follower_to_unfollow):
            user_on.follows.remove(follow)
            print(liste_follows)
            break

    print(liste_follows[0].id)
    user_list = User.objects.all()

    return redirect('abonnements')

def follow(request):

    user_to_follow = request.POST.get('test', None)
    print(user_to_follow)
    User_on = request.user
    users = User.objects.all()
    Validation = False

    abonnements = []
    abonnes = []

    abonnements = User_on.follows.all()
    abonnes = User_on.followers.all()

    for user in users:
        if user_to_follow == user.username : 
            User_on.follows.add(user) 
            validation = True
            break
    
    if Validation == False:
        message = "Utilisateur introuvable"

    return render(request, 'abonnement.html', context={'abonnements' : abonnements, 'abonnes' : abonnes, 'message' : message })

