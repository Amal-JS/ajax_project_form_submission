from django.http import JsonResponse
from django.shortcuts import redirect, render
from . forms import Custom_Form

# Create your views here.

def index(request):

    #normal django approach
    '''
    if request.method =='POST':
        
        form = Custom_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            return render(request,'index.html',{'form':form})'''
    
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest': # check if request is ajax ,old (.is_ajax())
        form = Custom_Form(request.POST)  

        print(request.POST) #printing the request

        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'  # if success we are returning a Json response which has a object 
                                      # with key message and value as success .
                                      #  can access this value in html after ajax execution will get it in 'success',  handler function
            })
        else:
            return JsonResponse({
                'message':'rejected',  #if form has error changed message to rejected and form.errors is send
                'reason':form.errors    # with another key reason
            })
    form = Custom_Form()
    return render(request,'index.html',{'form':form})
        


def success(request):
    return render(request,'success.html')