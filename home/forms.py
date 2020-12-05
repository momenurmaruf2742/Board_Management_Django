
from django.forms import forms

from home.models import RecruitInfo


class RecruitInfoForm(forms.ModelForm):
    class Meta:
        model = RecruitInfo
        fields = "__all__"

