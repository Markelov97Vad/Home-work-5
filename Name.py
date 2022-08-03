def add_cild(st, numb, dict):
    dict[numb] = {st : []}
    print("OK")
    return dict

def out_child(dict):
    for c1, v1 in dict.items():
        for c2, v2 in v1.items():
            if v2 == []:
                print(f"{c1}. {c2}")
            else:
                print(f"{c1}. {c2}", end = " ")
                for i in range(len(v2)):
                    if i == len(v2) - 1:
                        print(f"{v2[i]}", end = " ")
                    else:
                        print(f"{v2[i]},", end = " ")
                print("")

def mark_child(mark, numb, dict):
    for v in dict[numb].values():
        v.append(mark)
    print("OK")
    return dict