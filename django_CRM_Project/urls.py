"""django_CRM_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# load static file
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page,header,footer
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from Organization.views import OrganizationViewSetAPI

router = DefaultRouter()
router.register('organization', OrganizationViewSetAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page,name="homepage"),
    path('header', header, name="header"),
    path('footer', footer, name="footer"),
    path('', include('user_accounts.urls')),
    path('', include('product.urls')),
    path('', include('organization.urls')),
    path('', include('quote.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),

]



# Static File Setting
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # python manage.py collectstatic

    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)