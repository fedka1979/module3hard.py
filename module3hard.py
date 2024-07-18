data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(structure):
    numbers = 0
    strings = 0

    if isinstance(structure, int):
        numbers += structure
    elif isinstance(structure, str):
        strings += len(structure)
    elif isinstance(structure, (list, tuple, set)):
        for item in structure:
            numbers += calculate_structure_sum(item)
    elif isinstance(structure, dict):
        for key, value in structure.items():
            numbers += calculate_structure_sum(key)
            strings += calculate_structure_sum(value)

    return numbers + strings


result = calculate_structure_sum(data_structure)
print(result)