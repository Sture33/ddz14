from django.contrib import admin

from lesson14app.models import Feedback, Tag

# Register your models here.
admin.site.register(Feedback)
admin.site.register(Tag)