from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from PRopre.models import Propre
from bootstrap_modal_forms.forms import BSModalModelForm

class ClientForm(forms.ModelForm):
    class Meta:
         model = Propre
         fields = ('Nom', 'prenom','telephone','num_compte')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


class ClientForm_Op(forms.ModelForm):
    class Meta:
        model = Propre
        fields = ['num_compte',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))


class ClientModelForm(BSModalModelForm):
    class Meta:
        model = Propre
        fields = ('Nom', 'prenom','telephone','num_compte')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
