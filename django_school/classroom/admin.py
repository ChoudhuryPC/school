from django.contrib import admin
from classroom.models import (Student,
                              Subject, User,Quiz,Answer)

# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(User)
admin.site.register(Answer)
admin.site.register(Quiz)

