# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url
# from . import views
# from django.conf.urls.static import static
# from django.conf import settings
#
# app_name = 'hello'
#
# urlpatterns = [
#     url(r'^upload', views.uploadImg),
#     url(r'^show', views.showImg),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print("qiulongquan_static_MEDIA_URL={}".format(settings.MEDIA_URL))
# print("qiulongquan_static_MEDIA_ROOT={}".format(settings.MEDIA_ROOT))
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 这句话是用来指定和映射静态文件的路径


from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'hello'


urlpatterns = [
path('admin/', admin.site.urls),
url(r'^upload', views.uploadImg),
url(r'^show', views.showImg),
]