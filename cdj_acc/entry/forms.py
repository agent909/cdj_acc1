from django import forms


class AccountReceivableForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control form-control-sm', 
        'type':'date',
        }))
    documentNumber = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class':'form-control form-control-sm',
        'placeholder':'Doc No.'
    }))
    buyer = forms.CharField(max_length=180, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Solt to',
        'data-target':'#AReceivable_buyer_names_modal',
        'data-toggle':'modal',
        'id':'ar_buyer_name',
    }))
    cash = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Cash',
    }))

    def __str__(self):
        return 'Account Receivable'


class SalesForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control form-control-sm', 
        'type':'date',
        }))
    documentNumber = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class':'form-control form-control-sm',
        'placeholder':'Doc No.',
    }))
    buyer = forms.CharField(max_length=180, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Solt to',
    }))
    cash = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Cash',
    }))

    def __str__(self):
        return 'Sales'


class PaymentToAccountReceivableForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control form-control-sm', 
        'type':'date',
    }))
    documentNumber = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class':'form-control form-control-sm',
        'placeholder':'Doc No.'
    }))
    debtor = forms.CharField(max_length=180, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Debtor',
        'data-target':'#AReceivable_debtor_names_modal',
        'data-toggle':'modal',
        'id':'ar_debtor_name',
    }))
    cash = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Cash',
    }))

    def __str__(self):
        return 'Payment To Account Receivable'


class LoansReceivableForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control form-control-sm', 
        'type':'date',
    }))
    documentNumber = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class':'form-control form-control-sm',
        'placeholder':'Doc No.'
    }))
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'firstname',
        'data-target':'#LoansReceivable_modal2',
        'data-toggle':'modal',
        'id':'lr_borrower_fname',
    }))
    middlename = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'middlename',
        'data-target':'#LoansReceivable_modal2',
        'data-toggle':'modal',
        'id':'lr_borrower_mname',
    }))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'lastname',
        'data-target':'#LoansReceivable_modal2',
        'data-toggle':'modal',
        'id':'lr_borrower_lname',
    }))
    amountApplied = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Amount Applied',
    }))
    loanType = forms.ChoiceField(
        choices=[
            ['regular','Regular loan'],
            ['business','Business loan'],
            ['educational','Educational loan'],
            ['petty cash','Petty cash loan']
        ], widget=forms.Select(attrs={
            'class':'form-control',
            'id':'lr_ltype',
        }))
    modeOfPayment = forms.ChoiceField(
        choices=[
            ['monthly','monthly'],
            ['semi-monthly','semi-monthly'],
            ['weekly','weekly'],
            ['daily','daily']
        ], widget=forms.Select(attrs={
            'class':'form-control',
        }))
    termsOfPaymentYear = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Years',
    }))
    termsOfPaymentMonth = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Months',
    }))
    termsOfPaymentDay = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Days',
    }))
    interestRate = forms.DecimalField(max_digits=4, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Rate Of Interest',
    }))
    methodOfInterest = forms.ChoiceField(
        choices=[
            ['deminishing','Deminishing'],
            ['straight','Straight line']
        ], widget=forms.Select(attrs={
            'class':'form-control',
        }))
    serviceFee = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Service Fee',
    }))
    penaltyRate = forms.DecimalField(max_digits=4, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Rate of Penalty',
    }))

    def __str__(self):
        return 'Loans Receivable'


class LoanPaymentForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control form-control-sm',
        'type':'date',
    }))
    documentNumber = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control form-control-sm',
        'placeholder':'Doc No.'
    }))
    # firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    #     'class':'form-control',
    #     'placeholder':'firstname',
    #     'data-target':'#LoansReceivable_modal',
    #     'data-toggle':'modal',
    #     'id':'lp_borrower_fname',
    #     'visibility','hidden',
    # }))
    # middlename = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    #     'class':'form-control',
    #     'placeholder':'middlename',
    #     'data-target':'#LoansReceivable_modal',
    #     'data-toggle':'modal',
    #     'id':'lp_borrower_mname',
    #     'visibility','hidden',
    # }))
    # lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
    #     'class':'form-control',
    #     'placeholder':'lastname',
    #     'data-target':'#LoansReceivable_modal',
    #     'data-toggle':'modal',
    #     'id':'lp_borrower_lname',
    #     'visibility','hidden',
    # }))
    paymentAmount = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Amount of Payment',
    }))
    # loanType = forms.ChoiceField(
    #     choices=[
    #         ['regular','Regular loan'],
    #         ['business','Business loan'],
    #         ['educational','Educational loan'],
    #         ['petty cash','Petty cash loan']
    #     ], widget=forms.Select(attrs={
    #         'class':'form-control',
    #         'visibility','hidden',
    #     }))

    def __str__(self):
        return 'Loan Payment'
