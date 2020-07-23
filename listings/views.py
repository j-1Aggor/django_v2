from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_mvp=True)
    
    # paginator
    paginator = Paginator(listings,2)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)

    context = {
        'listings': paged_listings
    }
    return render(request,'listings/listings.html',context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    
    context = {
        'listing': listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    querysetlist = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords :
            querysetlist = querysetlist.filter(description__icontains = keywords,is_mvp=True)
    
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city :
            querysetlist = querysetlist.filter(city__iexact = city,is_mvp=True)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms :
            querysetlist = querysetlist.filter(bedrooms__lte = bedrooms,is_mvp=True)

    if 'price' in request.GET:
        price = request.GET['price']
        if price :
            querysetlist = querysetlist.filter(price__lte = price,is_mvp=True)


    context = {
        'listings': querysetlist
    }
    return render(request,'listings/search.html',context)
