from django.db import models
import forms
import re
from south.modelsinspector import add_introspection_rules

# Below are all the custom fields used for DB models
class DayIntervalField(models.Field):
    SECS_IN_DAY = 86400

    description = "time interval"
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(DayIntervalField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'interval'

    def get_prep_value(self, value):
        try:
            value = int(value)
            return "%d %s" % (value, 'days')
        except:
            if re.match(r"days$", value):
                return value
            elif value:
                return "%s %s" % (value, 'days')
            else:
                return None

class EnumField(models.Field):
    """
        generic enumerated type.  have your custom types inherit this
    """
    description = "enumerated type"

    def __init__(self, *args, **kwargs):
        self.enum = kwargs['enum']
        del kwargs['enum']
        super(EnumField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return self.enum

class HstoreField(models.Field):
    description = "Use PostgreSQL hstore "
    __metaclass__ = models.SubfieldBase

    def db_type(self, connection):
        return 'hstore'

    def get_prep_value(self, value):
        if isinstance(value, (str, unicode)):
            pass
        elif isinstance(value, dict):
            values = []
            for key in value.keys():
                values.append('"%s"=>"%s"' % (key, value[key]))

            return ", ".join(values)

    def to_python(self, value):
        if isinstance(value, dict):
            return value
        else:
            value = value.split(',')
            return dict(map(self._hstore_clean, value))

    def _hstore_clean(self, value):
        k, v = value.strip().split('=>')
        k = re.sub('^"|"$', '', k)
        v = re.sub('^"|"$', '', v)
        return [k,v]

class IntegerArrayField(models.Field):
    description = "Use PostgreSQL integer arrays"
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(IntegerArrayField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'integer[]'

    def formfield(self, **kwargs):
        defaults = { 'form_class': forms.IntegerArrayField }
        defaults.update(kwargs)
        return super(IntegerArrayField, self).formfield(**defaults)

    def get_prep_value(self, value):
        if isinstance(value, list):
            db_value = str(value)
            db_value = re.sub(r'\[', '{', db_value)
            db_value = re.sub(r'\]', '}', db_value)
            return db_value
        elif isinstance(value, (str, unicode)):
            if not value: return None
            return value

    def to_python(self, value):
        if isinstance(value, list):
            return value
        elif isinstance(value, (str, unicode)):
            if not value: return None
            value = re.sub(r'\{|\}', '', value).split(',')
            return map(lambda x: int(x), value)

class MoneyField(models.Field):
    description = "Store money in it's proper integer format, but display it as [0-9]+.[0-9]{2} format"
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(MoneyField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'int'

    def formfield(self, **kwargs):
        defaults = { 'form_class': forms.MoneyField }
        defaults.update(kwargs)
        return super(MoneyField, self).formfield(**defaults)

    def get_prep_value(self, value):
        if isinstance(value, (str, unicode)):
            if value:
                value = value.replace(',', '')
                return int(float(value) * 100)
            else:
                return None
        elif isinstance(value, float):
            return int(value * 100)
        elif isinstance(value, (int, long)):
            return value

    def to_python(self, value):
        if isinstance(value, (str, unicode)):
            return value
        elif isinstance(value, float):
            return "%.2f" % value
        elif isinstance(value, (int, long)):
            return "%.2f" % (value / 100.0)

class PointField(models.Field):
    description = "point type"
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(PointField, self).__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'point'

add_introspection_rules([], ["^ext\.models\.DayIntervalField"])
add_introspection_rules([], ["^ext\.models\.EnumField"])
add_introspection_rules([], ["^ext\.models\.HstoreField"])
add_introspection_rules([], ["^ext\.models\.IntegerArrayField"])
add_introspection_rules([], ["^ext\.models\.MoneyField"])
add_introspection_rules([], ["^ext\.models\.PointField"])
