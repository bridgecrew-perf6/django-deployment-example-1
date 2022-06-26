from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

'''
We create a view inside view.py.
Each view must return HttpResponse object. Here, it just returns a string object.
In order to see this view while running server, we need to map this view to url.py file.ff
'''


def index(request):
    # my_dict = {'insert_me': "Hello I am from first_app/index.html and not directly from views.py! "}
    return render(request, 'first_app/index.html')
    # return render(request, 'first_app/index_first.html', context=my_dict)

    # return HttpResponse('first_app/index.html')
