from blog.models import QuotesTitle
import random

def quotelist(request):
    random_index = random.randint(0,QuotesTitle.objects.count()-1)
    return {'quotesTitlerandom':QuotesTitle.objects.all()[random_index]}