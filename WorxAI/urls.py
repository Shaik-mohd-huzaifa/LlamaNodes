from django.urls import path
from WorxAI import views


urlpatterns = [
    path("create-workflow", views.workflow_creation, name="Ask ChatBot"),
    path("use-workflow", views.workflow_execution, name="Executes Workflows"),
    path("signup", views.signup, name="Signs in user"),
    path("get-workflows", views.get_workflows, name="Get Users Workflows"),
]
