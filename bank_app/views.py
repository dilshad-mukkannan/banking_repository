from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import District, Branch, Customer
from .forms import MovieForm
from django.views.generic.edit import CreateView


# Create your views here.

def demo(request):
    return render(request, 'index.html')


def create_form(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Application accepted!')
        return HttpResponseRedirect(request.path_info)
    return render(request,'form.html', {'form':form})






# class FormCreateView(CreateView):
#     model = Customer
#     template_name = 'form.html'
#     fields = '__all__'


# def create_customer(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         dob = request.POST.get("dob")
#         age = request.POST.get("age")
#         gender = request.POST.get("gender")
#         phone = request.POST.get("phone")
#         mail = request.POST.get("mail")
#         address = request.POST.get("address")
#         district_id = request.POST.get("district")
#         branch_id = request.POST.get("branch")
#         account_type = request.POST.get("account_type")
#         materials_provided = request.POST.getlist("materials_provided")
#
#         # Convert IDs to objects
#         district = District.objects.get(pk=district_id)
#         branch = Branch.objects.get(pk=branch_id)
#         materials = Material.objects.filter(pk__in=materials_provided)
#
#         # Create a Customer instance and save it
#         customer = Customer(
#             name=name,
#             dob=dob,
#             age=age,
#             gender=gender,
#             phone=phone,
#             mail=mail,
#             address=address,
#             district=district,
#             branch=branch,
#             account_type=account_type
#         )
#         customer.save()
#
#         # Add materials provided
#         customer.materials_provided.set(materials)
#
#         # Redirect to a success page or perform other actions as needed
#         return redirect('/')
#
#     districts = District.objects.all()
#     all_branches = Branch.objects.all()
#     materials = Material.objects.all()
#
#
#     return render(request, 'form.html', {
#         'districts': districts,
#         'all_branches': all_branches,
#         'materials': materials,
#     })


