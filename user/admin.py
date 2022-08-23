from django.contrib import admin
from .models import *

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'main_work', 'phone_number', 'level')

    @admin.display(description='Level')
    def level(self, obj):
        if 2022 - obj.experience.year > 3:
            result = 'middle'
        if 2022 - obj.experience.year < 3:
            result = 'strong_junior'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('language', 'mentor')
    list_display = ('name', 'language', 'date_started', 'mentor', 'student',)
    search_fields = ('mentor', 'student',)



admin.site.register(Language)
admin.site.register(Student)




