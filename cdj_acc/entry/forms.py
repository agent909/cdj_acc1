from django import forms


class AccountReceivableForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control form-control-sm', 
        'name':'date',
        'type':'date',
        }))
    documentNumber = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class':'form-control form-control-sm',
        'name':'document_number',
        'placeholder':'Doc No.'
    }))
    buyer = forms.CharField(max_length=180, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Solt to',
        'name':'debtor',
    }))
    amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'name':'amount',
        'placeholder':'Amount',
    }))


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

