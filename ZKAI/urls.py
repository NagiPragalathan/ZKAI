# from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls.static import static
from ZKAI import settings
from base.views import video_feed,home,Test_home,report
urlpatterns = [
    path('video_feed', video_feed, name='video_feed'),
    path('home', home, name='home'),
    path('test_home', Test_home, name='test_home'),
    # path('show_images', show_images, name='show_images'),
    path('report/<int:total_question>/<int:total_mark>', report, name='report'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
