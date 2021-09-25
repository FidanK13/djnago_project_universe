from django import forms
from .models import WorkModel

class WorkCreateForm(forms.ModelForm):
    class Meta:
        model=WorkModel
        exclude=['user_id','work_date']