import joblib
from django.shortcuts import render
from loan_prediction_app.form import LoanPredictionForm

def loan_prediction(request):
    # Load the model from the file
    clf = joblib.load('C:/Users/dell/.vscode/atharv/loan_prediction_project/loan_prediction_app/model.pkl')

    if request.method == 'POST':
        form = LoanPredictionForm(request.POST)
        if form.is_valid():
            # Get the form data
            data = {
                'Gender': form.cleaned_data['Gender'],
                'Married': form.cleaned_data['Married'],
                'Dependents': form.cleaned_data['Dependents'],
                'Education': form.cleaned_data['Education'],
                'Self_Employed': form.cleaned_data['Self_Employed'],
                'ApplicantIncome': form.cleaned_data['ApplicantIncome'],
                'CoapplicantIncome': form.cleaned_data['CoapplicantIncome'],
                'LoanAmount': form.cleaned_data['LoanAmount'],
                'Loan_Amount_Term': form.cleaned_data['Loan_Amount_Term'],
                'Credit_History': form.cleaned_data['Credit_History'],
                'Property_Area': form.cleaned_data['Property_Area'],
            }

            # Create a list of lists to represent the input data for the model prediction
            new_data = [
                [
                    data['Gender'], data['Married'], data['Dependents'],
                    data['Education'], data['Self_Employed'],
                    data['ApplicantIncome'], data['CoapplicantIncome'],
                    data['LoanAmount'], data['Loan_Amount_Term'],
                    data['Credit_History'], data['Property_Area']
                ]
            ]

            # Make predictions using the loaded model
            predictions = clf.predict(new_data)

            return render(request, 'result.html', {'predictions': predictions})
    else:
        form = LoanPredictionForm()

    return render(request, 'loan_prediction.html', {'form': form})

