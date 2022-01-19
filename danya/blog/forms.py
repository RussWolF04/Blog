from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # исключаем не нужные для заполнения поля
        exclude = ['create_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'message': forms.Textarea(attrs={'placeholder': 'message'})
        }


# Форма поста для вывода на странице Новый Пост
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ['create_at', 'category', 'tag', 'slug']
#         # fields = ['author', 'image', 'title', 'text', 'category', 'tag', 'create_at', 'slug']
#         widgets = {
#             'author': forms.TextInput(attrs={'placeholder': 'Author'}),
#             # 'image': forms.ImageField(attrs={'placeholder': 'Image'}),
#             'title': forms.TextInput(attrs={'placeholder': 'Title'}),
#             'text': forms.Textarea(attrs={'placeholder': 'Text Post'}),
#         }

