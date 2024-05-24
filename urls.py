# shop/urls.py
urlpatterns = [
    path('register/', views.register, name='register'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/review/', views.add_review, name='add_review'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.checkout, name='checkout'),
]
