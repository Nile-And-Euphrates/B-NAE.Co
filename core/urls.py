"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path  , include
from Products import views
from rest_framework.routers import  DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

# router = DefaultRouter()
# router.register("product",views.viewsets_product)

urlpatterns = [
    path('admin/', admin.site.urls),

    # path("django/jsonresponsenomodel/",views.no_rest_no_model),

    # path("django/jsonresponsefrommodel/",views.no_rest_from_model),

    # path("restframework/fbvlist/",views.FBV_List),
    # path("restframework/fbvlist/<int:id>",views.FBV_id),

    # path("restframework/cbv",views.CBV_List.as_view()),
    # path("restframework/cbv/<int:id>",views.CBV_Id.as_view()),

    # path("restframework/mixins/",views.mixins_List.as_view()),
    # path("restframework/mixins/<int:id>",views.mixins_id.as_view()),

    path("restframework/generics/",views.generics_list.as_view()),
    path("restframework/generics/<int:pk>",views.generics_id.as_view()),

    # path("restframework/viewset/",include(router.urls)),

    #token 
    path("api-token-auth",obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)