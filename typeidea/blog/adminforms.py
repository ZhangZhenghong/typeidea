from django import forms

class PostAdminForms(forms.ModelForm):
  desc = forms.CharField(widget=forms.Textarea, label='Abstract', required=False)

