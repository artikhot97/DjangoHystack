from django.shortcuts import render
from rest_framework.decorators import (
    api_view, renderer_classes,
)
from .models import Note
from haystack.query import SearchQuerySet
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def search_note(request, title):
    note = SearchQuerySet().models(Note).autocomplete(
        title__startswith=title)
    searched_data = []
    for i in note:
        all_results = {"title": i.title,
                       "body": i.body,
                       "pub_date": i.pub_date,
                       "user": i.user,
                       }
        searched_data.append(all_results)
    return Response(searched_data)
