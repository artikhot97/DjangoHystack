import datetime
from haystack import indexes
from my_app.models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    print( '===1===============================')
    text = indexes.EdgeNgramField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    title = indexes.CharField(model_attr='title')
    body = indexes.CharField(model_attr='body')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        print('===2===============================')
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        print(using,'=====3=============================')
        return self.get_model().objects.all()