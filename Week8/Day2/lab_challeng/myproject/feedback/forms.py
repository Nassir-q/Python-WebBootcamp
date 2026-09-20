from django import forms

# Define the dropdown options: (Internal Value, Display Text)
RATING_CHOICES = [
    ('', 'Select a rating (Optional)'),
    ('1', '1 - Poor'),
    ('2', '2 - Fair'),
    ('3', '3 - Good'),
    ('4', '4 - Very Good'),
    ('5', '5 - Excellent'),
]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    # Updated to use ChoiceField instead of IntegerField
    rating = forms.ChoiceField(choices=RATING_CHOICES, required=False)

    def clean_message(self):
        message_data = self.cleaned_data.get('message', '')

        if len(message_data) < 20:
            raise forms.ValidationError(
                "Message must be at least 20 characters long.")

        return message_data
