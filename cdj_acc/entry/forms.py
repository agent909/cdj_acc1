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
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Amount',
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
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Amount',
    }))

    def __str__(self):
        return 'Sales'



class PaymentToAccountReceivableForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control form-control-sm', 
        'type':'date',
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

