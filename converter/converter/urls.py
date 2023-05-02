
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('dwgtotxt/', include('dwgtotxt.urls')),
    path('admin/', admin.site.urls),
]
