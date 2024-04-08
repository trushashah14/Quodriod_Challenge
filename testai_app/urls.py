from django.urls import path  # Import the path function from django.urls module
from .views import execute_tests  # Import the execute_tests view function from the views module in the current directory

urlpatterns = [
    # Define a URL pattern for the endpoint '/tests/v1/execute' that maps to the execute_tests view function
    path('tests/v1/execute', execute_tests),  
]
