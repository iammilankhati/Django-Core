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

### Write to db

#### vpost_1 = Post(title="Blog 1", content="First Blog Post", author=user)

#### post_1.save()

#### user.post_set.create(title="Blog 3", content="Third Post Content")

<p>Post.objects.all() user = User.objects.get(id=1) user <User:
milankc4860@gmail.com> user.id 1 user.username 'milankc4860@gmail.com' </p>
<p>user.password</p>
<p>Post.objects.all() 
</p>
<p>post_1 = Post(title="Blog 1" ,content="First Blog Post", author=user) Post.objects.all() <QuerySet []> (exit and relogin to get the data)</p>

### Using db in views

def home(request): context = { 'posts': Post.objects.all(), } return
render(request, 'blog/home.html', context)

## STEP 5 FORMS

#### Default form in django

from django.contrib.auth.forms import UserCreationForm

//users/views.py def register(request): if request.method == 'POST': form =
UserCreationForm(request.POST) if form.is_valid(): username =
form.cleaned_data.get('username') messages.success(request, f'Account created
for {username}!') return redirect('blog-home') else: form = UserCreationForm()
return render(request, 'users/register.html', { "form": form, })

//users/templates/users/register.py {% extends 'blog/base.html' %}
{% extends 'blog/base.html' %} 
{% load crispy_forms_tags %}
{% block content %}
<div class="content-section">
    <form action="" method="POST">
        {% csrf_token %}
        <fieldset class="form-group">
            <legend class="border-bottom mb-4"> Join Today</legend>
            {{form|crispy}}
        </fieldset>
        <div class="form-group">
            <button class="btn btn-outline-info" type="submit">Sign Up</button>
        </div>
    </form>

    <div class="border-top pt-3 mt-4">
        <small class="text-muted">Already Have An Account ?
            <a href="#" class="ms-2">Sign In</a>
        </small>

    </div>
</div>
{% endblock content %}

//blog/base.html for alert message 
   {% if messages %}
      {% for message in messages %}
      <div class="alert alert-{{message.tags}}">{{message}}</div> {% endfor %}
   {% endif %}

//custom forms
class UserRegistrationForm(UserCreationForm):
    email: forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


### issues for crispy template doesn't exist for styling

      I also ran to this problem but crispy-form is already supporting boostrap 5. In their github page was instructed as so

      $ pip install django-crispy-forms

      $ pip install crispy-bootstrap5
      And in settings.py

      INSTALLED_APPS = [
      ...,
      'crispy_forms',
      'crispy_bootstrap5',  # Forgetting this was probably your error
      ]
      And then at the bottom of the page of settings.py

      CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
      CRISPY_TEMPLATE_PACK = "bootstrap5"
      This worked for me solving the TemplateDoesNotExist error. No need to downgrade to bootstrap4


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
