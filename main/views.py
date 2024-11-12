from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages

def home(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Отправка письма
            send_mail(
                f'Сообщение от {name}',
                message,
                email,
                ['youremail@example.com'],  # Замени на свой email
                fail_silently=False,
            )
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            form = ContactForm()  # Сброс формы после отправки

    return render(request, 'main/home.html', {'form': form})
