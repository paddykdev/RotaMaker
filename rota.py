import json
import random

staff = {"Carer": {
    1: {"fname": "Rebecca", "lname": "Herbert", "shifts": 5, "am": True, "pm": True},
    2: {"fname": "Toni", "lname": "Herbert", "shifts": 3, "am": True, "pm": True},
    3: {"fname": "Justyna", "lname": "Polish", "shifts": 4, "am": True, "pm": True},
    4: {"fname": "Debbie", "lname": "Debbie", "shifts": 5, "am": True, "pm": True},
    5: {"fname": "Andrea", "lname": "Eddie", "shifts": 5, "am": True, "pm": True},
    6: {"fname": "Darren", "lname": "Eddie", "shifts": 5, "am": True, "pm": True},
    7: {"fname": "Lisa", "lname": "Abudabwenga", "shifts": 5, "am": True, "pm": True},
    8: {"fname": "Laura", "lname": "Smith", "shifts": 5, "am": True, "pm": True},
    9: {"fname": "Collun", "lname": "Jebadiah", "shifts": 3, "am": True, "pm": True},
    10: {"fname": "Taylor", "lname": "Reefa", "shifts": 5, "am": False, "pm": True},
    11: {"fname": "Anna", "lname": "Spanna", "shifts": 5, "am": False, "pm": True},
    12: {"fname": "Raani", "lname": "Arnie", "shifts": 5, "am": False, "pm": True},
    13: {"fname": "Seema", "lname": "Keema", "shifts": 2, "am": False, "pm": True},
    14: {"fname": "Saffie", "lname": "Laughy", "shifts": 2, "am": False, "pm": True},
    15: {"fname": "Tara", "lname": "Para", "shifts": 3, "am": True, "pm": False},
}}


class Employee:
    def __init__(self, dict):
        self.fname = dict["fname"]
        self.lname = dict["lname"]
        self.am = dict["am"]
        self.pm = dict["pm"]
        self.shifts = dict["shifts"]
        self.shifts_assigned = 0
        self.actualshifts = {}

    def __str__(self):
        return f"{self.fname} {self.lname}"

    def shiftsLeft(self):
        shiftsleft = self.shifts - self.shifts_assigned
        return shiftsleft
    
    
    def getShift(self, term):
        for shift in self.actualshifts.keys():
            if shift == term:
                return (shift, self.actualshifts[shift])
            else:
                continue
    
    def week(self):
        fullrow = {
            "Saturday": self.getShift("Saturday"),
            "Sunday": self.getShift("Sunday"),
            "Monday": self.getShift("Monday"),
            "Tuesday": self.getShift("Tuesday"),
            "Wednesday": self.getShift("Wednesday"),
            "Thursday": self.getShift("Thursday"),
            "Friday": self.getShift("Friday"),        
        }
        return fullrow


staffdict = {
    "rherbert": Employee(staff["Carer"][1]),
    "therbert": Employee(staff["Carer"][2]),
    "jpolish": Employee(staff["Carer"][3]),
    "ddebbie": Employee(staff["Carer"][4]),
    "aeddie": Employee(staff["Carer"][5]),
    "deddie": Employee(staff["Carer"][6]),
    "labudabwenga": Employee(staff["Carer"][7]),
    "lsmith": Employee(staff["Carer"][8]),
    "cjebadiah": Employee(staff["Carer"][9]),
    "treefa": Employee(staff["Carer"][10]),
    "aspanna": Employee(staff["Carer"][11]),
    "rarnie": Employee(staff["Carer"][12]),
    "skeema": Employee(staff["Carer"][13]),
    "slaughy": Employee(staff["Carer"][14]),
    "tpara": Employee(staff["Carer"][15]),
}
staffkeys = list(staffdict.keys())
print(staffkeys)
random.shuffle(staffkeys)
staffObject = {}
for key in staffkeys:
    staffObject[key] = staffdict[key]



