from django.shortcuts import render
from django.http import JsonResponse
from demoapp.models import EmployeeDetails,InsuaranceDetails
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from .serializers import EmployeeDetailsSerializer
from rest_framework.response import Response

# Create your views here.
def index(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')
        department = request.POST.get('department')

        try:
            employee_Detail = EmployeeDetails()
            employee_Detail.full_name = full_name
            employee_Detail.age = age
            employee_Detail.department = department
            employee_Detail.salary = salary
            employee_Detail.designation = designation
            employee_Detail.save()

        except Exception as e:
            print(e)
    return render(request,"index.html")


def policy(request):
    if request.method == "POST":
        policy_name = request.POST.get('policy_name')
        policy_number = request.POST.get('policy_number')

        full_name = request.POST.get('full_name')
        age = request.POST.get('age')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')
        department = request.POST.get('department')

        try:
            employee_Detail = EmployeeDetails()
            employee_Detail.full_name = full_name
            employee_Detail.age = age
            employee_Detail.department = department
            employee_Detail.salary = salary
            employee_Detail.designation = designation
            employee_Detail.save()
            
            employeePolicyDetail = InsuaranceDetails()
            employeePolicyDetail.full_name = employee_Detail
            employeePolicyDetail.policy_name = policy_name
            employeePolicyDetail.policy_number = policy_number
            employeePolicyDetail.save()

        except Exception as e:
            print(e)
    return render(request,"policy.html")



class EmployeeDetailsViewset(viewsets.ViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer

    def list(self, request):
        get_all_employee = EmployeeDetails.objects.all()
        data = EmployeeDetailsSerializer(get_all_employee,many=True)
        return Response({'data': data.data}, content_type = 'application/json' )
    
    def destroy(self, request, id):
        user_name = EmployeeDetails.objects.filter(id=id)
        user_name = user_name.full_name
        EmployeeDetails.objects.filter(id=id).delete()
        return Response({'data':f" {user_name} user is deleted"}, 
                        content_type = 'application/json' )

    def create(self, request):
        #postEmpData = request.data
        #print(postEmpData)
        dataSeriealizer = EmployeeDetailsSerializer(data = request.data)
        if dataSeriealizer.is_valid():
            dataSeriealizer.save()
            return Response({'data': dataSeriealizer.data}, content_type = 'application/json')
        else:
            return Response(dataSeriealizer.errors)