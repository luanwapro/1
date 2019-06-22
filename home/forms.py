from django import forms
import re
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from .models import Comment

User = get_user_model()
class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='Họ', max_length=50)
    last_name = forms.CharField(label='Tên', max_length=50)
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.CharField(label='Email', max_length=50)
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Xác nhận mật khẩu', widget=forms.PasswordInput())
    phone_number = forms.CharField(label='Số điện thoại', max_length=50 )
    address = forms.CharField(label='Địa chỉ', max_length=50)

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
            raise  forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        User.objects.create_user(first_name = self.cleaned_data['first_name'], last_name = self.cleaned_data['last_name'], username = self.cleaned_data['username'], email = self.cleaned_data['email'], password = self.cleaned_data['password1'],
                                 phone_number = self.cleaned_data['phone_number'], address = self.cleaned_data['address'])

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author', None)
        self.product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.product = self.product
        comment.save()
    class Meta:
        model = Comment
        fields =["body"]