from django import forms
import re

# list of custom fields that are tied to custom form elements.

class IntegerArrayField(forms.Field):

    def __init__(self, **kwargs):
        super(IntegerArrayField, self).__init__(**kwargs)

    def prepare_value(self, value):
        if isinstance(value, list):
            return re.sub(r'\[|\]', '', str(value))
        return value

    def validate(self, value):
        super(IntegerArrayField, self).validate(value)
        if not re.search('^[\s,0-9]*$', value):
            raise forms.ValidationError, "Please use only integers in your data"

class MoneyField(forms.Field):

    def __init__(self, **kwargs):
        super(MoneyField, self).__init__(**kwargs)

    def clean(self, value):
        value = re.sub(',|\$', '', value)
        return super(MoneyField, self).clean(value)

    def validate(self, value):
        super(MoneyField, self).validate(value)
        value = re.sub(',|\$', '', value)
        if not re.search('^[1-9][0-9]*(\.[0-9]{2})?$', value):
            raise forms.ValidationError, "Please enter in a proper money format (99 or 99.99)"