from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
      	 
	 url(r'^', ListView.as_view(
	 queryset=Post.objects.all().order_by("-created")[:5],
	 template_name="blog.html")),
	 
		url(r'^(?P<pk>\d+)$', DetailView.as_view(
		model=Post,
		template_name="post.html")),
		 
	 url(r'^archives/$', ListView.as_view(
	 queryset=Post.objects.all().order_by("-created"),
	 template_name="achives.html")),
	 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #  url(r'^admin/', include(admin.site.urls)),
)

