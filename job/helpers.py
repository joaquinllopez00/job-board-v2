from .models import Listing

def searchAlgo(keywords):
    q_set = []
    print(keywords, "working")
    for listing in Listing.objects.all():
        if listing.title.find(keywords) != -1:
          print(listing, "match")
          q_set.append(listing)
    print(q_set)
    return q_set
        

