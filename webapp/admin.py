from django.contrib import admin
from .models import Course,FeedbackData
class CourseAdmin(admin.ModelAdmin):
    list_display = ('Course_id','Course_name','Faculty','Duration','course_content')
class FedbackAdmin(admin.ModelAdmin):
    list_display = ['name','rating','feedback']
admin.site.register(Course,CourseAdmin)
admin.site.register(FeedbackData,FedbackAdmin)
