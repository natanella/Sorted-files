from pprint import pprint

def read_file(folder, *files):
    data_list = []
    for file in files:
        path = folder + '\\' + file
        with open(path, encoding='utf-8') as f:
            data = f.read().split('\n')
        data.insert(0, str(len(data)))
        data.insert(0, file)
        data_list.append(data)

    sorted_data = sorted(data_list, key=lambda x: len(x))
    
    with open('result.txt', 'a', encoding='utf-8') as f:
        for el in sorted_data:
            for line in el:
                f.write(line+'\n')

read_file('files', '1.txt', '2.txt', '3.txt')