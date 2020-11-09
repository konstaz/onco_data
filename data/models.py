from django.db import models

from data import model_choices as mch


# class Team(models.Model):
#    # doctors_name = models.CharField(max_length=128)
#    # access = models.PositiveIntegerField(choices=mch.research_roles)

#    # def __unicode__(self):
#        # return "".join(self.doctors_name, " | ", self.access)


# class Patient(models.Model):
#    # patients_name = models.CharField(max_length=128)
#    # status = models.PositiveIntegerField(choices=mch.research_status)

#    # def __unicode__(self):
#        # return "".join(self.patients_name, " | ", self.status)


# class Fop(models.Model):
#    fop_name = models.CharField(max_length=128)

#    # def save(self, *args, **kwargs):
#       # super().save(*args, **kwargs)


class Clinic(models.Model):
    # Clinical research
    research_name = models.CharField(max_length=256)
    patients_profile = models.CharField(max_length=256)
    date_condition = models.DateTimeField()
    protocol_date = models.CharField(max_length=128)  # дата и номер протокола ДФЦ утверждения
    PI = models.PositiveIntegerField(choices=mch.PI_mentors)
    # Clinical data
    sponsor = models.CharField(max_length=256)
    begin_date = models.DateTimeField()

    # fop = models.ManyToManyField(Fop)  # FOP data
    monitor = models.CharField(max_length=256)
    first_patient = models.DateTimeField()  # date of registration of the first patient
    # Team data
    # team = models.ManyToManyField(Team)
    name_doctor_field = models.CharField(max_length=512)  # name with access to research
    # Patient data
    # patient = models.ManyToManyField(Patient)
    patients_name_status = models.CharField(max_length=512)  # Patients and their current status
    sae = models.CharField(max_length=512)
    # Update sign date for monitoring
    update = models.DateTimeField(auto_now_add=True)
    f_o_p_data = models.CharField(max_length=256)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
