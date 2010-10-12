# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Skill_Group'
        db.create_table('bb_dataset_skill_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('bb_dataset', ['Skill_Group'])

        # Adding model 'Skill'
        db.create_table('bb_dataset_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32, unique=True)),
            ('skill_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bb_dataset.Skill_Group'])),
        ))
        db.send_create_signal('bb_dataset', ['Skill'])

        # Adding model 'Race'
        db.create_table('bb_dataset_race', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('use_apoth', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('max_rerolls', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=8)),
            ('reroll_cost', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=50)),
        ))
        db.send_create_signal('bb_dataset', ['Race'])

        # Adding model 'Position'
        db.create_table('bb_dataset_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('race', self.gf('django.db.models.fields.related.ForeignKey')(related_name='positions', to=orm['bb_dataset.Race'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('cost', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('max_qty', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('ma', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('st', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('ag', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('av', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
        ))
        db.send_create_signal('bb_dataset', ['Position'])

        # Adding M2M table for field skills on 'Position'
        db.create_table('bb_dataset_position_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('position', models.ForeignKey(orm['bb_dataset.position'], null=False)),
            ('skill', models.ForeignKey(orm['bb_dataset.skill'], null=False))
        ))
        db.create_unique('bb_dataset_position_skills', ['position_id', 'skill_id'])

        # Adding M2M table for field normal_group on 'Position'
        db.create_table('bb_dataset_position_normal_group', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('position', models.ForeignKey(orm['bb_dataset.position'], null=False)),
            ('skill_group', models.ForeignKey(orm['bb_dataset.skill_group'], null=False))
        ))
        db.create_unique('bb_dataset_position_normal_group', ['position_id', 'skill_group_id'])

        # Adding M2M table for field double_group on 'Position'
        db.create_table('bb_dataset_position_double_group', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('position', models.ForeignKey(orm['bb_dataset.position'], null=False)),
            ('skill_group', models.ForeignKey(orm['bb_dataset.skill_group'], null=False))
        ))
        db.create_unique('bb_dataset_position_double_group', ['position_id', 'skill_group_id'])


    def backwards(self, orm):
        
        # Deleting model 'Skill_Group'
        db.delete_table('bb_dataset_skill_group')

        # Deleting model 'Skill'
        db.delete_table('bb_dataset_skill')

        # Deleting model 'Race'
        db.delete_table('bb_dataset_race')

        # Deleting model 'Position'
        db.delete_table('bb_dataset_position')

        # Removing M2M table for field skills on 'Position'
        db.delete_table('bb_dataset_position_skills')

        # Removing M2M table for field normal_group on 'Position'
        db.delete_table('bb_dataset_position_normal_group')

        # Removing M2M table for field double_group on 'Position'
        db.delete_table('bb_dataset_position_double_group')


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
