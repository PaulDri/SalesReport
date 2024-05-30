from django.shortcuts import render
from rest_framework import generics, status
from .serializers import SalesSerializer
from .models import SalesReport

# Create your views here.


#FOR SALES REPORT VIEW
class getSalesReport(generics.ListAPIView):
    serializer_class = SalesSerializer

    def get_queryset(self):
        queryset = SalesReport.objects.all()


        #For Filtering Reports by Product Category
        getProductCategory = self.request.query_params.get('getProductCategory', None)

        if getProductCategory is not None:
            queryset = queryset.filter(product_category = getProductCategory)
            return queryset
        

        #For Filtering Report by Date Month 
        getMonthOrder = self.request.query_params.get('getMonthOrder', None)

        if getMonthOrder is not None:
            months = {
                'January': 1, 'February': 2, 'March': 3, 'April': 4,'May': 5, 'June': 6,
                'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11,
                'December': 12

            }
        
        return queryset

#For creating data
class createSalesReport(generics.CreateAPIView):
    serializer_class = SalesSerializer
    queryset = SalesReport.objects.all()

# #For deleting, updating data
class modifySalesReport(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SalesSerializer
    queryset = SalesReport.objects.all()
    lookup_field = 'pk'


# #FOR INVENTORY REPORT VIEW
# class getInventoryReport(generics.ListAPIView):
#     serializer_class = InventorySerializer
#     def get_queryset(self):
#         queryset = InventoryReport.objects.all()


#         #For Filtering Item Age
#         getItemAge = self.request.query_params.get('getItemAge', None)

#         if getItemAge is not None:
#             queryset = queryset.filter(item_age=getItemAge)
#             return queryset
        
#         #For Filtering Low Stock Items
#         getLowStock = self.request.query_params.get('getLowStock', None)
        
#         if getLowStock is not None:
#             queryset = queryset.filter(low_stock=getLowStock)
#             return queryset
        
#         #For Filtering Dead Stock Items
#         getDeadStock = self.request.query_params.get('getDeadStock', None)

#         if getDeadStock is not None:
#             queryset = queryset.filter(dead_stock=getDeadStock)
#             return queryset
