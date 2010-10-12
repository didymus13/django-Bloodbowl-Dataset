from django.db import models

# Create your models here.
class Skill_Group(models.Model):
	name = models.CharField("Skill Group Initial", max_length=1)
	
	def __unicode__(self):
		return self.name

class Skill(models.Model):
	name = models.CharField("Skill Name", max_length=32, unique=True)
	skill_group = models.ForeignKey(Skill_Group)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ('name',)

class Race (models.Model):
	name = models.CharField("Race Team Name", max_length=32)
	use_apoth = models.BooleanField("Apothicary Available for Hire", default=True, help_text="Undead teams can't normally use an apothicary")
	max_rerolls = models.PositiveSmallIntegerField("Maximum Re-rolls", default=8)
	reroll_cost = models.PositiveSmallIntegerField("Basic Reroll Cost", default=50, help_text="000")
	
	class Meta:
		ordering = ['name']
	
	def __unicode__(self):
		return self.name
	
class Position (models.Model):
	race = models.ForeignKey(Race)
	name = models.CharField(max_length=32)
	cost = models.PositiveSmallIntegerField(help_text="k")
	max_qty = models.PositiveSmallIntegerField("Maximum Quantity")
	ma = models.PositiveSmallIntegerField("MA")
	st = models.PositiveSmallIntegerField("ST")
	ag = models.PositiveSmallIntegerField("AG")
	av = models.PositiveSmallIntegerField("AV")
	skills = models.ManyToManyField(Skill, blank=True)
	normal_group = models.ManyToManyField(Skill_Group, related_name='normal_group')
	double_group = models.ManyToManyField(Skill_Group, related_name='double_group')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ['race', '-max_qty', 'name',]