#create forms for blog app
from django import forms
from .models import Post, PostImage
from django.forms import formset_factory, modelformset_factory


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image', 'content','status')


class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('image', 'content',)


PostImageFormSet = formset_factory(PostImageForm, extra=1)
PostImageFormSetUpdate = modelformset_factory(PostImage, form=PostImageForm, extra=1)


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=True)


