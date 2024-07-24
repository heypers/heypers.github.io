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

from apps.site.models import Information, BaseModel, Character, Object, Protocol, Plot, Lore, Location, Department, Document, Organization, Group, Technology
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


class LoreForm(forms.ModelForm):
    class Meta:
        model = Lore
        fields = '__all__'


class PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = '__all__'


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = '__all__'


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class BaseModelForm(forms.ModelForm):
    class Meta:
        model = BaseModel
        fields = '__all__'
