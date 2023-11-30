from hospital_parser import parse_dataset
from hospital_constraints import *
from csp import *
from utils import *
from main import *

#region Import
with open("dataset.txt", "r") as file:
    dataset = file.read()

departments, rooms, beds, patients = parse_dataset(dataset)

#endregion

# Create a CSP instance
csp = CSP()

#Variables
csp.add_variables(list(Xpb.keys()))
csp.add_variables(list(Ypd.keys()))
csp.add_variables(list(Ypn.keys()))

#Constraints
csp.add_constraint(PatientBedAssignmentConstraint(patients, beds))
csp.add_constraint(RoomGenderLimitationConstraint(rooms, patients))
csp.add_constraint(EquipmentRoomAssignmentConstraint(patients, rooms))
csp.add_constraint(DepartmentSpecializationConstraint(patients, departments))
csp.add_constraint(DepartmentAgeLimitConstraint(patients, departments))
csp.add_constraint(PatientAcuityLevelConstraint(patients))

# Create a Problem instance and solve
initial_state = {}  # Initial assignment state
problem = HospitalSchedulingProblem(initial_state)
solution = problem.backtracking_search(csp)

# Print or handle the solution as needed
print("Solution:", solution)
