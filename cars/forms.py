from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vehicle, Bid, VehicleImage
from django.forms import inlineformset_factory

VehicleImageFormSet = inlineformset_factory(
    Vehicle, VehicleImage, fields=('image',), extra=3, can_delete=True
)

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['make', 'model', 'year', 'starting_price', 'description', 'image', 'mileage', 'condition', 'transmission', 'owner_phone', 'owner_email']

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['max_price']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user