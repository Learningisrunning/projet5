from django.db import models

# Create your models here.


class CreerCritiqueMod(models.Model):
    class Note(models.TextChoices):
        UN = "1"
        DEUX = "2"
        TROIS = "3"
        QUATRE = "4"
        CINQ = "5"

    titre = models.CharField(max_length=100)
    note = models.CharField(choices = [(tag, tag.value) for tag in Note],  max_length=3)
    commentaire = models.CharField(max_length=600)
    
    def __str__(self) -> str:
        return self.titre


class DemanderCritiqueMod(models.Model):
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=1025)
    img_livre = models.FileField()
    reponse_critique = models.ForeignKey(CreerCritiqueMod, null = True,  on_delete = models.SET_NULL)


    def __str__(self) -> str:
        return self.titre