from django.contrib import admin
from .models import Jobs, JobDetail,JobFunctions,Location,Industries,Type,JbImage
# Register your models here.
admin.site.register(Jobs)
admin.site.register(JobDetail)
admin.site.register(JobFunctions)
admin.site.register(Location)
admin.site.register(Type)
admin.site.register(Industries)
admin.site.register(JbImage)