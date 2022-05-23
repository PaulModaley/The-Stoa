from django import forms
from models import Post

class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'status']

form = ArticleForm()

article = Article.objects.get(pk=1)
form = ArticleForm(instance=article)