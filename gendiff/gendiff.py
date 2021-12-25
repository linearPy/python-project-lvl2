from gendiff.parser import deserialize


def generate_diff(first_path, second_path):
    data1 = deserialize(first_path)
    data2 = deserialize(second_path)

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

    return '{\n' + '\n'.join(result) + '\n}\n'
