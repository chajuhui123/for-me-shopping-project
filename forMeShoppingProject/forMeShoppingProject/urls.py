from django.contrib import admin
from django.urls import path
from mainApp.views import * #mainApp의 views에서 모든 함수 불러옴
from userApp.views import * #userApp의 views에서 모든 함수 불러옴

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name = "main"),
    path('signup/', signup_view, name = "signup"),
    path('login/', login_view, name = "login"), 
    path('logout/', logout_view, name = "logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)