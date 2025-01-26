from django.forms import ModelForm
from feedback import models



class FeedbackCreateFrom(ModelForm):
    """
    Форма отправки обратной связи
    """

    class Meta:
        model = models.Feedback
        fields = ('subject', 'email', 'content')

    
