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