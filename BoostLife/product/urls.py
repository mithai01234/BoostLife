from .views import *
from django.urls import path

urlpatterns = [
    path('backend/catagoryapp/', catagory, name="catagoryapp"),
    path('backend/catgoryadd/', catgoryadd, name="catgoryadd"),
    path('backend/catagoryapp/delete_item/<int:myid>/', catdelete_item, name="catagory/delete_item"),
    path('backend/catagoryapp/edit_item/<int:myid>/', catedit_item, name="catagory/edit_item"),
    path('backend/catagoryapp/update_item/<int:myid>/', catupdate_item, name="catagory/update_item"),

    path('backend/productapp/', product, name="productapp"),
    path('backend/productadd/', productadd, name="productadd"),
    path('backend/productapp/delete_item/<int:myid>/', delete_item, name="delete_item"),
    path('backend/productapp/edit_item/<int:myid>/', edit_item, name="edit_item"),
    path('backend/productapp/update_item/<int:myid>/', update_item, name="update_item"),
    path('backend/productapp/view_item/<int:myid>/', view_item, name="view_item"),
    path('backend/productapp/activate_product/<int:product_id>/', activate_product, name='productapp/activate_product'),
    path('backend/productapp/deactivate_product/<int:product_id>/', deactivate_product,
         name='productapp/deactivate_product'),

    path('api/categories/', CatagoryListView.as_view(), name='category-list'),
    path('api/categorywise-products/', ProductListView.as_view(), name='product-list'),
    path('api/product/', ProductListThroughIdView.as_view(), name='product-lists'),

    #http://127.0.0.1:8000/api/categorywise-products/?category_id=2
    path('api/recommended-products/', RecommendedProductListView.as_view(), name='recommended-product-list'),
    path('api/most-popular-products/', MostPopularProductListView.as_view(), name='most-popular-product-list'),
    path('api/goalwise-products/', GoalwiseProductListView.as_view(), name='goalwise-product-list'),
    #http://127.0.0.1:8000/api/goalwise-products/?goal=2

    path('api/categories/five/', CatagoryListViewFive.as_view(), name='category-listFive'),
    path('api/categorywise-products/five/', ProductListViewFive.as_view(), name='product-listFive'),
    # http://127.0.0.1:8000/api/categorywise-products/?category_id=2
    path('api/recommended-products/five/', RecommendedProductListViewFive.as_view(), name='recommended-product-listFive'),
    path('api/most-popular-products/five/', MostPopularProductListViewFive.as_view(), name='most-popular-product-listFive'),
    path('api/goalwise-products/four/', GoalwiseProductListViewFive.as_view(), name='goalwise-product-listFive'),

    path('backend/inventory_list/', stock, name="stock"),
    path('backend/stock/edit_item/<int:myid>/', edit_stock, name="edit_stock"),
    path('backend/stock/update_item/<int:stock_id>/', update_stock, name="update_stock"),
    path('backend/stock/update/', update_all_stock, name='update_all_stock'),
    path('backend/stock/all_edit_item/', allstock, name="allstock"),


]