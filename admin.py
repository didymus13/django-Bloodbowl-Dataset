from django.contrib import admin
from models import *

class Skills_Inline(admin.TabularInline):
	model = Skill
	extra = 1
	
class Skill_Group_Admin(admin.ModelAdmin):
	inlines = [Skills_Inline]

admin.site.register(Skill_Group, Skill_Group_Admin)

class Skill_Admin(admin.ModelAdmin):
	pass
admin.site.register(Skill, Skill_Admin)

class Positions_Inline(admin.TabularInline):
	model = Position
	extra = 1
	filter_horizontal = ('skills',)

class Race_Admin(admin.ModelAdmin):
	inlines = [Positions_Inline]

admin.site.register(Race, Race_Admin)

