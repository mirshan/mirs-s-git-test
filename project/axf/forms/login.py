from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,min_length=6,required=True,error_messages={'required':'用户账号不能为空','invalid':'格式错误'},widget=forms.TextInput(attrs={'class':'c'}))
    #定义了最长，最短，必填，错误信息，widget是：给模板中textinput添加class=c的样式
    passwd=forms.CharField(max_length=20,min_length=6,required=True,widget=forms.PasswordInput)
    #widget中forms.PasswordInput指的是密码加密

