# super-pancake
Django Rest Framework Serialization
tutorial: https://www.django-rest-framework.org/tutorial/1-serialization/

lib pygments: we'll be using this for the code highlighting

# Working with Serializers

link: https://www.django-rest-framework.org/tutorial/1-serialization/#working-with-serializers

- python manage.py shell

    
    from snippets.models import Snippet
    from snippets.serializers import SnippetSerializer
    from rest_framework.renderers import JSONRenderer
    from rest_framework.parsers import JSONParser

    snippet = Snippet(code='foo = "bar"\n')
    snippet.save()
    
    snippet = Snippet(code='print("hello, world")\n')
    snippet.save()

    serializer = SnippetSerializer(snippet)
    serializer.data
    # {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
    