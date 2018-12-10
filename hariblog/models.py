from django.db import models

class Theme(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book theme (e.g. Agriculture Policy, Food Security)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese, Nepali etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


from django.urls import reverse

class Blogs(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    content = models.TextField(max_length=10000, help_text='Please write your blog content here.., maximum 10000 words')
    #blog_id = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    theme = models.ManyToManyField(Theme, help_text='Select a theme for this post')
    post_date = models.DateField(auto_now_add=True)
    comments = models.TextField(max_length=1000, blank=True)
    comment_count = models.IntegerField(null=True, blank=True)
    comment_ornot = models.BooleanField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    dislikes = models.IntegerField(null=True, blank=True)
    shared = models.BooleanField(null=True, blank=True)
    shared_freq = models.IntegerField(null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('blog-detail', args=[str(self.id)])

    def display_theme(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(theme.name for theme in self.theme.all()[:3])

    display_theme.short_description = 'Theme'

import uuid # Required for unique book instances

class BlogInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular blog across all Blogs')
    blog = models.ForeignKey('Blogs', on_delete=models.SET_NULL, null=True)
    comment_ornot = models.BooleanField(null=True)
    post_date = models.DateField(auto_now_add=True)
    no_of_shares = models.IntegerField(null=True, blank=True)
    post_date = models.IntegerField(null=True, blank=True)
    no_of_dislikes = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.blogs.title})'

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_register = models.DateField('Registered', null=True, blank=True)
    email_address = models.EmailField(max_length=254)
    no_of_blog_posts = models.IntegerField(null=True, blank=True)


    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

