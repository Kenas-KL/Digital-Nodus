from django.urls import path
from .views import index, list_events, register, detail_event, about


urlpatterns = [
    path('', index, name="index"),
    path('register', register, name='register'),
    path('list_events', list_events, name="list_events"),
    path('detail_event/<int:pk>/community', detail_event, name="detail_event"),
    path('about-community', about,  name="about")
]