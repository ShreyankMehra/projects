# view bmi#view workout regimen
import filehandling as fh
fh=fh.fh()

def login_su(di):
    name=input("enter your name :").strip()
    if name in di:
        passw=input("enter your password here :" ).strip()
        if passw == di[name]:
            print("login successfuly!!")
            return 1
        else:
            print("wrong password !!")
            return 0
    else:
        print("wrong username !!")
        return 0

def create_su(di):
    name = input("enter your name :").strip()
    if name in di:
        print("superuser already exist!!")



    elif name:
        passw = input("create password :").strip()
        if passw:
            print("superuser created !!")
            di[name] = passw
            fh.upd_user(di)
        else:
            print("no input!!")
    else:
        print("no input!!")

def view_bmi(di):
    for i in di:
        print(":", f"{i[0]}<BMI<={i[1]} :")

def viewregime(di):
    if di:
        view_bmi(di)
        n = input("select bmi range for regimen seperated by coma:").split(',')
        try:
            n = [float(i) for i in n]
        except:
            print("wrong input!!")
            return ""
        n = tuple(n)
        if n in di:
            print("regimen for this bmi :")
            for i in di:
                if n == i:
                    for j in di[i]:
                        print(j, "-", di[i][j])
        else:
            print("regime for this bmi range is not created !!")
    else:
        print("no regimen created yet!!")

def create_regimen(di):
    temp_range=input("enter bmi range for regimen seperated by coma :").split(',')
    try:
        temp_range=[float(i.strip()) for i in temp_range]
    except:
        print("wrong input!!")
        return ""
    temp_range=tuple(temp_range)
    if len(temp_range)==2 and temp_range[0]<temp_range[1]:
        t=True
        for i in temp_range:
            for j in di:
                if j[0]<i and i<=j[1]:
                    print('regimen For this range already exist.')
                    t=False
                    break
            if t==False:
                break
        if t:
            print(f'BMI for range {temp_range[0]} to {temp_range[1]} is created!!')
            di[temp_range]={"Mon": "Chest", "Tue": "Biceps",
                               "Wed": "Rest", "Thu": "Back",
                               "Fri": "Triceps", "Sat": "Rest","Sun": "Rest"}
            fh.upd_bmi(di)


    else:
        print("wrong input !!")

def del_regimen(di):
    if di:

        view_bmi(di)
    else:
        print("no regimen created yet!!")
        return""
    n = input("select bmi range for regimen seperated by coma:").split(',')
    try:
        n = [float(i) for i in n]
    except:
        print("wrong input!!")
        return ""

    n = tuple(n)
    if n in di:
        print("regimen for this bmi :")
        for i in di:
            if n == i:
                for j in di[i]:
                    print(j, "-", di[i][j])
        n1 = input("enter y/Y to confirm deletion :")
        if n1 in ['y', 'Y']:
            del di[n]
            print("deleted successfully!!")
            fh.upd_bmi(di)
        else:
            print('not deleted!!')
    else:
        print("regime for this bmi range does not exist !!")

def update_regimen(di):
    if di:
        view_bmi(di)
    else:
        print("no regimen created yet!!")

    n = input("select bmi range for regimen seperated by coma:").split(',')
    try:
        n = [float(i) for i in n]
    except:
        print("wrong input!!")
        return ""
    n = tuple(n)
    if n in di:
        print("regimen for this bmi :")
        for i in di:
            if n == i:
                for j in di[i]:
                    print(j, "-", di[i][j])

        m = input("select day to edit in regimen :")
        if m in di[n]:
            n1 = input(f"enter new regimen for {m}day :")
            di[n][m] = n1
            fh.upd_bmi(di)
            print("updated succesfully")
        else:
            print("wrong input")







    else:
        print("regime for this bmi range is not created !!")



