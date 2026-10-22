from django.contrib import admin
from apps.base.models import Name
# Register your models here.


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age')
    search_fields = ("name",)
    list_filter = ("age",)
    ordering = ("id",)

