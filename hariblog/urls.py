from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='drharidahalindex'),
	# path('contactme/', views.contactme.as_view(), name='drharidahalcontactme'),
	path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogs/<int:pk>',views.BlogDetailView.as_view(), name='blog-detail'),
    #path('publications/',views.PublicationListView.as_view(), name='publications'),
    #path('publications/<int:pk>',views.PublicationDetailView.as_view(), name='publications-detail'),
    #path('projects/',views.ProjectListView.as_view(), name='projects'),
    #path('publications/<int:pk>',views.ProjectDetailView.as_view(), name='projects-detail'),
    #path('courses/',views.CourseListView.as_view(), name='course'),
    #path('courses/<int:pk>',views.CourseDetailView.as_view(), name='course-detail'),


]

