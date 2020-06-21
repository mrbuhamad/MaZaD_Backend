from API.models import Clickes,Subscribers,Question

def run():

    clickes = Clickes.objects.all()
    subscribers=Subscribers.objects.all()
    question=Question.objects.all()
   

    for i in clickes:
        i.delete()

    for i in subscribers:
        i.delete()

    for i in question:
        i.delete()


