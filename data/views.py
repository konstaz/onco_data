from django.http import HttpResponse  # noqa
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView, CreateView

from data.models import Clinic  # ClinicData, Team, Patient
from data import model_choices as mch  # noqa


class ClinicalResearch(ListView):
    paginate_by = 50
    queryset = Clinic.objects.all()
    template_name = 'research-list.html'


class ClinicalData(ListView):
    queryset = Clinic.objects.all()
    template_name = 'clinic-data.html'


class EditClinic(UpdateView):
    template_name = 'edit-data.html'
    model = Clinic
    fields = 'research_name', 'patients_profile', 'date_condition', 'protocol_date', 'PI', 'sponsor', 'begin_date', \
             'monitor', 'first_patient', 'name_doctor_field', 'patients_name_status', 'sae', 'f_o_p_data'
    success_url = reverse_lazy('data:clinical_research')


class DeleteClinic(DeleteView):
    model = Clinic
    success_url = reverse_lazy('data:clinical_research')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class AddClinic(CreateView):
    template_name = 'clinic_form.html'
    model = Clinic
    fields = 'research_name', 'patients_profile', 'date_condition', 'protocol_date', 'PI', 'sponsor', 'begin_date', \
             'monitor', 'first_patient', 'name_doctor_field', 'patients_name_status', 'sae', 'f_o_p_data'
    success_url = reverse_lazy('data:clinical_research')
