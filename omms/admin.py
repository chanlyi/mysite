from django.contrib import admin
from omms.models import *


# Register your models here.


class SightInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'phone', 'needpost',
                    'diopter', 'corrected_sight', 'eye_mid_distance',
                    'optometist', 'newdate')  # 把字段信息全部显示出来
    list_display_links = ('name',)
    search_fields = ('name', 'optometist', 'address', 'glass_frame_type',
                     'glass_lens_type',)  # 添加search bar，在指定的字段中search
    fields = ('name', 'gender', 'age', 'address', 'phone', 'needpost', 'diopter', 'corrected_sight', 'glass_frame_type',
              'glass_lens_type',
              'eye_mid_distance', 'optometist', 'comment', 'newdate', 'uptime')
    list_filter = ('newdate', 'gender', 'optometist', 'needpost', 'glass_frame_type',
                   'glass_lens_type',)


admin.site.register(SightInfo, SightInfoAdmin)
