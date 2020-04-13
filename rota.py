import csv
import json
import os
import sys
import time

import RotaUtil as ru
import ShiftPattern as sp


"""for period in table:
    for day in table[period]:
        for shift in table[period][day]:
            for stobj in staffObject:
                if table[period][day][shift] == staffObject[stobj].__str__():
                    staffObject[stobj].shifts_assigned += 1"""


def gethighest(listtocalc, staffObject):
    lowest_staff = None
    lowest_amount = 0
    for staffa in listtocalc:
        if staffObject[staffa].shiftsLeft() > lowest_amount:
            lowest_staff = staffa
            lowest_amount = staffObject[staffa].shiftsLeft()
    return lowest_staff


def checkDay(dayshift, employ, staffObject):
    check = True
    if employ == None:
        return check
    for shift_ in dayshift:
        if dayshift[shift_] == staffObject[employ].__str__():
            check = False

    return check

done = False

def main():
    staff = ru.staff
    staffObject = ru.getStaffObject()
    shiftpattern = sp.pattern

    for day in shiftpattern:
        for shift in shiftpattern[day]:
            for slot in shiftpattern[day][shift]:
                for stobj in staffObject:
                    if shiftpattern[day][shift][slot] == staffObject[stobj].__str__():
                        staffObject[stobj].shifts_assigned += 1
                    else:
                        continue

    for day in shiftpattern:
        for shift in shiftpattern[day]:
            for slot in shiftpattern[day][shift]:
                staffObjectcopy = staffObject.copy()
                if shiftpattern[day][shift][slot] == None:
                    stafflist = ru.getStaffList(shift, staffObjectcopy)
                    lowestshiftstaff = gethighest(stafflist, staffObject)
                    check = checkDay(shiftpattern[day][shift], lowestshiftstaff, staffObject)
                    while check is False:
                        del staffObjectcopy[lowestshiftstaff]
                        stafflist = ru.getStaffList(shift, staffObjectcopy)
                        lowestshiftstaff = gethighest(stafflist, staffObject)
                        check = checkDay(
                            shiftpattern[day][shift], lowestshiftstaff, staffObject)
                    if lowestshiftstaff:
                        shiftpattern[day][shift][slot] = staffObject[lowestshiftstaff].__str__()
                        staffObject[lowestshiftstaff].shifts_assigned += 1
                    else:
                        continue
    shiftsun = 0
    count = 0
    for day in shiftpattern:
        for shift in shiftpattern[day]:
            for staff in staffObject:
                for slot in shiftpattern[day][shift]:
                    shiftstaff = shiftpattern[day][shift][slot]
                    if shiftstaff == staffObject[staff].__str__():
                        staffObject[staff].actualshifts[day] = shift
                        count += 1
    errors = ru.checkErrors(staffObject)
    #answer = input(" Process rota? y/n")
    if int(errors) <= 18:
        return staffObject
    else:
        print(f" Errors: {errors}  Shifts Not Full: {shiftsun}")
        with open('tries.csv', 'a', newline='') as csvfile1:
            writer = csv.writer(csvfile1)
            writer.writerow((errors, shiftsun))
        os.execl(sys.executable, sys.executable, * sys.argv)
        

staffObject = main()


def fromatcsv(data):
    if data == False:
        return "None"
    elif data == None:
        return "None"
    elif data == "AM":
        return "Morning"
    elif data == "PM":
        return "Evening"
    elif data == "NS":
        return "Night"
    else:
        return "None"


with open('rota.csv', 'w', newline='') as csvfile:
    fieldnames = ['Employee', 'Saturday', 'Sunday', 'Monday',
                  'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for staff in staffObject:
        details = staffObject[staff].week()
        writer.writerow({
            'Employee': staffObject[staff].__str__(),
            'Saturday': fromatcsv(details['Saturday']),
            'Sunday': fromatcsv(details['Sunday']),
            'Monday': fromatcsv(details['Monday']),
            'Tuesday': fromatcsv(details['Tuesday']),
            'Wednesday': fromatcsv(details['Wednesday']),
            'Thursday': fromatcsv(details['Thursday']),
            'Friday': fromatcsv(details['Friday'])})
