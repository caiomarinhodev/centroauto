from django.forms import ModelForm, forms

from app.models import Cliente


class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClienteForm(ModelForm, BaseForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'cep']
