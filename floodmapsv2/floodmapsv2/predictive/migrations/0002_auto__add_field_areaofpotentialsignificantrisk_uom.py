# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AreaOfPotentialSignificantRisk.uom'
        db.add_column('predictive_areaofpotentialsignificantrisk', 'uom',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['predictive.UnitOfManagement']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AreaOfPotentialSignificantRisk.uom'
        db.delete_column('predictive_areaofpotentialsignificantrisk', 'uom_id')


    models = {
        'predictive.annualexceedanceprobability': {
            'Meta': {'ordering': "['name']", 'object_name': 'AnnualExceedanceProbability'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.areaofpotentialsignificantrisk': {
            'Meta': {'ordering': "['name']", 'object_name': 'AreaOfPotentialSignificantRisk'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.UnitOfManagement']"})
        },
        'predictive.availability': {
            'Meta': {'ordering': "['name']", 'object_name': 'Availability'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.climate': {
            'Meta': {'ordering': "['name']", 'object_name': 'Climate'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.floodextent': {
            'Meta': {'ordering': "['apsr']", 'object_name': 'FloodExtent'},
            'apsr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.AreaOfPotentialSignificantRisk']"}),
            'availability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Availability']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Scenario']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Status']"}),
            'version_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.VersionType']"})
        },
        'predictive.node': {
            'Meta': {'ordering': "['name']", 'object_name': 'Node'},
            'apsr': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.AreaOfPotentialSignificantRisk']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.nodevalue': {
            'Meta': {'ordering': "['node']", 'object_name': 'NodeValue'},
            'depth': ('django.db.models.fields.FloatField', [], {}),
            'elevation': ('django.db.models.fields.FloatField', [], {}),
            'flow': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Node']"}),
            'scenario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Scenario']"}),
            'velocity': ('django.db.models.fields.FloatField', [], {})
        },
        'predictive.scenario': {
            'Meta': {'ordering': "['name']", 'object_name': 'Scenario'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'aep': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.AnnualExceedanceProbability']"}),
            'climate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Climate']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.Source']"})
        },
        'predictive.source': {
            'Meta': {'ordering': "['name']", 'object_name': 'Source'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.status': {
            'Meta': {'ordering': "['name']", 'object_name': 'Status'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.uncertainty': {
            'Meta': {'ordering': "['extent']", 'object_name': 'Uncertainty'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'extent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.FloodExtent']"}),
            'geometry': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'srid': '2157'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uncertainty_band': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['predictive.UncertaintyBand']"})
        },
        'predictive.uncertaintyband': {
            'Meta': {'ordering': "['name']", 'object_name': 'UncertaintyBand'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'predictive.unitofmanagement': {
            'Meta': {'ordering': "['name']", 'object_name': 'UnitOfManagement'},
            'acronym': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rbd': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'predictive.versiontype': {
            'Meta': {'ordering': "['name']", 'object_name': 'VersionType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['predictive']