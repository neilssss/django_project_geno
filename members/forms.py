from django import forms
from django.forms import ModelForm
from.models import Fish2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Fish2Form(ModelForm):
	class Meta:
		model = Fish2
		fields = ('fish_type','fish_name','fish_size','fish_img','fish_desc','available_size','available_qty','fish_price')
		labels = {
			'fish_type': '',
			'fish_name': '',
			'fish_size': '',
			'fish_img': 'Browse Image',
			'fish_desc': '',
			'available_size': '',
			'available_qty': '',
			'fish_price': '',

		}
		widgets = {
			'fish_type': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Fish Type'}),
			'fish_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Fish Name'}),
			'fish_size': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Max Size'}),
			'fish_desc': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Characteristic of Fish'}),
			'available_size': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Available Size'}),
			'available_qty': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Available qty'}),
			'fish_price': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Price'}),
			
		}

class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'