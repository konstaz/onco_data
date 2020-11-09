from django import forms
from data.models import Clinic


class AddClinicForm(forms.ModelForm):

    class Meta:
        model = Clinic
        field = (
            'research_name', 'patients_profile', 'date_condition', 'protocol_date', 'PI', 'sponsor', 'begin_date',
            'monitor', 'first_patient', 'name_doctor_field', 'patients_name_status', 'sae', 'f_o_p_data',
        )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.save()

        return instance
