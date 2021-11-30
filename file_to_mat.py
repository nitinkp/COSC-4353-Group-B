import os

inputs_list = []


def file_to_matrix(folder_input, num):
    for f1, f2, f3 in os.walk(folder_input):
        for file in f3:
            inputs_list.append(os.path.join(f1, file))

    file_name = ""

    for i in range(num):
        # print(i)
        try:
            file_name = inputs_list[i + 1]
        except:
            print("Provide input from given files")

    cons = ""

    try:
        with open(file_name) as r:
            try:
                cons = r.read()
            except:
                print("no contents")
                pass
    except:
        print("no file input")
        pass

    li = cons.split('\n')
    li2 = [e.split(',') for e in li]
    g = []
    for e in li2:
        li4 = []
        for j in e:
            li4.append(int(j))
        g.append(li4)
    return g
