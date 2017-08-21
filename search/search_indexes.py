from django.contrib.auth.models import User
from haystack import indexes
from accounts.models import Profile


class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    username = indexes.CharField(model_attr='username')
    content_auto = indexes.EdgeNgramField(model_attr='username')

    def get_model(self):
        return Profile

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
