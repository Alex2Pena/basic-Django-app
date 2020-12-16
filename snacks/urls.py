from django.urls import path
# 3. Import the necessary Classes from views
from .views import HomePageView, AboutPageView


# Make some modules to connect them to a path
urlpatterns = [
    # '' designates the route for the home page
    path('', HomePageView.as_view(), name="home"),
    # this is the route for the About page
    path('about/', AboutPageView.as_view(), name='about')
]
