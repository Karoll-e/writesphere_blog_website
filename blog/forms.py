from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['header_image', 'title', 'content', 'category']