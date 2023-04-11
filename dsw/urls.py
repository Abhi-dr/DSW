from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name='index'),
    path('portal/', include('portal.urls')),
    
    path('achievement', include('achievement.urls')),
    # path('activities', include('activities.urls')),
    # path('ncc', include('ncc.urls')),
    # path('sport/', include('sport.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)