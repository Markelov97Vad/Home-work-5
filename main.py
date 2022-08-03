from Name import add_cild, out_child, mark_child

dict = {}
numb = 1

while True:
    comnd = input("Введите комманду:").split()
    if comnd[0] == "exit":
        break
    elif comnd[0] == "add":
        dict = add_cild(comnd[1] + " " + comnd[2], numb,  dict)
        numb += 1
    elif comnd[0] == "all":
        out_child(dict)
    elif comnd[0] == "mark":
        dict = mark_child(int(comnd[1]), int(comnd[2]), dict)
    else:
        print("Не понял! Повторите команду!")