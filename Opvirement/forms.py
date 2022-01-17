from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Op_virement
from PRopre.models import Propre


class VirementForm(forms.ModelForm):
    class Meta:
        model = Op_virement
        fields = ('dest_num', 'montant_v')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))

class ClientForm_Op(forms.ModelForm):
    class Meta:
        model = Propre
        fields = ['num_compte']