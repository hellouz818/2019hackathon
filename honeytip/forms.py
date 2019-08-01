from django import forms 
from .models import Post 
class PostForm(forms.ModelForm):
class Meta:
model = Post # form에서 사용할 모델이 Post임을 명시
fields = ['title','content']