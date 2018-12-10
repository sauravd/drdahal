from django.shortcuts import render

from hariblog.models import Blogs, Author, BlogInstance, Theme, Language

from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blogs.objects.all().count()
    num_instances = BlogInstance.objects.all().count()



    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_blogs': num_blogs,
        'num_instances': num_instances,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'drharidahalindex.html', context=context)



def blogs(request):

 	return render(request, 'hariblog_list.html')

class BlogListView(generic.ListView):
   model = Blogs
   context_object_name = 'drdahal_blogs_list'
   queryset = Blogs.objects.all()[:5]
   template_name ='hariblog/hariblog_list.html'

class BlogDetailView(generic.DetailView):
    """docstring for BlogDetailView"""
    model = Blogs




def contactme(request):

    return render(request, 'drharidahalcontactme')
