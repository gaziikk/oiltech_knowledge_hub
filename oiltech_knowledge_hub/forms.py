from django import forms

class AddPostForm(forms.Form):
    full_name = forms.CharField(max_length=255, label="ФИО")
    email = forms.EmailField(max_length=255, label="Email")
    answer = forms.CharField(widget=forms.Textarea(), label="Вопрос")  
    