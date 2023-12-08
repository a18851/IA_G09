import time
from csp import *
from dataset_parser import dataset_parser
from graph import create_gantt_chart


# with open("dataset.txt", "r") as file:
#     dataset = file.read()
#     bed_rooms, room_departments, patients_data = dataset_parser(dataset)

    

bed_rooms = {
    1: "11",
    2: "11",
    3: "12",
    4: "12",
    5: "21",
    6: "21",
    7: "22",
    8: "22"
}

room_departments = {
    11: {
        "name": "R11",
        "capac": 2,
        "dept": 1,
        "telemetry": 1,
        "oxygen": 0
    },
    12: {
        "name": "R12",
        "capac": 2,
        "dept": 1,
        "telemetry": 1,
        "oxygen": 1
    },
    21: {
        "name": "R21",
        "capac": 2,
        "dept": 2,
        "telemetry": 1,
        "oxygen": 0
    },
    22: {
        "name": "R22",
        "capac": 2,
        "dept": 2,
        "telemetry": 1,
        "oxygen": 1
    }
}


patients_data = {
    1: {
        "age": 98,
        "gender": "M",
        "admission_day": 0,
        "discharge_day": 0,
        "dept": 0,
        "telemetry": 0,
        "oxygen": 0
    },
    2: {
        "age": 82,
        "gender": "M",
        "admission_day": 0,
        "discharge_day": 5,
        "dept": 1,
        "telemetry": 1,
        "oxygen": 1
    },
    3: {
        "age": 43,
        "gender": "M",
        "admission_day": 0,
        "discharge_day": 1,
        "dept": 0,
        "telemetry": 0,
        "oxygen": 0
    },
    4: {
        "age": 88,
        "gender": "F",
        "admission_day": 0,
        "discharge_day": 4,
        "dept": 1,
        "telemetry": 0,
        "oxygen": 0
    },
    5: {
        "age": 20,
        "gender": "M",
        "admission_day": 0,
        "discharge_day": 3,
        "dept": 2,
        "telemetry": 0,
        "oxygen": 1
    },
    6: {
        "age": 65,
        "gender": "F",
        "admission_day": 0,
        "discharge_day": 1,
        "dept": 0,
        "telemetry": 0,
        "oxygen": 0
    },
    7: {
        "age": 33,
        "gender": "F",
        "admission_day": 1,
        "discharge_day": 7,
        "dept": 1,
        "telemetry": 1,
        "oxygen": 0
    },
    8: {
        "age": 86,
        "gender": "F",
        "admission_day": 2,
        "discharge_day": 3,
        "dept": 0,
        "telemetry": 0,
        "oxygen": 0
    },
    9: {
        "age": 22,
        "gender": "M",
        "admission_day": 2,
        "discharge_day": 5,
        "dept": 1,
        "telemetry": 0,
        "oxygen": 1
    },
    10: {
        "age": 70,
        "gender": "F",
        "admission_day": 3,
        "discharge_day": 10,
        "dept": 2,
        "telemetry": 1,
        "oxygen": 0
    },
    11: {
        "age": 42,
        "gender": "M",
        "admission_day": 4,
        "discharge_day": 10,
        "dept": 2,
        "telemetry": 1,
        "oxygen": 1
    },
    12: {
        "age": 3,
        "gender": "F",
        "admission_day": 5,
        "discharge_day": 11,
        "dept": 1,
        "telemetry": 0,
        "oxygen": 0
    },
    13: {
        "age": 14,
        "gender": "F",
        "admission_day": 5,
        "discharge_day": 12,
        "dept": 2,
        "telemetry": 0,
        "oxygen": 1
    },
    14: {
        "age": 78,
        "gender": "M",
        "admission_day": 7,
        "discharge_day": 13,
        "dept": 1,
        "telemetry": 0,
        "oxygen": 0
    },
    15: {
        "age": 29,
        "gender": "F",
        "admission_day": 8,
        "discharge_day": 9,
        "dept": 0,
        "telemetry": 1,
        "oxygen": 0
    },
    16: {
        "age": 61,
        "gender": "M",
        "admission_day": 9,
        "discharge_day": 15,
        "dept": 1,
        "telemetry": 0,
        "oxygen": 0
    },
    17: {
        "age": 56,
        "gender": "M",
        "admission_day": 10,
        "discharge_day": 17,
        "dept": 2,
        "telemetry": 0,
        "oxygen": 1
    },
    18: {
        "age": 106,
        "gender": "F",
        "admission_day": 10,
        "discharge_day": 14,
        "dept": 1,
        "telemetry": 1,
        "oxygen": 0
    },
    19: {
        "age": 4,
        "gender": "F",
        "admission_day": 11,
        "discharge_day": 17,
        "dept": 2,
        "telemetry": 1,
        "oxygen": 0
    },
    20: {
        "age": 52,
        "gender": "F",
        "admission_day": 12,
        "discharge_day": 19,
        "dept": 1,
        "telemetry": 1,
        "oxygen": 1
    }
}

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
