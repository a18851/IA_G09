import time
from csp import *
from dataset_parser import dataset_parser
from graph import create_gantt_chart


with open("dataset.txt", "r") as file:
    dataset = file.read()
    bed_rooms, room_departments, patients_data = dataset_parser(dataset)

#Variables

beds = [f'bed{i}' for i in range(1, 9)]
patients = [f'patient{i}' for i in range(1, len(patients_data) + 1)]
domains = {f'patient{i}': set(range(1, 9)) for i in range(1, 21)}

# Department
for p in range(1, len(patients_data) + 1):
    for room_number, room_info in room_departments.items():
        if patients_data[p]['dept'] == 1 and room_info['dept'] == 2:
            matching_beds = [bed_number for bed_number, value in bed_rooms.items() if value == str(room_number)]
            for bed_number in matching_beds:
                domains[f"patient{p}"].discard(bed_number)
        elif patients_data[p]['dept'] == 2 and room_info['dept'] == 1:
            matching_beds = [bed_number for bed_number, value in bed_rooms.items() if value == str(room_number)]
            for bed_number in matching_beds:
                domains[f"patient{p}"].discard(bed_number)


## Telemetry
for p in range(1, len(patients_data) + 1):
    for room_number, room_info in room_departments.items():
         if room_info['telemetry'] == 0 and patients_data[p]['telemetry'] == 1:
             matching_beds = [bed_number for bed_number, value in bed_rooms.items() if value == str(room_number)]
             for bed_number in matching_beds:
                 domains[f"patient{p}"].discard(bed_number)



# Oxygen
for p in range(1, len(patients_data) + 1):
    for room_number, room_info in room_departments.items():
        if room_info['oxygen'] == 0 and patients_data[p]['oxygen'] == 1:
            matching_beds = [bed_number for bed_number, value in bed_rooms.items() if value == str(room_number)]
            for bed_number in matching_beds:
                domains[f"patient{p}"].discard(bed_number)
                


constraints = []

#Constraint_day
for p1 in range(1, len(patients) + 1):
    for p2 in range(1, len(patients) + 1):
        if p1 != p2 and not (patients_data[p1]['admission_day'] >= patients_data[p2]['discharge_day'] or patients_data[p2]['admission_day'] >= patients_data[p1]['discharge_day']):
            constraints.append(Constraint([f'patient{p1}', f'patient{p2}'], lambda a, b: a != b))

# constraints.append(Constraint([f'patient{1}', f'patient{2}'], lambda a, b: a != b))
# constraints.append(Constraint([f'patient{1}', f'patient{3}'], lambda a, b: a != b))
# constraints.append(Constraint([f'patient{1}', f'patient{4}'], lambda a, b: a != b))
# constraints.append(Constraint([f'patient{1}', f'patient{5}'], lambda a, b: a != b))
# constraints.append(Constraint([f'patient{1}', f'patient{6}'], lambda a, b: a != b))

# for domain_key, domain_value in domains.items():
#     print(domain_key, domain_value)

# Impressão das constraints formatadas
print("# Constraint: Pacientes não podem ocupar a mesma cama simultaneamente")
for constraint in constraints:
    print(constraint)

#Genero
# for p1 in range(1, len(patients) + 1):
#      for p2 in range(1, len(patients) + 1):
#          if p1 != p2 and not(patients_data[p1]["gender"] == patients_data[p2]["gender"]):
#              constraints.append(Constraint([f'patient{p1}', f'patient{p2}'], lambda a, b: a != b))

# Create CSP instance
csp = NaryCSP(domains, constraints)

# Find a solution using AC solvers
solution = ac_solver(csp, arc_heuristic=sat_up)
print(solution)

create_gantt_chart(solution, bed_rooms, patients_data)
