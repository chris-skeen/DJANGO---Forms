from django import forms

class Warmup2(forms.Form):
  string = forms.CharField(max_length=50)
  number = forms.IntegerField()

class Logic2(forms.Form):
  a = forms.IntegerField()
  b = forms.IntegerField()
  c = forms.IntegerField()

class String2(forms.Form):
  string = forms.CharField(max_length=20)

class List2(forms.Form):
  n1 = forms.IntegerField()
  n2 = forms.IntegerField()
  n3 = forms.IntegerField()
  n4 = forms.IntegerField()
  n5 = forms.IntegerField()
  n6 = forms.IntegerField(required=False)
  n7 = forms.IntegerField(required=False)