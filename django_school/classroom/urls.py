from django.urls import include, path
from .views import classroom, students, teachers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', classroom.home, name='home'),

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('answer_form/',students.AnswerCreateForm.as_view(),name='add_answer'),
        path('answer_form/thanks',students.ThanksView.as_view(),name='thanks')



        #path('quiz/<int:pk>/', students.take_quiz, name='take_quiz')
        
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/answers/', teachers.AnswerListView.as_view(), name='quiz_answers'),
        path('quiz/answers/class1', teachers.Class1.as_view(), name='class1'),

        path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
    ], 'classroom'), namespace='teachers')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
