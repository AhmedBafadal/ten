from django.shortcuts import render
from django.http import HttpResponse
from .forms import CsvModelForm
from .models import Csv, Member, Inventory
from datetime import datetime
import csv
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def apiOverview(request):
    # takes a booking of item from inventory based on
    # name of member
    # provides a reference number and records it
    # max    booking must not be over 2 AND inventory remaining count cannot be 0.
    pass

@api_view(['DEL'])
def apiCanel(request):
    # delete based on reference provided.
    # return inventory + 1
    # member booking reduced by 1
    pass


def upload_members_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)

        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            if 'member' in str(obj.file_name).lower():
                for i, row in enumerate(reader):
                    if i == 0: 
                        pass
                    else:
                        first = row[0]
                        last = row[1]
                        booking_count = int(row[2])
                        date = datetime.strptime(row[3], '%Y-%m-%dT%H:%M:%S') 
                        Member.objects.create(name= first, surname= last, booking_count= booking_count, date_joined=date) 
                        print(Member)
                        # print(first, last, booking_count, type(date))
                        # member.save()
        obj.activated=True
        obj.save()
            
    # return redirect(upload_inventory_view)
    return render(request, 'core/upload-members.html', {'form': form})

def upload_inventory_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        objs = Csv.objects.all().filter(activated=False)
        for ob in objs:
            if 'inventory' in str(ob.file_name).lower():
                print('Here')
                with open(ob.file_name.path, 'r') as f:
                    reader = csv.reader(f)
                    
                    for i, row in enumerate(reader):
                        if i == 0:
                            pass
                        else:
                            if all(row):
                                print(row)
                                title = row[0]
                                description = row[1]
                                remaining_count = int(row[2])
                                expiration_date = datetime.strptime(row[3], '%d/%m/%Y')
                                Inventory.objects.create(title=title, description=description, remaining_count=remaining_count, expiration_date=expiration_date)
                            else:
                                pass
                            # inventory.save()
                            # print(title, description, remaining_count, type(expiration_date))
        ob.activated=True
        ob.save()
                        
                            
    return render(request, 'core/upload-inventory.html', {'form': form})


#1  Booking an item from the inventory in the name of a member via a /book endpoint. Whenever a
# member makes a booking, keep a record of it in the database, including datetime of booking. A
# booking will only be possible if a member hasn’t reached MAX_BOOKINGS = 2, and if the
# inventory’s remaining_count hasn’t been depleted.
#2 Cancelling a booking for a member based on a booking reference via a /cancel endpoint.