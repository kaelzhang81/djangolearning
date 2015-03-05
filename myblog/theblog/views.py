# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader, Context
from django.shortcuts import render_to_response

# Create your views here.
# def index(req):
# 	template = loader.get_template('index.html')
# 	ctx = Context({})
# 	return HttpResponse(template.render(ctx))
class Person(object):
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex 

def index(req):
	# user = {'name':'kael', 'age':'34', 'sex':'male'}	
	user = Person('kael', 34, 'male')
	book_list = ['python', 'c++', 'java']
	return render_to_response('index.html', {'title':'my page', 'user':user, 'book':book_list})


