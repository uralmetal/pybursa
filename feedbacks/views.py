from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.core.mail import mail_admins
# Create your views here.

from .models import Feedback

class FeedbackView(generic.CreateView):
    template_name = 'feedbacks/feedbacks.html'
    model = Feedback
    fields = ['name', 'subject', 'message', 'from_email']
    success_url = reverse_lazy('feedbacks:form')

    def form_valid(self, form):
        ret = super().form_valid(form)
        if ret.url == self.get_success_url():
            try:
                mail_admins(self.model.subject, self.model.message)
                messages.success(self.request, "Спасибо за ваше сообщение! Мы скоро с вами свяжемся")
            except Exception:
                messages.success(self.request, "Сообщение сохранено, но не было доставлено администратору")
        return ret
