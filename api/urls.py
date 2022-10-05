from django.urls import path, include

from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('', CategoriesView)
router.register('subcategory', SubCategoryView)
router.register('product', ProductsView)


urlpatterns = [
    path("", include(router.urls))
]
