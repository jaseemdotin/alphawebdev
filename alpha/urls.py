"""alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from ALPHAGAD import views

urlpatterns = [
    url('admin/', admin.site.urls),url('^$',views.home,name='home'),
    url('^productadd/',views.alphaproductadd,name='productadd'),
    url('^catadd/',views.catadd,name='catadd'),
    url('^alphasignup/',views.alphasignup,name='signup'),
    url('accounts',include('django.contrib.auth.urls')),
    url('^base/',views.base,name='base'),
    url('^$',views.home),
    url('^adminpage/',views.adminpage,name='adminpage'),
    url('^adminview/',views.adminview,name='adminview'),
    url('^productdview/(?P<pk>.*)/$',views.productdview,name='productdview'),
    url('^view-product/(?P<pk>.*)/$',views.productview,name='productview'),
    url('^profileview/',views.profileview,name='profileview'),
    url('^adminadd/',views.adminadd,name='adminadd'),
    url('^ramspecadd/',views.ramspecadd,name='ramspecadd'),
    url('^lapspecadd/',views.lapspecadd,name='lapspecadd'),
    url('^camspecadd/',views.camspecadd,name='camspecadd'),
    url('^pdf/',views.printpdf,name='pdf'),
]
if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
