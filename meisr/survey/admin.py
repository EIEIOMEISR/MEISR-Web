from django.contrib import admin

from .models import *

class FunctionalDomainInline(admin.TabularInline):
	model = FunctionalDomain

class DevelopmentalDomainInline(admin.TabularInline):
	model = DevelopmentalDomain

class OutcomeInline(admin.TabularInline):
	model = Outcome

class QuestionAdmin(admin.ModelAdmin):
	inlines = [FunctionalDomainInline, DevelopmentalDomainInline, OutcomeInline,]
	list_display = [field.name for field in Question._meta.fields]
admin.site.register(Question, QuestionAdmin)
class AnswerAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Answer._meta.fields]
admin.site.register(Answer, AnswerAdmin)
class ChildAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Child._meta.fields]
admin.site.register(Child, ChildAdmin)
class FunctionalDomainAdmin(admin.ModelAdmin):
	list_display = [field.name for field in FunctionalDomain._meta.fields]
admin.site.register(FunctionalDomain, FunctionalDomainAdmin)
class DevelopmentalDomainAdmin(admin.ModelAdmin):
	list_display = [field.name for field in DevelopmentalDomain._meta.fields]
admin.site.register(DevelopmentalDomain, DevelopmentalDomainAdmin)
class OutcomeAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Outcome._meta.fields]
admin.site.register(Outcome, OutcomeAdmin)
class ScoreAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Score._meta.fields]
admin.site.register(Score, ScoreAdmin)
'''
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(FunctionalDomain, FunctionalDomainAdmin)
admin.site.register(DevelopmentalDomain, DevelopmentalDomainAdmin)
admin.site.register(Outcome, OutcomeAdmin)
admin.site.register(Score, ScoreAdmin)'''