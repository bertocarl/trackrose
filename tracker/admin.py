from django.contrib import admin
from .models import User, Image, Attendance

#Registration of admin sites

admin.site.register(User)
admin.site.register(Image)
admin.site.register(Attendance)