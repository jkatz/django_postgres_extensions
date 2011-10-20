# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ParameterLog'
        db.create_table('demo_parameterlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('params', self.gf('ext.models.HstoreField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('demo', ['ParameterLog'])


    def backwards(self, orm):
        
        # Deleting model 'ParameterLog'
        db.delete_table('demo_parameterlog')


    models = {
        'demo.lotto': {
            'Meta': {'object_name': 'Lotto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numbers': ('ext.models.IntegerArrayField', [], {'null': 'True', 'blank': 'True'})
        },
        'demo.map': {
            'Meta': {'object_name': 'Map'},
            'geocode': ('ext.models.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'demo.parameterlog': {
            'Meta': {'object_name': 'ParameterLog'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'params': ('ext.models.HstoreField', [], {'null': 'True', 'blank': 'True'})
        },
        'demo.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'period': ('ext.models.DayIntervalField', [], {}),
            'price': ('ext.models.MoneyField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['demo']
