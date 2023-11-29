def parse_dataset(dataset):
    departments = []
    rooms = {}
    beds = {}
    patients = {}

    lines = dataset.strip().split('\n')
    current_section = None

    for line in lines:
        words = line.split()

        if not words:
            continue

        if words[0] in ['DEPARTMENTS:', 'ROOMS:', 'BEDS:', 'PATIENTS:']:
            current_section = words[0].rstrip(':')
            continue

        if current_section == 'DEPARTMENTS':
            if words[0] == 'END.':
                break

            department_id, department_name = words
            departments.append((int(department_id), department_name))

        elif current_section == 'ROOMS':
            if words[0] == 'END.':
                break

            room_id = words[0]
            room_name = ' '.join(words[1:-3])
            room_capacity = words[-3]
            room_department = words[-1]

            rooms[room_id] = {'name': room_name, 'capacity': int(room_capacity), 'department': int(room_department)}

        elif current_section == 'BEDS':
            if words[0] == 'END.':
                break

            bed_id, bed_room_id = words
            beds[bed_id] = {'room': bed_room_id}

        elif current_section == 'PATIENTS':
            if words[0] == 'END.':
                break

            patient_id, patient_name, patient_age, patient_gender, patient_admission_day, patient_discharge_day = words
            patients[int(patient_id)] = {
                'name': patient_name,
                'age': int(patient_age),
                'gender': patient_gender,
                'admission_day': int(patient_admission_day),
                'discharge_day': int(patient_discharge_day)
            }

    return departments, rooms, beds, patients


