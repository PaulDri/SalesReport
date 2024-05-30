from django.urls import path
from . import views

urlpatterns = [
    path('salesreport/', views.getSalesReport.as_view()),
    #For Creating Data
    # path('createreport/', views.createSalesReport.as_view()),
    # #For Updating,Deleting Data
    # path('modifyreport/<int:pk>', views.modifySalesReport.as_view())
]