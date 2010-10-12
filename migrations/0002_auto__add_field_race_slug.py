# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Race.slug'
        db.add_column('bb_dataset_race', 'slug', self.gf('django.db.models.fields.SlugField')(default='human', max_length=128, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Race.slug'
        db.delete_column('bb_dataset_race', 'slug')


    models = {
        'bb_dataset.position': {
            'Meta': {'ordering': "['race', '-max_qty', 'name']", 'object_name': 'Position'},
            'ag': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'av': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'cost': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'double_group': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'double_group'", 'symmetrical': 'False', 'to': "orm['bb_dataset.Skill_Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ma': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'max_qty': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'normal_group': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'normal_group'", 'symmetrical': 'False', 'to': "orm['bb_dataset.Skill_Group']"}),
            'race': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'positions'", 'to': "orm['bb_dataset.Race']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bb_dataset.Skill']", 'symmetrical': 'False', 'blank': 'True'}),
            'st': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        },
        'bb_dataset.race': {
            'Meta': {'ordering': "['name']", 'object_name': 'Race'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_rerolls': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '8'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'reroll_cost': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128', 'db_index': 'True'}),
            'use_apoth': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'bb_dataset.skill': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Skill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'unique': 'True'}),
            'skill_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bb_dataset.Skill_Group']"})
        },
        'bb_dataset.skill_group': {
            'Meta': {'object_name': 'Skill_Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['bb_dataset']
