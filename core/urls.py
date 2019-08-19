from django.conf.urls import url
from . views import CategoryItemList, ArticleDetailView, CartSummaryView, HomeView
from . import views

urlpatterns = [
    url('^$', HomeView.as_view() , name='index'),
    url('^article-category/(?P<pk>\d+)/$', CategoryItemList.as_view() , name='article'),
    url('^article-detail/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view() , name='article-detail'),
    url('^user-register/$', views.user_register, name='user-register'),
    url('^user-login/$', views.user_login, name='user-login'),
    url('^user-log-out/$', views.user_log_out, name='user-log-out'),
    url('add-to-cart/(?P<slug>[-\w]+)/$', views.add_to_cart, name='add-to-cart'),
    url('^cart-summary-view/$', CartSummaryView.as_view(), name='cart-summary-view'),
    url('remove-item-from-cart/(?P<slug>[-\w]+)/$', views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
    url('add-single-item-from-cart/(?P<slug>[-\w]+)/$', views.add_single_item_from_cart, name='add-single-item-from-cart'),
    url('remove-from-cart/(?P<slug>[-\w]+)/$', views.remove_from_cart, name='remove-from-cart'),

    url('^shop/$', views.shop, name='shop'),
    url('^contact-us/$', views.contact_us, name='contact-us'),
    url('^product-details/$', views.product_details, name='product-details'),
    url('^login/$', views.login, name='login'),
    url('^checkout/$', views.checkout, name='checkout'),
    # url('^cart/$', views.cart, name='cart'),
    url('^blog-single/$', views.blog_single, name='blog-single'),
    url('^blog/$', views.blog, name='blog'),
    url('^404/$', views.page_not_found, name='404'),

]
