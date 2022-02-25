import datetime
from django import forms
from django.core.exceptions import ValidationError


class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Insira uma data entre hoje e daqui a 4 semanas.")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError("Data inválida: Data informada menor que a data de hoje.")

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError("Data inválida: Data informada maior do que 4 semanas.")

        return data