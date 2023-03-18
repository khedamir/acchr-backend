from django.contrib import admin

# Register your models here.
from accounts_chamber.models import Employee, File, Document, PageHTML, Posts

admin.site.register(Employee)
admin.site.register(File)
admin.site.register(Document)
admin.site.register(PageHTML)
admin.site.register(Posts)
