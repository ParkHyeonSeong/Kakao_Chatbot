from django.contrib import admin
from .models import User,User_Box,User_Bank,Goods

# Register your models here.
# 사용자 정보
admin.site.register(User)
# 사용자 은행 정보
admin.site.register(User_Bank)
# 사용자 창고 정보
admin.site.register(User_Box)
# 재화 정보
admin.site.register(Goods)