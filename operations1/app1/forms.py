from django import forms
from django.contrib.auth.password_validation import password_changed


class AdditionForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()

class BmiForm(forms.Form):
      weight=forms.IntegerField()
      height=forms.IntegerField()


class SignupForm(forms.Form):
     gender_choices=(('male','Male'),('female','Female'))
     role_choices=(('admin','Admin'),('student','Student'))
     username=forms.Textarea()
     password=forms.CharField(widget=forms.PasswordInput)
     place=forms.CharField()
     gender=forms.ChoiceField(choices=gender_choices,widget=forms.RadioSelect)
     role=forms.ChoiceField(choices=role_choices)
     email=forms.EmailField()

class CalorieForm(forms.Form):
    activity_choices=((1.2,'sedentary'),
                      (1.375,'lightly active'),
                      (1.55,'moderately active'),
                      (1.725,'very active'),
                      (1.9,'extra active'))
    gender_choices = (('male', 'Male'), ('female', 'Female'))

    weight=forms.IntegerField()
    height=forms.IntegerField()
    age=forms.IntegerField()
    activity_levels=forms.ChoiceField(choices=activity_choices)
    gender= forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect)

