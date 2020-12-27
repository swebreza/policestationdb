from django import forms
from my_django_app.models import hellow

class crform(forms.ModelForm):
    class Meta:
        model = hellow
        fields = "__all__"