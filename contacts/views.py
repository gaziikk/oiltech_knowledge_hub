from django.shortcuts import redirect, render
from oiltech_knowledge_hub.forms import AddPostForm
from django.core.mail import EmailMessage
from os import getenv
from aiogram import Bot, asyncio

def contacts(request):
    message_send = False
    
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            answer = form.cleaned_data['answer']

            subject = f'Новый вопрос от пользователя {full_name}'
            message = (f'База знаний в области нефтяных технологий.\n'
                       f'От: {full_name}\n'
                       f'Почта: ({email}):\n\n'
                       f'{answer}')

            # Отправка сообщений в телеграм
            async def send_telegram_message():
                bot = Bot(token=getenv('TOKEN'))
                
                await bot.send_message(getenv('TELEGRAM_ID'),
                           f'*{subject}*\n'
                           f'{message}',
                           parse_mode='MARKDOWN'
                          )
            asyncio.run(send_telegram_message())
                
            # Отправка сообщений на почту
            email_send = EmailMessage(
                subject,
                message,
                str(getenv("EMAIL")),
                to=[str(getenv("EMAIL"))]
            )
            email_send.send(fail_silently=False)
            message_send = True
    else:
        form = AddPostForm()
    data = {
        'form': form,
        'message_send': message_send
    }
    return render(request, 'contacts.html', data)
