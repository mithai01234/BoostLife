from .views import *
from django.urls import path

urlpatterns = [
	path('backend/partner/add/', partner_add, name='partner_add'),
	path('backend/partners/', partner_list, name='partner_list'),
	path('backend/partner/edit/<str:partner_id>/', partner_edit, name='partner_edit'),
	path('backend/partner/delete/<str:partner_id>/', partner_delete, name='partner_delete'),
	path('backend/partner/view/<str:partner_id>/', partner_view, name='partner_view'),
	path('backend/partner/<int:partner_id>/activate/', activate_partner, name='activate_partner'),
	path('backend/partner/<int:partner_id>/deactivate/', deactivate_partner, name='deactivate_partner'),
	path('backend/add-package/', add_package, name='add_package'),
	path('backend/edit-package/<int:package_id>/', edit_package, name='edit_package'),
	path('backend/delete-package/<int:package_id>/', delete_package, name='delete_package'),
	path('backend/packages/', list_packages, name='package_list'),

	path('backend/add-package/', add_package, name='add_package'),
	path('backend/edit-package/<int:package_id>/', edit_package, name='edit_package'),
	path('backend/delete-package/<int:package_id>/', delete_package, name='delete_package'),

	path('backend/list_of_store/', list_store, name='list_store'),
	path('backend/add-store/', store_add, name='add_store'),
	path('backend/delete-store/<int:store_id>/', delete_store, name='delete_store'),
	path('backend/store/<int:store_id>/activate/', activate_store, name='activate_store'),
	path('backend/store/<int:store_id>/deactivate/', deactivate_store, name='deactivate_store'),
	path('backend/edit-store/<int:store_id>/', edit_store, name='edit_store'),

]
