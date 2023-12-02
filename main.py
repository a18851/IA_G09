from csp import *
from hospital_parser import parse_dataset
import time

# start_time of execution
start_time = time.time()

# Define Domains for Variables
Domain = {}

B = {'b{}'.format(i) for i in range(1, 17)}  # qtt camas
S = {'S.{:02d}'.format(i) for i in range(0, 30)}  # qtt slots
P = {'p{}'.format(i) for i in range(1, 40)}  # qtt pacientes
Ab = {0, 1}  # cama ocupada
Rps = {'Rps.{:02d}'.format(i) for i in range(0, 30)}  # start dia mês cama ocupada
Rpd = {'Rpd.{:02d}'.format(i) for i in range(0, 20)}  # dias cama ocupada
Xpb = {0, 1}  # Paciente ocupa cama

Domain.update({
    'B': B,
    'S': S,
    'P': P,
    'Ab': Ab,
    'Rps': Rps,
    'Rpd': Rpd,
    'Xpb': Xpb
})

# Parse the dataset
with open("dataset.txt", "r") as file:
    dataset = file.read()

departments, rooms, beds, patients = parse_dataset(dataset)

restrictions = []

#region Constraints

# ...

class PatientBedAssignmentConstraint(Constraint):
    def __init__(self, patients, beds):
        super().__init__([Xpb[p, b] for p in patients for b in beds])
        self.patients = patients
        self.beds = beds

    def satisfied(self, assignment):
        for p in self.patients:
            bed_assigned = [assignment[Xpb[p, b]] for b in self.beds]
            if sum(bed_assigned) != 1:
                return False
        return True

class RoomGenderLimitationConstraint(Constraint):
    def __init__(self, rooms, patients):
        super().__init__([self.room_gender_variable(p) for p in patients])
        self.rooms = rooms
        self.patients = patients

    def satisfied(self, assignment):
        for p in self.patients:
            if p in patients:
                patient_gender = patients[p]['gender']
                room_gender_variable = self.room_gender_variable(p)  
                room_gender = assignment.get(room_gender_variable, None)

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
# ...



#endregion

restrictions.append(PatientBedAssignmentConstraint(patients, beds))
restrictions.append(RoomGenderLimitationConstraint(rooms, patients))


class_scheduling = NaryCSP(Domain, *restrictions)
dict_solver = ac_solver(class_scheduling, arc_heuristic=sat_up)
print(dict_solver)
print("--- %s seconds ---" % (time.time() - start_time))
