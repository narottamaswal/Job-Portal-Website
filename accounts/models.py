import datetime
from django.db import models
#from django.contrib.auth.models import User,UserManager
#from django.forms import ModelForm
from django.db.models.signals import post_save
#from .models import UserProfile
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.

#
class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    savedjobs=models.TextField(max_length=50)
    email_confirmed = models.BooleanField(default=False)
    skills=models.TextField(max_length=200,blank=True,default=" ")
    additionalinfo=models.TextField(max_length=100,blank=True,default=" ")
    city=models.CharField(max_length=10,blank=False,default=" ")
    def __str__(self):

        return f'{self.user.username}'



class Example2(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=20)

@receiver(post_save,sender=User)
def create_userprofile(sender,instance,created,**kwargs):
    if created:
        print("hello")
        print(instance)
        UserProfile.objects.create(user=instance)
        print(UserProfile)


@receiver(post_save,sender=User)
def save_userprofile(sender,instance,**kwargs):
    print("hello")
    instance.profile.save()

class Jobs(models.Model):
    url = models.URLField(blank=False,unique=True,max_length=250)
    date=models.DateField(blank=False,default=datetime.date.today())
    minsal=models.IntegerField(blank=True,default=0)
    maxsal = models.IntegerField(blank=True,default=0)
    jobtitle=models.TextField(blank=False, max_length=100)
    companyname=models.CharField(blank=False,max_length=500)
    minexp=models.IntegerField(blank=False,default=0,max_length=10)
    maxexp = models.IntegerField(blank=False,default=0, max_length=10)
    location=models.CharField(blank=True,max_length=300 )
    jobdescription=models.TextField(blank=False,max_length=500)
    originaljoburl=models.URLField(blank=True)
    jobportal=models.CharField(blank=True,max_length=20)
    skills=models.CharField(blank=True,max_length=1000)
    jobtype=models.CharField(blank=True,max_length=10)

class Saved(models.Model):
    Jobtitle=models.CharField(blank=True, max_length=100)
    SORTING_OPTIONS = [
        ('DATE', 'DATE'),
        ('SALARY', 'SALARY'),
        ('EXPERIENCE', 'EXPERIENCE'),
    ]
    Sortby = models.CharField(choices=SORTING_OPTIONS,max_length=100)

class Temp(models.Model):
    searchedtitle=models.CharField(blank=False,max_length=20)

class InfoSearch(models.Model):
    searchedtitle=models.CharField(blank=False,max_length=20)

class Resume(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phoneno = models.CharField(max_length=30,blank=True)
    linkedinprofileurl = models.CharField(max_length=30,blank=True)
    usertitle = models.CharField(max_length=30)
    skills = models.TextField(max_length=100)
    extrainfo = models.TextField(max_length=200)
    address=models.CharField(max_length=42,blank=True)
    projecttitle1 = models.CharField(max_length=30,blank=True)
    projectdescription1 = models.TextField(max_length=200,blank=True)
    projectyoc1 = models.CharField(max_length=30,blank=True)
    projecttitle2= models.CharField(max_length=30,blank=True)
    projectdescription2 = models.TextField(max_length=200,blank=True)
    projectyoc2 = models.CharField(max_length=30,blank=True)
    projecttitle3 = models.CharField(max_length=30,blank=True)
    projectdescription3 = models.TextField(max_length=200,blank=True)
    projectyoc3 = models.CharField(max_length=30,blank=True)

    companyname1 = models.CharField(max_length=30,blank=True)
    designation1 = models.CharField(max_length=30,blank=True)
    companyyow1 = models.CharField(max_length=30,blank=True)
    companyname2 = models.CharField(max_length=30,blank=True)
    designation2 = models.CharField(max_length=30,blank=True)
    companyyow2 = models.CharField(max_length=30,blank=True)
    companyname3 = models.CharField(max_length=30,blank=True)
    designation3 = models.CharField(max_length=30,blank=True)
    companyyow3 = models.CharField(max_length=30,blank=True)

    institute1 = models.CharField(max_length=30,blank=True)
    degree1 = models.CharField(max_length=30,blank=True)
    stream1 = models.CharField(max_length=30,blank=True)
    studyforyears1 = models.CharField(max_length=30,blank=True)
    grade1 = models.CharField(max_length=30,blank=True)
    institute2 = models.CharField(max_length=30,blank=True)
    degree2 = models.CharField(max_length=30,blank=True)
    stream2 = models.CharField(max_length=30,blank=True)
    studyforyears2 = models.CharField(max_length=30,blank=True)
    grade2 = models.CharField(max_length=30,blank=True)
    institute3 = models.CharField(max_length=30,blank=True)
    degree3 = models.CharField(max_length=30,blank=True)
    stream3 = models.CharField(max_length=30,blank=True)
    studyforyears3 = models.CharField(max_length=30,blank=True)
    grade3 = models.CharField(max_length=30,blank=True)




class state(models.Model):
    name = models.CharField(max_length=30)
    sid=models.IntegerField(max_length=30)
    def __str__(self):
        return self.name

class city(models.Model):
    name = models.CharField(max_length=30)
    cid=models.IntegerField(max_length=110)
    def __str__(self):
        return self.name
