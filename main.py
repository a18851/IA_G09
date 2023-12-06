from csp import *
from hospital_parser import parse_dataset
import time


# Define variables
patients = [f'patient{i}' for i in range(1, 9)]
beds = [f'bed{i}' for i in range(1, 9)]
rooms = [f'room{i}' for i in range(1, 5)]
departments = [f'department{i}' for i in range(1, 3)]
variables = set(patients + beds + rooms + departments)

# Parse the dataset variables
with open("dataset.txt", "r") as file:
    dataset = file.read()

departments, rooms, beds, patients = parse_dataset(dataset)

#Domain
domain ={}
domain.update(departments)
domain.update(rooms)
domain.update(beds)
domain.update(patients)

#region Constraints

def unique_assignment(*args):
    return len(set(args)) == len(args)


constraints = [
    Constraint(patients, unique_assignment),
]

#endregion


#Algorithm Execution
hospital_scheduling = NaryCSP(domain, constraints)
solver = ac_solver(hospital_scheduling, arc_heuristic=sat_up)

print(solver)
print("--- %s seconds ---" % (time.time()))