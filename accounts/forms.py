from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms.models import ModelForm
from .models import UserProfile,Jobs,Saved,InfoSearch,Resume
from django.forms import modelformset_factory


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True,max_length=40)
    first_name = forms.CharField(required=True,max_length=40)
    last_name = forms.CharField(required=True,max_length=40)
    username = forms.CharField(required=True,max_length=10)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )



class LoginForm(forms.Form):
        username = forms.CharField(required=True, label='Enter your username', max_length=100)
        password = forms.CharField(required=True, label='Enter your password', widget=forms.PasswordInput())




class UserUpdateForm(ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image','skills','additionalinfo','city']


class SavedJobsSearch(ModelForm):
    class Meta:
        model=Saved
        fields = ['Jobtitle','Sortby']


class InfoSearchForm(ModelForm):
    jobtitle=forms.CharField(required=False,max_length=20,widget=forms.TextInput(attrs={'placeholder': 'ENTER JOBTITLE, DESIGNATION OR SKILL'}))
    class Meta:
        model=InfoSearch
        fields=['jobtitle']

class JobsSearchForm(ModelForm):
    INTEGER_CHOICES = [tuple([x, x]) for x in range(0, 32)]
    experience = forms.ChoiceField(required=False,choices=INTEGER_CHOICES)
    SALARY_CHOICES = [
        ('any', 'any'),
        ('below1lac', 'Below >1 Lacs'),
        ('1to3Lacs', '1-3'),
        ('3to5lacs', '3-5'),
        ('5to7lacs', '5-7'),
        ('7to9lacs', '7-9'),
        ('9to11lacs', '10-11'),
        ('above11lacs', 'Above 11'),
    ]
    salary = forms.ChoiceField(required=False, choices=SALARY_CHOICES)
    jobtitle=forms.CharField(required=True,max_length=20,widget=forms.TextInput(attrs={'placeholder': 'ENTER JOBTITLE, DESIGNATION OR SKILL'}))
    DATE_POSTED_CHOICES = [
        ('Anytime', 'Anytime'),
        ('Within1day', 'Within 1 Day'),
        ('Within1week', 'Within 1 Week'),
        ('Within15days', 'Within 15 Days'),
        ('WithinAMonth', 'Within A Month'),
        ('Within3Months', 'Within 3 Months'),
        ('Within6Months', 'Within 6 Months'),
        ('Within1Year', 'Within 1 Year'),
    ]
    dateposted = forms.ChoiceField(required=False, choices=DATE_POSTED_CHOICES)
    companyname= forms.CharField(required=False,max_length=25,widget=forms.TextInput(attrs={'placeholder': 'ENTER COMPANY NAME'}))
    skills=forms.CharField(required=False,max_length=30,widget=forms.TextInput(attrs={'placeholder': 'ENTER SKILLS'}))
    NO_OF_JOBS = [
        (10, '10'),
        (30, '30'),
        (50, '50'),
        (100, '100'),
    ]
    noofjobs = forms.ChoiceField(required=False, choices=NO_OF_JOBS)
    JOB_TYPES = [
        ('FULL-TIME', 'FULL-TIME',),
        ('PART-TIME', 'PART-TIME'),
        ('INTERNSHIP', 'INTERNSHIP'),
        ('CONTRACT', 'CONTRACT'),
    ]
    jobtype = forms.ChoiceField(required=False, choices=JOB_TYPES)
    location = forms.CharField(required=False,max_length=15,widget=forms.TextInput(attrs={'placeholder': 'ENTER LOCATION'}))

    class Meta:
        model = Jobs
        fields = ['jobtitle','experience','salary','location','dateposted','companyname','skills','noofjobs','jobtype']


class ResumeMain(forms.ModelForm):
    class Meta:
        model=Resume
        fields=('__all__')