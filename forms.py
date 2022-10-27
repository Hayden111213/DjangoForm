from django import forms
from django.contrib.auth.models import User



class Customer(forms.Form):
    OCCUPATIONS = [("0", "Occupation"),
                   ("Head of Shrubbery", "Head of Shrubbery"),
                   ("Interim Substitute Teacher", "Interim Substitute Teacher"),
                   ("Water Softener", "Water Softener"),
                   ("Listener of the House", "Listener of the House"),
                   ("Really Good Dancer", "Really Good Dancer"),
                   ("Gainfully Unemployed", "Gainfully Unemployed"),
                   ("Alexa Impersonator", "Alexa Impersonator"),
                   ("Chard Farmer", "Chard Farmer"),
                   ("Chief Frolicker (Jolly)", "Chief Frolicker (Jolly)"),
                   ("Entry-level Seat Recliner", "Entry-level Seat Recliner"),
                   ("CEO (Summer Internship)", "CEO (Summer Internship)"),
                   ("Widget Fabricator", "Widget Fabricator"),
                   ("Underwater Basket Weaver", "Underwater Basket Weaver")]
    STATES = [("0", "State"),
              ("Alabama", "Alabama"),
              ("Alaska", "Alaska"),
              ("Arizona", "Arizona"),
              ("Arkansas", "Arkansas"),
              ("California", "California"),
              ("Colorado", "Colorado"),
              ("Connecticut", "Connecticut"),
              ("Delaware", "Delaware"),
              ("District of Columbia", "District Of Columbia"),
              ("Florida", "Florida"),
              ("Georgia", "Georgia"),
              ("Hawaii", "Hawaii"),
              ("Idaho", "Idaho"),
              ("Illinois", "Illinois"),
              ("Indiana", "Indiana"),
              ("Iowa", "Iowa"),
              ("Kansas", "Kansas"),
              ("Kentucky", "Kentucky"),
              ("Louisiana", "Louisiana"),
              ("Maine", "Maine"),
              ("Maryland", "Maryland"),
              ("Massachusetts", "Massachusetts"),
              ("Michigan", "Michigan"),
              ("Minnesota", "Minnesota"),
              ("Mississippi", "Mississippi"),
              ("Missouri", "Missouri"),
              ("Montana", "Montana"),
              ("Nebraska", "Nebraska"),
              ("Nevada", "Nevada"),
              ("New Hampshire", "New Hampshire"),
              ("New Jersey", "New Jersey"),
              ("New Mexico", "New Mexico"),
              ("New York", "New York"),
              ("North Carolina", "North Carolina"),
              ("North Dakota", "North Dakota"),
              ("Ohio", "Ohio"),
              ("Oklahoma", "Oklahoma"),
              ("Oregon", "Oregon"),
              ("Pennsylvania", "Pennsylvania"),
              ("Rhoda Island", "Rhode Island"),
              ("South Carolina", "South Carolina"),
              ("South Dakota", "South Dakota"),
              ("Tennessee", "Tennessee"),
              ("Texas", "Texas"),
              ("Utah", "Utah"),
              ("Vermont", "Vermont"),
              ("Virginia", "Virginia"),
              ("Washington", "Washington"),
              ("West Virginia", "West Virginia"),
              ("Wisconsin", "Wisconsin"),
              ("Wyoming", "Wyoming")]

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'style': 'width: 300px;',
        'class': 'name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'style': 'width: 300px;',
        'class': 'email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'style': 'width: 300px;',
        'class': 'pass'}))
    occupation = forms.CharField(widget=forms.Select(choices=OCCUPATIONS,
                                                     attrs={
                                                         'placeholder': 'Occupation',
                                                         'style': 'width: 300px;',
                                                         'class': 'occ'}))

    states = forms.CharField(widget=forms.Select(choices=STATES,
                                                 attrs={
                                                     'placeholder': 'State',
                                                     'style': 'width: 300px;',
                                                     'class': 'states'}))

    class Meta:
        model = User
        fields = '__all__'
