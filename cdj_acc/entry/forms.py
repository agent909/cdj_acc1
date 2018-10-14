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
        'placeholder':'Loanee',
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
    loanee = forms.CharField(max_length=180, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Debtor',
        'data-target':'#LoansReceivable_loanee_names_modal',
        'data-toggle':'modal',
        'id':'ar_debtor_name',
    }))
    loanAmount = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Loan Amount',
    }))
    loanType = forms.ChoiceField(
        choices=[
            ['regular','Regular loan'],
            ['business','Business loan'],
            ['educational','Educational loan'],
            ['petty cash','Petty cash loan']
        ], widget=forms.Select(attrs={
            'class':'form-control',
        }))
    termsOfPayment = forms.ChoiceField(
        choices=[
            ['monthly','monthly'],
            ['semi-monthly','semi-monthly'],
            ['weekly','weekly']
        ], widget=forms.Select(attrs={
            'class':'form-control',
        }))
    modeOfPayment = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'No. of Years',
    }))
    interestRate = forms.DecimalField(max_digits=4, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Interest Rate',
    }))
    methodOfInterest = forms.ChoiceField(
        choices=[
            ['deminishing','Deminishing'],
            ['flat','Flat']
        ], widget=forms.Select(attrs={
            'class':'form-control',
        }))
    serviceFee = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Service Fee',
    }))
    penaltyRate = forms.DecimalField(max_digits=4, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Penalty Rate',
    }))

    def __str__(self):
        return 'Loans Receivable'

    # RESERVED FOR INVENTORY FEATURE
    
    # item = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
    #     'class':'form-control',
    #     'name':'item_name',
    #     'id':'TESTid2', #TRACE THIS ONE and change the ID
    #     'placeholder':'Item',
    # }))
    # quantity = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
    #     'class':'form-control',
    #     'name':'quantity',
    #     'placeholder':'Quanity'
    # }))
    # price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
    #     'class':'form-control',
    #     'name':'price',
    #     'palceholder':'Price',
    # }))

