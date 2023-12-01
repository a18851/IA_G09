from csp import *
from utils import *
from main import *


# Define Domains for Variables
B = {'b1', 'b2', ..., 'bm'}
D = {'d1', 'd2', ..., 'dn'}
N = {'n1', 'n2', ..., 'nk'}
S = {'S.01', 'S.02', ..., 'S.24'}
P = {'p1', 'p2', ..., 'pq'}
Ab = {0, 1}
Ad = {0, 1}
An = {0, 1}
Rp = set()
Xpb = {0, 1}
Ypd = {0, 1}
Ypn = {0, 1}



class PatientBedAssignmentConstraint(Constraint):
    def __init__(self, patients, beds):
        super().__init__(patients)
        self.beds = beds

    def satisfied(self, assignment):
        for p in self.variables:
            bed_assigned = [assignment[Xpb[p, b]] for b in self.beds]
            if sum(bed_assigned) != 1:
                return False
        return True

class RoomGenderLimitationConstraint(Constraint):
    def __init__(self, rooms, patients):
        super().__init__(patients)
        self.rooms = rooms

    def satisfied(self, assignment):
        for p in self.variables:
            # Verifique se o paciente está no dicionário antes de acessar para evitar erros
            if p in patients:
                patient_gender = patients[p]['gender']
                room_gender_variable = self.room_gender_variable(p)  # Substitua com o método real
                room_gender = assignment.get(room_gender_variable)  # Usando get para evitar KeyError

                if room_gender is not None:
                    if room_gender == "female" and patient_gender != "female":
                        return False
                    elif room_gender == "male" and patient_gender != "male":
                        return False
                else:
                    print(f"Room gender variable not found for patient {p}.")
            else:
                print(f"Patient with ID {p} not found.")

        return True


# class EquipmentRoomAssignmentConstraint(Constraint):
#     def __init__(self, patients, rooms):
#         super().__init__(patients)
#         self.rooms = rooms

#     def satisfied(self, assignment):
#         for p in self.variables:
#             required_equipment = get_required_equipment(p)  # Replace with actual function
#             assigned_room = assignment[patient_room_variable(p)]  # Replace with actual variable

#             if required_equipment not in assigned_room_equipment(assigned_room):
#                 return False

#         return True

class DepartmentSpecializationConstraint(Constraint):
    def __init__(self, patients, departments):
        super().__init__(patients)
        self.departments = departments

    def satisfied(self, assignment):
        for p in self.variables:
            patient_department = assignment[patient_department_variable(p)]  # Replace with actual variable
            assigned_department = get_assigned_department(p)  # Replace with actual function

            if assigned_department != patient_department:
                return False

        return True

class DepartmentAgeLimitConstraint(Constraint):
    def __init__(self, patients, departments):
        super().__init__(patients)
        self.departments = departments

    def satisfied(self, assignment):
        for p in self.variables:
            patient_age = get_patient_age(p)  # Replace with actual function
            assigned_department = assignment[patient_department_variable(p)]  # Replace with actual variable

            min_age_limit = get_min_age_limit(assigned_department)  # Replace with actual function
            max_age_limit = get_max_age_limit(assigned_department)  # Replace with actual function

            if not (min_age_limit <= patient_age <= max_age_limit):
                return False

        return True

class PatientAcuityLevelConstraint(Constraint):
    def __init__(self, patients):
        super().__init__(patients)

    def satisfied(self, assignment):
        for p in self.variables:
            patient_acuity = get_patient_acuity(p)  # Replace with actual function
            assigned_room_acuity = assignment[patient_room_acuity_variable(p)]  # Replace with actual variable

            if assigned_room_acuity < patient_acuity:
                return False

        return True
