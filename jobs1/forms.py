from django import forms

class NameForm(forms.Form):
    company_name = forms.CharField( max_length=100,initial = "company name",required= False)
    profile = forms.CharField( max_length=100 , initial = "profile",required = False)
    location = forms.CharField( max_length=100 , initial = "location",required = False)
    experience = forms.ChoiceField(choices=[('Experience','Experience' ), ('0','0'), ('1','1'),('2','2'),('3','3'),('4','4'), ('5','5') ])

class SignUpForm(forms.Form):
    name = forms.CharField( max_length=100 , initial = "name",required = True)
    user_name = forms.CharField( max_length=100 , initial = "user_name",required = True)
    email_id = forms.CharField( max_length=100,initial = "email_id",required= True)
    password = forms.CharField( max_length=100 , initial = "password",required = True)
    prefered_profile = forms.CharField( max_length=100 , initial = "prefered_profile",required = False)
    prefered_prog_lang = forms.CharField( max_length=100 , initial = "prefered_prog_lang",required = False)
    prefered_location = forms.CharField( max_length=100 , initial = "location",required = False)
    exp_from = forms.CharField( max_length=2 , initial = "exp_from",required = False)
    exp_to = forms.CharField( max_length=2 , initial = "exp_to",required = False)

class SignInForm(forms.Form):
    user_name = forms.CharField( max_length=100 , initial = "user_name",required = True)
    password = forms.CharField( max_length=100 , initial = "password",required = True)
