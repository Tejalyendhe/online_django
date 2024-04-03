from django.urls import path,include
from .views import UserRecordView
from . import views,supplier
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', UserRecordView.as_view(), name='users'),
    path('add_product_type/', views.add_product_type, name='add_product_type'),
    path('add_cipher/', views.add_cipher, name='add_cipher'),
    path('add_calculation/', views.add_calculation, name='add_calculation'),
    path('delete_product_type/', views.delete_product_type, name='delete_product_type'),
    path('delete_cipher/', views.delete_cipher, name='delete_cipher'),
    path('delete_calculation/', views.delete_calculation, name='delete_calculation'),
    #------------ supplier ----------------
    path('add_product/', supplier.add_product, name='add_product'),
    path('get_product_supplier/', supplier.get_product_supplier, name='get_product_supplier'),
    path('delete_product/', supplier.delete_product, name='delete_product'),
    path('delete_image/', supplier.delete_image, name='delete_image'),
    path('get_image/', supplier.get_image, name='get_image'),
    

]
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)