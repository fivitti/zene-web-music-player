from django.contrib.auth.models import User
import datetime
from models import Application

def generate_dict(mode, user):
    app = Application.objects.filter(status=mode, author=user)
    label_active = 'active_' + mode
    label_count = 'count_' + mode
    d = {'applications': app,
         label_active: 'active',
         label_count: len(app)}
    return d

def create_application(cleaned_data, author):
    label_user = cleaned_data.get('user')
    user = User.objects.get(username=label_user)
    app = Application(title=cleaned_data.get('title'),
                      user=user,
                      description=cleaned_data.get('description'),
                      answer='',
                      author=author,
                      status='a',
                      date_create=datetime.datetime.now().date())

    app.save()