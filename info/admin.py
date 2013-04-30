#-*- coding:utf-8-*-
from django.contrib import admin

import models



class InfoAdmin(admin.ModelAdmin):
    #exclude=['posted']
    readonly_fields=('posted',)
    prepopulated_fields = {'slug':('title',)}
    list_display = ('slug',)



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class LeadersAdmin(admin.ModelAdmin):
    list_display = ('name','email','get_name')
    def get_name(self,obj):
        return obj.name
    get_name.verbose_name = '姓名'
class MembersAdmin(admin.ModelAdmin):
    pass
class GraduateAdmin(admin.ModelAdmin):
    pass
class DeviceAdmin(admin.ModelAdmin):
    pass
class LibNoticeAdmin(admin.ModelAdmin):
    pass
class ResearchDirectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Info,InfoAdmin)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.Leaders,LeadersAdmin)
admin.site.register(models.Members,MembersAdmin)
admin.site.register(models.Graduate,GraduateAdmin)
admin.site.register(models.Device,DeviceAdmin)
admin.site.register(models.LibNotice,LibNoticeAdmin)
admin.site.register(models.ResearchDirection,ResearchDirectionAdmin)
admin.site.register(models.Contact)



