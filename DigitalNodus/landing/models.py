from django.db import models

# Create your models here.

class Member(models.Model):
    all_names = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    whatsapp_number = models.CharField(unique=True, max_length=15)
    profession = models.CharField()
    sex = models.CharField(choices=[
        ("M","M"),
        ("F","F")
    ])
    institution = models.CharField(max_length=255)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Membre"
        ordering = ['created_at']
    
    def __str__(self):
        return self.all_names
    

class OpenSourceProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Projets open source"
        ordering = ['created_at']
    
    def __str__(self):
        return self.name 
    


class SocialProofComment(models.Model):
    name = models.CharField(max_length=255)
    thumbnail_url = models.URLField()
    fonction = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Avis Social"
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.name} |{self.fonction}" 



class Event(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, default="#")
    url_image = models.URLField()
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=255, default="Kalemie")
    places_event = models.IntegerField(default=50)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Evenement"
        ordering = ["-created_at"]

    def __str__(self): return self.name


class Reservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default="None")
    all_names = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    whatsapp_number = models.CharField(unique=True, max_length=15)
    profession = models.CharField()
    sex = models.CharField(choices=[
        ("M","M"),
        ("F","F")
    ])
    institution = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reservation"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.all_names



class Support(models.Model):
    name = models.CharField(max_length=255)
    url_site = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Soutient"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name}" 
    


class LinkGroupDigitalNodus(models.Model):
    link = models.URLField()

    def __str__(self): return self.link



