from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Listing
from .forms import CreateListingForm
# Create your views here.
class listing_detail_view(View):

    def get(self, request, *args, **kwargs):
        listing_id = kwargs['listing_id']
        template = 'listing_detail.html'
        listing = Listing.objects.get(id=listing_id)
        context = {
            'listing': listing
        }
        return render(request, template, context)

class create_listing_view(View):
    def get(self, request):
        user = self.request.user
        template_name = 'create_listing.html'
        form = CreateListingForm()
        context = {'form': form}
        return render(request, template_name, context)
    def post(self, request, *args, **kwargs):
        form = CreateListingForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                listing = form.save(commit=False)
                listing.user = request.user
                listing.save()
                template = 'listing_detail.html'
                messages.add_message(request, messages.INFO, "<p id='listing-message'>Want to create another Job Listing? Click <a href='/create/'>here</a></p>", extra_tags='safe')
                return HttpResponseRedirect("/listing/%s" % listing.id)
