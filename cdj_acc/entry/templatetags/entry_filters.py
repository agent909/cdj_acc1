from django import template
from entry.models import Accounts

register = template.Library()


@register.filter
def get_account(value, accountId):
    # print(accounts)
    return Accounts.objects.get(pk=accountId)


@register.filter
def get_form(value, accountId):
    current_form = Accounts.objects.get(pk=accountId).name.lower()    
    return current_form.replace(" ","_")


@register.filter
def get_formname(value, mode):
    if(mode==1):
        return value.replace("_"," ").upper()
    else:
        return value.replace(" ","_").upper()

@register.filter
def to_upper(value):
    return value.upper()

@register.filter
def replace_x_with(value, mycharacter):
    mycharacter=mycharacter.split(",")
    return value.replace(mycharacter[0],mycharacter[1])