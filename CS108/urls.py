from django.urls import path
from .views import HomePageView, QuotePageView, RandomQuotePageView

urlpatterns = [
    # map URL to the view
    path('', RandomQuotePAgeView.as_view(), name="random")
    path('all', HomePageView.as_view(), name='home'),
    path('quote/<int:pk'>, QuotePageView.as_view(), name='quote'),
    path('person/<int:pk>', QuotePageView.as_view(), name='quote'),
    path('create', CreateQuoteView.as_view(), name='create'),
]    
