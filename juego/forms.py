from django import forms



def FormJudadores(form.Form):
    jugadores = forms.CharField(help_text='Ingrese los judagores separados por coma')


def FormNumero(forms.Form):
    numero = forms.CharField()

    def clean_numero(self):
        numero = self.cleaned_data['numero']
        # validacion
        if not numero.isdigit():
            raise forms.ValidationError('no es un numero. ')

        return numero