table = {
    "AM": {
        "Saturday": {
            1: None, 2: None, 3: None, 4: staffObject["cjebadiah"].__str__(), 5: None
        },
        "Sunday": {
            1: None, 2: None, 3: None, 4: staffObject["cjebadiah"].__str__(), 5: staffObject["jpolish"].__str__()
        },
        "Monday": {
            1: None, 2: None, 3: None, 4: staffObject["cjebadiah"].__str__(), 5: None
        },
        "Tuesday": {
            1: None, 2: None, 3: None, 4: None, 5: None
        },
        "Wednesday": {
            1: None, 2: None, 3: None, 4: None, 5: staffObject["jpolish"].__str__()
        },
        "Thursday": {
            1: None, 2: None, 3: None, 4: None, 5: None
        },
        "Friday": {
            1: None, 2: None, 3: None, 4: None, 5: None
        },
    },
    "PM": {
        "Saturday": {
            1: None, 2: None, 3: None, 4: None
        },
        "Sunday": {
            1: staffObject["jpolish"].__str__(), 2: None, 3: None, 4: None
        },
        "Monday": {
            1: None, 2: None, 3: None, 4: None
        },
        "Tuesday": {
            1: None, 2: None, 3: None, 4: staffObject["skeema"].__str__()
        },
        "Wednesday": {
            1: staffObject["jpolish"].__str__(), 2: None, 3: None, 4: staffObject["skeema"].__str__()
        },
        "Thursday": {
            1: None, 2: None, 3: None, 4: None
        },
        "Friday": {
            1: None, 2: None, 3: None, 4: None
        },
    },
}

for period in table:
    for day in table[period]:
        for shift in table[period][day]:
            for stobj in staffObject:
                if table[period][day][shift] == staffObject[stobj].__str__():
                    staffObject[stobj].shifts_assigned += 1



def getStaffList(sent_period, staffdict):
    stafflist = []
    #print(staffdict)
    if sent_period.lower() == "am":
        for staff_ in staffdict:
            staff = staffdict[staff_]
            if staff.am == True:
                if staff.shiftsLeft() == 0:
                    continue
                else:
                    stafflist.append(staff_)
            else:
                continue
    else:
        for staff_ in staffdict:
            staff = staffdict[staff_]
            if staff.pm == True:
                if staff.shiftsLeft() == 0:
                    continue
                else:
                    stafflist.append(staff_)
            else:
                continue    
    random.shuffle(stafflist)
    return stafflist


def gethighest(listtocalc):
    # print(listtocalc)
    lowest_staff = None
    lowest_amount = 0
    for staffa in listtocalc:
        if staffObject[staffa].shiftsLeft() > lowest_amount:
            lowest_staff = staffa
            lowest_amount = staffObject[staffa].shiftsLeft()
    return lowest_staff


def checkDay(dayshift, employ):
    check = True
    if employ == None:
        return check
    for shift_ in dayshift:
        # print(dayshift[shift_])
        if dayshift[shift_] == staffObject[employ].__str__():
            check = False
        #print(check, employ)

    return check


def main():
    for period in table:
        #print(f"{period} : {table[period]}")
        for day in table[period]:
            # print(f"{day} : {table[period][day]}")
            for shift in table[period][day]:
                staffObjectcopy = staffObject.copy()
                #print(f"{shift} : {table[period][day][shift]}")
                if table[period][day][shift] is None:
                    stafflist = getStaffList(period, staffObjectcopy)
                    lowestshiftstaff = gethighest(stafflist)
                    check = checkDay(table[period][day], lowestshiftstaff)
                    while check is False:
                        del staffObjectcopy[lowestshiftstaff]
                        stafflist = getStaffList(period, staffObjectcopy)
                        lowestshiftstaff = gethighest(stafflist)
                        check = checkDay(table[period][day], lowestshiftstaff)
                    if lowestshiftstaff:
                        table[period][day][shift] = staffObject[lowestshiftstaff].__str__()
                        staffObject[lowestshiftstaff].shifts_assigned += 1
                else:
                    continue
    for value in staffObject.values():
        print(f"{value.__str__()}  {value.shiftsLeft()}")
    answer = input(" Process rota? y/n")
    if answer.lower() == "y":
        return True
    else:
        main()

main()
count = 0
for period in table:
    for day in table[period]:
        for staff in staffObject:
            for shift in table[period][day]:
                shiftstaff = table[period][day][shift]            
                if shiftstaff == staffObject[staff].__str__():
                    staffObject[staff].actualshifts[day] = period
                    count += 1
                    #print(shiftstaff, period, day, shift, count)

def fromatcsv(data):
    print(data)
    if data == False:
        return ""
    elif data == None:
        return ""
    elif data[1] == "AM":
        #print(data[0])
        return "Morning"
    elif data[1] == "PM":
        #print(data[0])
        return "Evening"
    else:
        return ""


import csv
import time

with open('rota.csv', 'w', newline='') as csvfile:
    fieldnames = ['Employee', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
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
        time.sleep(1)
