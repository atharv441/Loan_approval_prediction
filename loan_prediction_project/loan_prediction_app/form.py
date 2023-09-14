# your_app/forms.py
from django import forms

class LoanPredictionForm(forms.Form):
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

    Gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    Married = forms.ChoiceField(choices=MARRIED_CHOICES, widget=forms.RadioSelect)
    Dependents = forms.ChoiceField(choices=DEPENDENTS_CHOICES, widget=forms.Select)
    Education = forms.ChoiceField(choices=EDUCATION_CHOICES, widget=forms.RadioSelect)
    Self_Employed = forms.ChoiceField(choices=SELF_EMPLOYED_CHOICES, widget=forms.RadioSelect)
    ApplicantIncome = forms.FloatField()
    CoapplicantIncome = forms.FloatField()
    LoanAmount = forms.FloatField()
    Loan_Amount_Term = forms.FloatField()
    Credit_History = forms.FloatField()
    Property_Area = forms.ChoiceField(choices=PROPERTY_AREA_CHOICES, widget=forms.Select)
