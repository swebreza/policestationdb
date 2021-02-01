from django import forms
from my_django_app.models import hellow
from my_django_app.models import fir
from my_django_app.models import officer

from django.contrib.auth import authenticate
class crform(forms.ModelForm):
    class Meta:
        model = hellow
        fields = "__all__"

    class Meta:
        model = fir
        fields = "__all__"

    class Meta:
        model = officer
        fields = "__all__"
