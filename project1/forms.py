from django import forms
class InputForm(forms.Form): 
  
    Text= forms.CharField(widget=forms.Textarea)