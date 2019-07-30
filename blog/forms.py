from django import forms
from .models import Blog,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog # 어떤 모델 쓸래?
        # fields = {"name", "leader", "create_date", "location", "introduce"}
        # 그 모델에서 어떤 필드 쓸래?

        fields = '__all__' # 모델 모든 필드를 다 씀
        exclude = ['pub_date'] # name 필드 사용 안함

        widgets = { # name 필드 위젯을 재정의, Textinput 태그, class는 test 지정
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {"body",}

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update({'class' : 'form-control'})
        # 필드 중 name을 찾아서 class를 test로 업데이트