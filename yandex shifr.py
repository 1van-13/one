def vvod():
    i = 1
    a =''
    data = []
    N = int(input())
    for i in range(0,N):
        a = str(input())
        data.append(a)
    return data
def fio_date(data):
    data_fio = []
    data_date = []
    f = ''
    v = ''
    fio = []
    date = []
    long_fio = []
    sss = []
    for d in data:
        sss = d.split(',')
        for i in range(0,3):
            f += sss[i]
        f = "".join(set(f))
        fio.append(f)
        long_fio.append(len(f))
        f =''
        for k in range(3,6):
            v += sss[k]
        date.append(v)
        v = ''
    return fio,date,long_fio
def first_letter(data):
    first_letter = []
    for i in data:
        r = i[0]
        r = ord(r) - ord('A') + 1
        first_letter.append(r)
    return first_letter
def day_month(date):
    a = ''
    date_dm = []
    for i in date:
        a = str(i)
        a = a[:(len(a)-4)]
        date_dm.append(a)
    return date_dm
def sum_day_month(date_dm):
    popa = 0
    suma = 0
    digit = 0
    sum_dm = []
    for namber in date_dm:
        popa = int(namber)
        suma = 0
        while popa > 0:
            digit = popa % 10
            suma = suma + digit
            popa = popa // 10
        sum_dm.append(suma)
    return sum_dm
def encoding (long_fio,summa_dm,first_lette):
    final = []
    cod = 0
    dl = 0
    for i in range(0,len(summa_dm)):
        cod = long_fio[i] + 256 *  int(first_lette[i]) + 64 * int(summa_dm[i])
        cod =hex(cod)
        cod = cod[2:]
        dl = len(cod) - 3
        cod = cod[dl:]
        cod = cod.upper()
        final.append(cod)
        cod = 0
    return final
def resalt (encod):
    for i in encod:
        print(i, end=' ')
def main():
    data = []
    fio = []
    date = []
    first_lette = []
    long_fio = []
    date_dm = []
    summa_dm = []
    encod = []
    data = vvod()
    fio,date,long_fio = fio_date(data)
    first_lette = first_letter(data)
    date_dm = day_month(date)
    summa_dm = sum_day_month(date_dm)
    encod = encoding (long_fio,summa_dm,first_lette)
    resalt(encod)
main()
