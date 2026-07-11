from django.shortcuts import render, redirect
from .models import Staff

def home(request):
    return render(request, "staff/home.html")

def staff_list(request):
    staffs = Staff.objects.all()

    return render(request, "staff/staff_list.html",
                    {"staffs": staffs}
                )

def add_staff(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        department = request.POST.get("department")
        designation = request.POST.get("designation")
        joining_date = request.POST.get("joining_date")
        salary = request.POST.get("salary")

        Staff.objects.create(
            name=name,
            email=email,
            phone=phone,
            department=department,
            designation=designation,
            joining_date=joining_date,
            salary=salary
        )

        return redirect("staff_list")

    return render(request, "staff/add_staff.html")

def edit_staff(request, id):

    staff = Staff.objects.get(id=id)

    if request.method == "POST":

        staff.name = request.POST.get("name")
        staff.email = request.POST.get("email")
        staff.phone = request.POST.get("phone")
        staff.department = request.POST.get("department")
        staff.designation = request.POST.get("designation")
        staff.joining_date = request.POST.get("joining_date")
        staff.salary = request.POST.get("salary")

        staff.save()

        return redirect("staff_list")

    return render(
        request,
        "staff/edit_staff.html",
        {
            "staff": staff
        }
    )

def delete_staff(request, id):
    staff = Staff.objects.get(id=id)
    staff.delete()

    return redirect("staff_list")