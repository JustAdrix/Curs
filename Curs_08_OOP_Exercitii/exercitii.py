x = 0
while x == 0:
    a = int(input('INtroduceti un numar : '))
    suma = 0
    str = "473 1035 547 93 507 130 633 425 137 231 851 429 1004 1221 1156 1256 403 302 769 691 285 197 703 116 80 627 810 109 1164 459 844"
    lst = str.split()
    n = len(lst)
    for lst_re in lst:
        if a > n:
            # print('Numarul introdul depasesta numarul elementelor din lista')
            raise Exception('Numarul introdul este mai mare decat numarul elementelor din lista')
            # raise Exception('Numarul introdus este mai mare decat numarul elementelor din lista!!!')

        else:
            a -= 1
            if a >= 0:
                lst_nr = lst_re.replace("'", "")
                suma += int(lst_nr)
            else:
                break
    print(suma)
