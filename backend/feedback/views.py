from django.shortcuts import redirect, render
from feedback.forms import FeedbackCreateFrom

from django.core.mail import send_mail


def send_message_user(request):
    """Добавление карточки товара"""

    if request.method =='POST':
        form = FeedbackCreateFrom(request.POST)
 
        subject = request.POST.get("subject", "")
        message = request.POST.get("content", "")
        from_email = request.POST.get("email", "")
        recipient_list = ['subachevdenis@yandex.ru']

        if form.is_valid():
            form.save()
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            return redirect('marketplace:product_list')
    else:
        form = FeedbackCreateFrom()
        context = {
            'title': 'Обратная связь пользователя',
            'form': form
        }
        return render(request, 'blog/base_form.html', context)
    

 
