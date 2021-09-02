from django import forms
from .models import blog


class blogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'author', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = blog.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'Title: {title} , already exists!!!')
        return data
