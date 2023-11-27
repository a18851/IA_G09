from hospital_parser import parse_dataset

#region Import
with open("dataset.txt", "r") as file:
    dataset = file.read()

departments, rooms, beds, patients = parse_dataset(dataset)

#endregion

