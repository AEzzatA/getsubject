from django.http import HttpResponse
from django.shortcuts import render
from .analyzer import POSTagger

def search(request):
	output = []
	if request.method == 'POST':
		form = request.POST['item_text']
		sentence = POSTagger(form)
		sentence.processText()
		output = sentence.getSubject()
		output = [str(x) for x in output]
		return render(request, 'subject/search.html',
			{'text': form, 'output': output})

	else:
		return render(request, 'subject/search.html',
			{'output': output,})



'''
def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			message = 'You have searched for {0}'.format(request.GET['q'])
			return render(request, 'subject/search.html', {'output': message})
	else:
		message = 'You have submitted an empty form'
		return render(request, 'subject/search.html',
			{'output': message, 'error': error})
'''
