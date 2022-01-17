from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Op_retrait
from PRopre.models import Propre


class RetraitForm(forms.ModelForm):
    class Meta:
        model = Op_retrait
        fields = ('montant_R',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class ClientForm_Op_r(forms.ModelForm):
    class Meta:
        model = Propre
        fields = ('num_compte',)