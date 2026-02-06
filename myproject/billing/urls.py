from django.urls import path
from .views import predict_cost_view, dashboard_view,home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("predict-cost/", predict_cost_view, name="predict_cost"),
    path("dashboard/", dashboard_view, name="dashboard"),
]
