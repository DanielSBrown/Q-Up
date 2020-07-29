from django import forms

class RoomForm(forms.Form):
    room_name = forms.CharField(label='Your group name', max_length=100)
