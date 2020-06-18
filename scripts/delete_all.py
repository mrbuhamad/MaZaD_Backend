from API.models import *

def run():

    Clickes = Clickes.objects.all()
    Subscribers=Subscribers.objects.all()
   

    for i in Clickes:
        i.delete()

    for i in Subscribers:
        i.delete()


