from API.models import Clickes,Subscribers

def run():

    clickes = Clickes.objects.all()
    subscribers=Subscribers.objects.all()
   

    for i in clickes:
        i.delete()

    for i in subscribers:
        i.delete()

