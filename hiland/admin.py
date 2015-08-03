from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Person, Student, Gender

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',               {'fields': ['first_name', 'last_name']}),
        ('Contact information', {'fields': ['email_address']}),
	('Date information', {'fields': ['birth_date'], 'classes': ['collapse']}),
    ]

    list_display = ('first_name', 'last_name', 'email_address', 'birth_date')

admin.site.register(Person, PersonAdmin)
admin.site.register(Student)
admin.site.register(Gender)
