from django.urls import include, path
from .views import classroom, students, teachers
from django.conf import settings
from django.conf.urls.static import static
app_name = 'buiz'
urlpatterns = [
    #path('', students.AnswerCreateView.as_view(), name='answer_add'),

    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
