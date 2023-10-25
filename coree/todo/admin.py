from django.contrib import admin
from todo.models import *

admin.site.register(Tasks)
admin.site.register(InProgress)
admin.site.register(Complete)

# Register your models here.
