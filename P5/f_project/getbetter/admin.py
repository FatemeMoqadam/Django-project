from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import feeling , solution ,solutionsong 




admin.site.register(feeling)
admin.site.register(solution)
admin.site.register(solutionsong)
