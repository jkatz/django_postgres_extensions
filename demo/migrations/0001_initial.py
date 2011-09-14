# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Map'
        db.create_table('demo_map', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('geocode', self.gf('ext.models.PointField')()),
        ))
        db.send_create_signal('demo', ['Map'])

        # Adding model 'Lotto'
        db.create_table('demo_lotto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('numbers', self.gf('ext.models.IntegerArrayField')(null=True, blank=True)),
        ))
        db.send_create_signal('demo', ['Lotto'])

        # Adding model 'Subscription'
        db.create_table('demo_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('period', self.gf('ext.models.DayIntervalField')()),
            ('price', self.gf('ext.models.MoneyField')(null=True, blank=True)),
        ))
        db.send_create_signal('demo', ['Subscription'])


    def backwards(self, orm):
        
        # Deleting model 'Map'
        db.delete_table('demo_map')

        # Deleting model 'Lotto'
        db.delete_table('demo_lotto')

        # Deleting model 'Subscription'
        db.delete_table('demo_subscription')


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
        'demo.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'period': ('ext.models.DayIntervalField', [], {}),
            'price': ('ext.models.MoneyField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['demo']
