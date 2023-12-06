import time
from csp import *

start_time = time.time()



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
        "name": "R22",
        "capac": 2,
        "dept": 2,
        "telemetry": 1,
        "oxygen": 0
    },
    22: {
        "name": "R23",
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
        "dept": 0,
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

days = [f'day{i}' for i in range(0, 20)]
beds = [f'bed{i}' for i in range(1, 9)]
patients = [f'patient{i}' for i in range(1, len(patients_data))]


domains = {
    'patient1':  {1, 2, 3, 4, 5, 6, 7, 8},
    'patient2':  {1, 2, 3, 4, 5, 6, 7, 8},
    'patient3':  {1, 2, 3, 4, 5, 6, 7, 8},
    'patient4':  {1, 2, 3, 4, 5, 6, 7, 8},
    'patient5':  {1, 2, 3, 4, 5, 6, 7, 8},
    'patient6':  {1, 2, 3, 4, 5, 6, 7, 8},
    'patient7':  {1, 2, 3, 4, 5, 6, 7, 8},
    'patient8':  {1, 2, 3, 4, 5, 6, 7, 8},
    'patient9':  {1, 2, 3, 4, 5, 6, 7, 8},
    'patient10': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient11': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient12': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient13': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient14': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient15': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient16': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient17': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient18': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient19': {1, 2, 3, 4, 5, 6, 7, 8},
    'patient20': {1, 2, 3, 4, 5, 6, 7, 8},
}


for p in range(1, len(patients_data) + 1):
    if patients_data[p]['dept'] == 1:
        domains[f"patient{p}"] = {1, 2, 3, 4}
    elif patients_data[p]['dept'] == 2:
        domains[f"patient{p}"] = {5, 6, 7, 8}

constraints = []

for p1 in range(1, len(patients) + 1):
    for p2 in range(1, len(patients) + 1):
        if p1 != p2 and not (patients_data[p1]['admission_day'] > patients_data[p2]['discharge_day'] or patients_data[p2]['admission_day'] > patients_data[p1]['discharge_day']):
            constraints.append(Constraint([f'patient{p1}', f'patient{p2}'], lambda a, b: a != b))

# Create CSP instance
csp = NaryCSP(domains, constraints)

# Find a solution using AC solvers
solution = ac_solver(csp, arc_heuristic=sat_up)
print("--- {:.2f} seconds ---".format(time.time() - start_time))
print(solution)
