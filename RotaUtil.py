import random

staff = {"Carer": {
    1: {"fname": "Rebecca", "lname": "Herbert", "shifts": 5, "am": True, "pm": False, "ns": False},
    2: {"fname": "Toni", "lname": "Herbert", "shifts": 3, "am": True, "pm": False, "ns": False},
    3: {"fname": "Justyna", "lname": "Polish", "shifts": 4, "am": True, "pm": True, "ns": False},
    4: {"fname": "Debbie", "lname": "Debbie", "shifts": 5, "am": True, "pm": True, "ns": False},
    5: {"fname": "Andrea", "lname": "Eddie", "shifts": 5, "am": True, "pm": True, "ns": False},
    6: {"fname": "Darren", "lname": "Eddie", "shifts": 5, "am": True, "pm": True, "ns": False},
    7: {"fname": "Lisa", "lname": "Abudabwenga", "shifts": 5, "am": True, "pm": True, "ns": False},
    8: {"fname": "Laura", "lname": "Smith", "shifts": 5, "am": True, "pm": True, "ns": False},
    9: {"fname": "Collun", "lname": "Jebadiah", "shifts": 3, "am": True, "pm": True, "ns": False},
    10: {"fname": "Taylor", "lname": "Reefa", "shifts": 5, "am": False, "pm": True, "ns": False},
    11: {"fname": "Anna", "lname": "Spanna", "shifts": 5, "am": False, "pm": True, "ns": False},
    12: {"fname": "Raani", "lname": "Arnie", "shifts": 5, "am": False, "pm": True, "ns": False},
    13: {"fname": "Seema", "lname": "Keema", "shifts": 2, "am": False, "pm": True, "ns": False},
    14: {"fname": "Saffie", "lname": "Laughy", "shifts": 2, "am": False, "pm": True, "ns": False},
    15: {"fname": "Tara", "lname": "Para", "shifts": 3, "am": True, "pm": False, "ns": False},
}}

class Employee:
    def __init__(self, dict):
        self.fname = dict["fname"]
        self.lname = dict["lname"]
        self.am = dict["am"]
        self.pm = dict["pm"]
        self.ns = dict["ns"]
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
                return (self.actualshifts[shift])
            else:
                continue
        return None
    
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

def myDictRandom(myDict):
    current_list = list(myDict.keys())
    copied_list = list(current_list)
    new_list = []
    for x in current_list:
        x = x
        length_list = len(copied_list)
        randomkey = random.randint(0, length_list)
        xb = copied_list[randomkey-1]
        new_list.append(xb)
        copied_list.remove(xb)
    new_dict = {}
    for item in new_list:
        new_dict[item] = myDict[item]
    return new_dict

def getStaffObject():
    staffdict= {}
    for carer in staff["Carer"]:
        staffdict[f"{staff['Carer'][carer]['fname'][:1].lower()}{staff['Carer'][carer]['lname'].lower()}"] = Employee(staff["Carer"][carer])
    """staffdict = {
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
    }"""
    """staffkeys = list(staffdict.keys())
    random.SystemRandom().shuffle(staffkeys)
    staffObject = {}
    for key in staffkeys:
        staffObject[key] = staffdict[key]"""
    staffObject = myDictRandom(staffdict)
    return staffObject

def getStaffList(sent_period, staffdict):
    stafflist = []
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
    elif sent_period.lower() == "pm":
        for staff_ in staffdict:
            staff = staffdict[staff_]
            if staff.pm == True:
                if staff.shiftsLeft() == 0:
                    continue
                else:
                    stafflist.append(staff_)
            else:
                continue
    newlist = []
    for value in sorted(stafflist, key=lambda _: random.random()):
        newlist.append(value)
    random.SystemRandom().shuffle(newlist)
    return newlist


def checkErrors(staffObject):
    errors = 0 
    for staff in staffObject:
        details = staffObject[staff].week()
        count = 0
        prev = None
        for x in details.keys():
            if count == 0:
                prev = details[x]
                count += 1
            else:
                if details[x] is None:
                    prev = details[x]
                    continue
                else:
                    if prev == details[x]:
                        prev = details[x]
                        errors += 1    
                    else:
                        prev = details[x]
                        continue
    return errors



        

