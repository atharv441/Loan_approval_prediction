# your_app/models.py
from django.db import models

class UserData(models.Model):
    GENDER_CHOICES = [
        (1, 'Male'),
        (2, 'Female'),
    ]

    MARRIED_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    DEPENDENTS_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3+'),
    ]

    EDUCATION_CHOICES = [
        (1, 'Graduate'),
        (2, 'Not Graduate'),
    ]

    SELF_EMPLOYED_CHOICES = [
        (1, 'Yes'),
        (2, 'No'),
    ]

    PROPERTY_AREA_CHOICES = [
        (1, 'Urban'),
        (2, 'Semiurban'),
        (3, 'Rural'),
    ]

    gender = models.IntegerField(choices=GENDER_CHOICES)
    married = models.IntegerField(choices=MARRIED_CHOICES)
    dependents = models.IntegerField(choices=DEPENDENTS_CHOICES)
    education = models.IntegerField(choices=EDUCATION_CHOICES)
    self_employed = models.IntegerField(choices=SELF_EMPLOYED_CHOICES)
    applicant_income = models.FloatField()
    coapplicant_income = models.FloatField()
    loan_amount = models.FloatField()
    loan_amount_term = models.FloatField()
    credit_history = models.FloatField()
    property_area = models.IntegerField(choices=PROPERTY_AREA_CHOICES)
    prediction = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.gender} - {self.applicant_income}'

  



