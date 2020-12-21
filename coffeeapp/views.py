from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader #for template
from django.db import connection
from django.shortcuts import render
# Create your views here.
def rfact(c,r):
	return {i[0]:r[c.description.index(i)] for i in c.description}
def menu(request):
	stat=''
	c=connection.cursor()
	c.cursor.row_factory=rfact		
	c.execute("select * from item")
	r=c.fetchall()
	dl=[]
	if r:
		dl=r 

	#print (dl)
	return render(request,'menu.html',{'msg':stat,'item':dl})
def index(request):
	t=loader.get_template('index.html')
	stat="welcome to home page"
	#stat=None
         
	return HttpResponse(t.render({'msg':stat},request))

def about(request):
#return HttpResponse("about us..!")
	return render(request,'about.html')

def contact(request):
	return HttpResponse("<b>Contact us..!</b>")


