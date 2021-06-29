from django import forms

class NameForm(forms.Form):
    company_name = forms.CharField( max_length=100,initial = "company name",required= False)
    profile = forms.CharField( max_length=100 , initial = "profile",required = False)
    location = forms.CharField( max_length=100 , initial = "location",required = False)
    experience = forms.ChoiceField(choices=[('Experience','Experience' ), ('0','0'), ('1','1'),('2','2'),('3','3'),('4','4'), ('5','5') ])
