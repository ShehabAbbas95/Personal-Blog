from django import forms
import datetime

class NameForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    comment= forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":40, "style":'resize:none;margin:35px'}))
