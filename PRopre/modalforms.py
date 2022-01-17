from .models import Propre
from bootstrap_modal_forms.forms import BSModalForm


class ModalForm(BSModalForm):
    class Meta:
        model = Propre
        fields = ('Nom', 'prenom','telephone','num_compte')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save person'))
