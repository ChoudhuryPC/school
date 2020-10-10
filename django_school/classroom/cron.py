from .models import Quiz,Answer
from datetime import datetime



def check():
	for q in Answer.objects.all():
		print(type(q.quiz_name))
		

	
			