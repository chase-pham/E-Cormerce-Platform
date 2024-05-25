# shop/urls.py
urlpatterns = [
    path('register/', views.register, name='register'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/review/', views.add_review, name='add_review'),
    path('profile/', views.profile, name='profile'),
    path('checkout/', views.checkout, name='checkout'),
    path('apply-discount/', views.apply_discount, name='apply_discount'),
        path('products/<int:product_id>/upload-image/', views.upload_product_image, name='upload_product_image'),
]
