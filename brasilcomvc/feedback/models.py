# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


QUESTIONS = (
    'Não recebi ou recebi poucos projetos próximos',
    'Não recebi ou recebi poucos projetos para meu perfil',
    'Recebo muitos e-mails do Brasil.com.vc',
    'Não tenho mais tempo para ajudar',
    'Não tenho mais tempo para pesquisar utilizando o serviço',
)


class Feedback(models.Model):

    email = models.EmailField()
    question_1 = models.BooleanField(QUESTIONS[0], default=False)
    question_2 = models.BooleanField(QUESTIONS[1], default=False)
    question_3 = models.BooleanField(QUESTIONS[2], default=False)
    question_4 = models.BooleanField(QUESTIONS[3], default=False)
    question_5 = models.BooleanField(QUESTIONS[4], default=False)
    comments = models.TextField(default='')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    comments.verbose_name = 'comentários'

    def __str__(self):
        return '{} - {}'.format(self.email, self.created)

    def __unicode__(self):
        return '{} - {}'.format(self.email, self.created)
