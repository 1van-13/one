def data_entry():
    data_log = []
    N = int(input())
    a = ''
    b = []
    for i in range(0,N):
        a = input()
        b.append(a.split(' '))
        data_log += b
        b = []
    return [N, data_log]
def in_seconds(data_log):
    p = 0
    new_data_log = []
    l = []
    for i in data_log:
        p = 1440 * int(i[0]) + 60 * int(i[1]) + int(i[2])
        l.append(p)
        l = l + i[3:5]
        new_data_log.append(l)
        p = 0
        l = []
    return new_data_log
def  unique_idex(data_log):
    data_index = []
    c = ''
    for i in data_log:
        if not(i[1] in data_index):
            data_index.append(i[1])
    return data_index
def main():
    N = 0
    data_log = []
    data_index = []
    N,data_log = data_entry()
    print(N,data_log)
    data_log = in_seconds(data_log)
    print(N,data_log)
    data_index = unique_idex(data_log)
    print(data_index,'Вот оно')
main()
