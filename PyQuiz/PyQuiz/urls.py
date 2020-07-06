from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quizzes/', include('quizzes.urls')),
    path('users/', include('users.urls'))
]
