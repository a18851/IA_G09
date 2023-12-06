import time
from csp import *

start_time = time.time()

bed_rooms = {
    1: 11,
    2: 11,
    3: 12,
    4: 12,
    5: 21,
    6: 21,
    7: 22,
    8: 22
}

room_departments = {
    11: 1,
    12: 1,
    21: 2,
    22: 2
}

patients_data = {
    1: {
        "age": 98,
        "gender": "M",
        "admission_day": 0,
        "discharge_day": 0
    },
    2: {
        "age": 82,
        "gender": "M",
        "admission_day": 0,
        "discharge_day": 5
    },
    3: {
        "age": 43,
        "gender": "M",
        "admission_day": 0,
        "discharge_day": 1
    },
    4: {
        "age": 88,
        "gender": "M",
        "admission_day": 0,
        "discharge_day": 4
    },
    5: {
        "age": 20,
        "gender": "F",
        "admission_day": 0,
        "discharge_day": 3
    },
    6: {
        "age": 65,
        "gender": "F",
        "admission_day": 0,
        "discharge_day": 1
    },
    7: {
        "age": 33,
        "gender": "F",
        "admission_day": 1,
        "discharge_day": 7
    },
    8: {
        "age": 86,
        "gender": "M",
        "admission_day": 2,
        "discharge_day": 3
    },
    9: {
        "age": 22,
        "gender": "F",
        "admission_day": 2,
        "discharge_day": 5
    },
    10: {
        "age": 70,
        "gender": "F",
        "admission_day": 3,
        "discharge_day": 10
    },
    11: {
        "age": 42,
        "gender": "M",
        "admission_day": 4,
        "discharge_day": 10
    },
    12: {
        "age": 3,
        "gender": "F",
        "admission_day": 5,
        "discharge_day": 11
    },
    13: {
        "age": 14,
        "gender": "F",
        "admission_day": 5,
        "discharge_day": 12
    },
    14: {
        "age": 78,
        "gender": "M",
        "admission_day": 7,
        "discharge_day": 13
    },
    15: {
        "age": 29,
        "gender": "F",
        "admission_day": 8,
        "discharge_day": 9
    },
    16: {
        "age": 61,
        "gender": "F",
        "admission_day": 9,
        "discharge_day": 15
    },
    17: {
        "age": 56,
        "gender": "F",
        "admission_day": 10,
        "discharge_day": 17
    },
    18: {
        "age": 106,
        "gender": "F",
        "admission_day": 10,
        "discharge_day": 14
    },
    19: {
        "age": 4,
        "gender": "M",
        "admission_day": 11,
        "discharge_day": 17
    },
    20: {
        "age": 52,
        "gender": "F",
        "admission_day": 12,
        "discharge_day": 19
    }
}

#Variables

days = [f'day{i}' for i in range(0, 20)]
beds = [f'bed{i}' for i in range(1, len(bed_rooms))]
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


constraints = []

def day_assignment(patients):
    for p1 in patients:
        for p2 in patients:
            if p1 != p2:
                constraints.append(Constraint(patients, lambda a = patients_data[p1]['admission_day'], b = patients_data[p2]['discharge_day'] , c= patients_data[p2]['admission_day'], d= patients_data[p1]['discharge_day']: a > b or c > d))


# Create CSP instance
csp = NaryCSP(domains, constraints)

# # Find a solution using AC solver
solution = ac_solver(csp, arc_heuristic=sat_up)
print("--- {:.2f} seconds ---".format(time.time() - start_time))
print(solution)
