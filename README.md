# Try Django



## Creating the virtual env (GETTING STARTED)

1. python -m venv venv - create the virtual environment
2. source venv/scripts/activate - activate the virtual environment
3. python -m django --version - check the django version
4. django-admin startproject django_project - create the django project

5. python manage.py runserver - run server python manage.py migrate
6. python manage.py createsuperuser - to access the backend creating superuser

7. python manage.py startapp blog - create a app

## Step 1 (summary: setup and basic routing) (APPLICATION AND ROUTES)

1. create the virtual environment, create project , create app
2. learn routing -> main route -> app route -> views (request)->HttpRespose()

## Step 2 Templates to return more complex code (TEMPLATES)

1. blog/templates/blog/template.html
2. adding 'blog.apps.Blog_Config' -> settings.py
3. Rendering Tempates:

=>> return render(request, 'blog/home.html')

=>> return HttpResponse('html content')

#### Rendering the data to template

      /blog/views.py
      posts = [
         {
            'author': 'Milan KC',
            'title': 'Blog Post 1',
            'content': 'First Post Content',
            'date_posted': 'August 27, 2018'
         },
         {
            'author': 'Eliza Shahi',
            'title': 'Blog Post 2',
            'content': 'Second Post Content',
            'date_posted': 'January 21, 2022'
         },
      ]


      def home(request):
         context = {
            'posts': posts,
         }
         return render(request, 'blog/home.html', context)


      /templates/blog/home.html

      {% for post in posts %}

      <h1>{{post.title}}</h1>
      <p>By {{post.author}} on {{post.date_posted}}</p>
      <p>{{post.content}}</p>

      {% endfor %}

#### Dynamic Title and template inheritance

    {% if title %}
    <title>Django Blog - {{title}}</title>
    {% else %}
    <title>Django Blog</title>
    {% endif %}

{% extends 'blog/base.html' %}

{% block content %} {% for post in posts %}

         <h1>{{post.title}}</h1>
         <p>By {{post.author}} on {{post.date_posted}}</p>
         <p>{{post.content}}</p>

      {% endfor %}

{% endblock content %}

#### Loading the Static file

static/blog/main.css

blog/base.html {% comment %} Custom CSS {% endcomment %}

<link rel="stylesheet" href="{% static 'blog/main.css'%}" />

## Step 3: Django Admin

1. python manage.py migrations
2. python manage.py createsuperuser
3. login: /admin

## Step 4: Database and Migrations (Django ORM)

1. Create a model (logical db)

class Post(models.Model): title = models.CharField(max_length=100) content =
models.TextField() date_posted = models.DateTimeField(default=timezone.now)
author = models.ForeignKey(User, on_delete=models.CASCADE)

2. python manage.py makemigrations
3. To see the sql commands : python manage.py sqlmigrate blog 0001
4. python manage.py migrate

### WE can directly communicate with db using terminal: python manage.py shell => thanks to django ORM

#### Post.objects.all(), Post.objects.get(id=1), Post.objects.filter(username="username"), Post.objects.first() or last()

#### post_1 = Post(title="Blog 1", content="First Blog Post", author=user)

#### post_1.save()

### Read from db

#### Post.objects.all(), Post.objects.get(id=1), Post.objects.filter(username="username"), Post.objects.first() or last()

#### user.post_set.all(), user.modelname_set.all()

<p> from blog.models import Post from django.contrib.auth.models import User</p>
<p> User.objects.all() User.objects.first() User.objects.last()</p>
<p> User.objects.filter(username="milankc4860@gmail.com")</p>
<p> User.objects.filter(username="milankc4860@gmail.com").first()</p>
<p> user.pk user = User.objects.get(id=1)</p>

### Create to db

#### vpost_1 = Post(title="Blog 1", content="First Blog Post", author=user)

#### post_1.save()

#### user.post_set.create(title="Blog 3", content="Third Post Content")

<p>Post.objects.all() user = User.objects.get(id=1) user <User:
milankc4860@gmail.com> user.id 1 user.username 'milankc4860@gmail.com' </p>
<p>user.password</p>
<p>Post.objects.all() <QuerySet []> post_1 = Post(title="Blog 1",</p>
<p>content="First Blog Post", author=user) Post.objects.all() <QuerySet []></p>

<QuerySet [<User: milankc4860@gmail.com>, <User: TestUser>]>

### Using the db:quering the db

def home(request):
   context = { 'posts': Post.objects.all(), } 
   return render(request, 'blog/home.html', context)

##### Materials from

1. Corey Schafer's Django series: Corey Schafer's tutorials are well-explained
   and comprehensive, making them perfect for beginners. He covers everything
   from setting up the development environment to deploying a Django
   application.

2. JustDjango: This channel has a wide range of tutorials on Django, from
   beginner to advanced topics. They also have tutorials on integrating Django
   with other technologies such as React.

3. Traversy Media: Brad Traversy's tutorials are clear and easy to follow. He
   has a number of tutorials on Django, including building a REST API,
   integrating with Vue.js, and more.
