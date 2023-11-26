from django.urls import path
from . import views

urlpatterns =[
    # path('', views.product_create_view, name='product-list'),
    # path('<int:pk>/',views.product_detail_view),
    #  path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    #   path('<int:pk>/delete/', views.product_destroy_view),

# mixin api
    # path('<int:pk>/',views.product_mixin_view),
    #  path('',views.product_mixin_view),

# raw
 path('voc/',views.voc_alt_view),
 path('voc/<int:pk>',views.voc_detail),
 path('reading/',views.reading_alt_view),
 path('reading/<int:pk>',views.reading_detail),
 path('writing/',views.writing_alt_view),
 path('writing/<int:pk>',views.writing_detail),
 path('speaking/',views.speaking_alt_view),
 path('speaking/<int:pk>',views.speaking_detail),
 path('listening/',views.listening_alt_view),
 path('listening/<int:pk>',views.listening_detail),
 path('statistic/',views.save_statistic),
 path('statistic/<int:userId>/<int:type>',views.get_statistic),


]


