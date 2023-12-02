from csp import *
from hospital_parser import parse_dataset
import time

# Start time of execution
start_time = time.time()

# Define Domains for Variables
Domain = {}

B = {'b{}'.format(i) for i in range(1, 17)}  # Quantity of beds
S = {'S.{:02d}'.format(i) for i in range(0, 30)}  # Quantity of slots
P = {'p{}'.format(i) for i in range(1, 40)}  # Quantity of patients
Ab = {0, 1}  # Bed occupied
Rps = {'Rps.{:02d}'.format(i) for i in range(0, 30)}  # Start day of the month bed is occupied
Rpd = {'Rpd.{:02d}'.format(i) for i in range(0, 20)}  # Days bed is occupied
Xpb = {0, 1}  # Patient occupies bed

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


patients_matrix = [[0 for _ in beds] for _ in patients]

# Populate the matrix based on patient-bed assignments
for p in patients:
    for b in beds:
        patients_matrix[p - 1][int(b[1:]) - 1] = (p, b) in Xpb




#region Constraints

class PatientBedAssignmentConstraint(Constraint):
    def __init__(self, patients, beds):
        super().__init__([(p, b) for p in patients for b in beds])
        self.patients = patients
        self.beds = beds

    def satisfied(self, assignment):
        for p in self.patients:
            bed_assigned = [assignment[(p, b)] for b in self.beds]
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


# endregion

restrictions.append(PatientBedAssignmentConstraint(patients, beds))
restrictions.append(RoomGenderLimitationConstraint(rooms, patients))


class_scheduling = NaryCSP(Domain, *restrictions)
dict_solver = ac_solver(class_scheduling, arc_heuristic=sat_up)
print(dict_solver)
print("--- %s seconds ---" % (time.time() - start_time))
