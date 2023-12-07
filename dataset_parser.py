def dataset_parser(dataset):
    bed_rooms = {}
    room_departments = {}
    patients_data = {}

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

        elif current_section == 'ROOMS':
            if words[0] == 'END.':
                break

            room_id = int(words[0])
            room_name = ' '.join(words[1:-5])
            room_capacity = int(words[-5])
            room_department = int(words[-3])
            telemetry = int(words[-2])
            oxygen = int(words[-1])

            room_departments[room_id] = {
                'name': room_name,
                'capac': room_capacity,
                'dept': room_department,
                'telemetry': telemetry,
                'oxygen': oxygen
            }

        elif current_section == 'BEDS':
            if words[0] == 'END.':
                break

            bed_id, bed_room_id = map(int, words)
            bed_rooms[bed_id] = bed_room_id

        elif current_section == 'PATIENTS':
            if words[0] == 'END.':
                break

            patient_id, patient_name, patient_age, patient_gender, admission_day, discharge_day, dept, telemetry, oxygen = map(int, words)
            patients_data[patient_id] = {
                'name': patient_name,
                'age': patient_age,
                'gender': patient_gender,
                'admission_day': admission_day,
                'discharge_day': discharge_day,
                'dept': dept,
                'telemetry': telemetry,
                'oxygen': oxygen
            }

    return bed_rooms, room_departments, patients_data
