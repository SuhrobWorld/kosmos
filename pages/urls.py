from django.urls import path
from .views import HomePagesView, AboutPageView, WikiPageView, ContactPageView, PicturePageView

urlpatterns = [
    path('', HomePagesView.as_view(), name='home'),
    path('wiki', WikiPageView.as_view(), name='wiki'),
    path('picture', PicturePageView.as_view(), name='picture'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('about', AboutPageView.as_view(), name='about')
]