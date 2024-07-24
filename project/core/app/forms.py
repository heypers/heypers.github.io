"""
Copyright 2023 mr_fortuna

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from apps.site.models import Information, BaseModel, Character, Object, Protocol
from django import forms


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = '__all__'

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'

class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = '__all__'


class ProtocolForm(forms.ModelForm):
    class Meta:
        model = Protocol
        fields = '__all__'

class BaseModelForm(forms.ModelForm):
    class Meta:
        model = BaseModel
        fields = '__all__'
