"""
URL configuration for pdfexactor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from pdfapp import views
from pdfapp.views import ExtractPDFData ,PDFExtractAPIView
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API Title",
#         default_version='v1',
#         description="Your API description",
#     ),
#     public=True,
# )

# urlpatterns = [
#     # ... other URL patterns
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('swagger/', swagger_views.get_swagger_view(title='Your API Title'), name='schema-swagger-ui'),
    path('extract_pdf/', views.extract_pdf_text, name='extract_pdf'),
    path('ext/', views.extract_pdf_data, name='extract_pdf'),
    path('ext2/', views.extract_key_value_pairs, name='extract_pdf2'),
    path('ext3/', ExtractPDFData.as_view(), name='extract_pdf3'),
    path('ext4/', PDFExtractAPIView.as_view(), name='extract_pdf4'),

    
]
