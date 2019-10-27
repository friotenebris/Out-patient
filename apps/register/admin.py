from django.contrib import admin

# Register your models here.
from apps.register.models import User,Nurse,Appointment,Administrator,Patient,Test,Diseases,Doctor
admin.site.register(User )
admin.site.register(Nurse )
admin.site.register(Appointment )
admin.site.register(Administrator )
admin.site.register(Patient )
admin.site.register(Test )
admin.site.register(Diseases )
admin.site.register(Doctor )
