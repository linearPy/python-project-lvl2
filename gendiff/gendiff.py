import json


def generate_diff(first_path, second_path):
    with open(first_path) as file1, open(second_path) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

        keys = sorted(data1.keys() | data2.keys())
        result = []

        for key in keys:
            if key in data1 and key not in data2:
                result.append(f'  - {key}: {data1[key]}')
            elif key in data2 and key not in data1:
                result.append(f'  + {key}: {data2[key]}')
            elif data1[key] == data2[key]:
                result.append(f'    {key}: {data1[key]}')
            else:
                result.append(f'  - {key}: {data1[key]}')
                result.append(f'  + {key}: {data2[key]}')

    return '{\n' + '\n'.join(result) + '\n}'
