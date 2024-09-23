from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *

# Create your views here.

    

def index(request):
    
    if request.method == 'POST':
        access_code_input = request.POST.get('access_code')  # Get access code from the form

        try:
            # Check if access code exists
            access_code = AccessCode.objects.get(code=access_code_input)
            # Redirect to details page and pass access code
            return redirect('details-page', access_code=access_code.code)

        except AccessCode.DoesNotExist:
            # Access code does not exist, show error message
            messages.error(request, 'Invalid access code. Please try again.')
    
    return render(request,'index.html')

# Function to display product details
def details(request, access_code):
    # Retrieve product details by access code
    access_code = get_object_or_404(AccessCode, code=access_code)
    product_details = get_object_or_404(ProductDetails, access_code=access_code)
    
    # Pass product details to the template
    context = {
        'access_code': access_code,
        'product_details': product_details
    }
    return render(request, 'details.html', context)












