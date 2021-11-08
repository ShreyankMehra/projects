import filehandling as fh
fh=fh.fh()


def login_member(di):

    mobile = input("enter mobile no :").strip()
    try:
        int(mobile)
    except:
        print("wrong input !!")
        return ""
    else:
        if not mobile:
            print("no input!!")
            return ""



    for i in di:
        if mobile == di[i]['mobile']:

            passw = input("enter your password here :").strip()
            if passw == di[i]['password']:
                print("login successfuly!!")
                return i
            else:
                print("wrong password !!")
                return 0

    print("no member found")



def create_members(di):
    name = input("enter name to create :").strip()
    if not name:
        print("no input!!")
        return ""

    if name in di:
        print("member already exist!!")
        return ""

    while True:
        age = input("enter age no :").strip()
        try:
            int(age)
        except:
            print("wrong input !!")
        else:
            if not age:
                print("no input!!")
                continue
            else:
                break

    while True:
        gender = input("select gender male:1//female:2//other:3 :").strip()
        if not gender:
            print("no input!!")
            continue
        elif gender in ["1", '2', '3']:
            if gender == '1':
                gender = 'male'
            elif gender == '2':
                gender = 'female'
            else:
                gender = 'other'
            break
        else:
            print("wrong input")
    while True:
        mobile = input("enter mobile no :").strip()
        try:
            int(mobile)
        except:
            print("wrong input !!")
        else:
            if not mobile:
                print("no input!!")
                continue
            else:
                break
    email = input("enter email :").strip()
    while True:
        duration = input("select duration 1//3//6//12 :").strip()
        if not duration:
            print("no input!!")
            continue
        elif duration in ["1", '3', '6', '12']:
            break
        else:
            print("wrong input")

    while True:
        bmi = input("enter bmi no :").strip()
        try:
            int(bmi)
        except:
            print("wrong input !!")
        else:
            if not bmi:
                print("no input!!")
                continue
            else:
                break
    while True:
        passw=input("enter password for member:").strip()
        if not passw:
            print("no input !!!")
        else:
            break



    di[name] = {}
    di[name]["age"] = age
    di[name]["gender"] = gender
    di[name]["mobile"] = mobile
    di[name]["email"] = email
    di[name]["duration"] = duration
    di[name]['password']=passw

    di[name]["bmi"] = bmi
    fh.upd_members(di)
    print("member created successfully !!")

def find_bmi_regime(n,di):
    found = False
    for i in di:

        if n > i[0] and n<=i[1]:
            found=True
            print("\n :  Regimen  :")
            for j in di[i]:


                print(j, "-", di[i][j])
    if not found:
        print("regime for this bmi range is not created !!")


def view_member(di):
    if di:
        print(" : list of members : ")
        for i in di:
            print(": ",i," :")
    else:
        print("no memebers yet !!")
        return ""
    mobile = input("enter contact no of member for info :").strip()
    if not mobile:
        print("no input")
        return ""

    for i in di:

        if mobile == di[i]['mobile']:
            print(f"NAME : {i}")
            print(" : MEMBER INFO :")
            for j in di[i]:
                print(j, ":", di[i][j])

            return float(di[i]['bmi'])

    print("no member with this contact no !!")

def view_single_member(m,di):

    print(f"NAME : {m}")
    print(" : MEMBER INFO :")
    for j in di[m]:
        print(j, ":", di[m][j])

def del_member(di):
    mobile = input("enter contact no of member :").strip()
    if not mobile:
        print("no input")
        return ""

    found = False
    for i in di:

        if mobile == di[i]['mobile']:
            found = True
            print(f"NAME : {i}")
            print(" : MEMBER INFO :")
            for j in di[i]:
                print(j, ":", di[i][j])
            break
    if found:
        confirm=input("enter y/Y to delete member :").strip()
        if confirm in ['y','Y']:
            del di[i]
            fh.upd_members(di)
            print("deleted successfully!!")
    else:
        print("no member with this contact no !!")


def update_membership(di):
    if di:
        print(" : list of members : ")
        for i in di:
            print(": ", i, " :")
    else:
        print("no memebers yet !!")
        return ""
    mobile = input("enter contact no of member for info :").strip()
    if not mobile:
        print("no input")
        return ""
    found = False
    for i in di:
        found = True
        if mobile == di[i]['mobile']:
            print(f"NAME : {i}")
            print(" : MEMBER INFO :")
            for j in di[i]:
                print(j, ":", di[i][j])
            break
    if found:
        while True:
            duration = input("select new duration 1//3//6//12 :").strip()
            if not duration:
                print("no input!!")
                continue
            elif duration in ["1", '3', '6', '12']:
                break
            else:
                print("wrong input")

        di[i]["duration"] = duration
        fh.upd_members(di)
        print("updated successfully!!")
    else:
        print("member not found !!")

def update_password(di):
    if di:
        print(" : list of members : ")
        for i in di:
            print(": ",i," :")
    else:
        print("no memebers yet !!")
        return ""
    mobile = input("enter contact no of member for info :").strip()
    if not mobile:
        print("no input")
        return ""
    found=False
    for i in di:
        found=True
        if mobile == di[i]['mobile']:
            print(f"NAME : {i}")
            print(" : MEMBER INFO :")
            for j in di[i]:
                print(j, ":", di[i][j])
            break
    if found:
        while True:
            passw=input("enter password for member:").strip()
            if not passw:
                print("no input !!!")
            else:
                break
        di[i]["password"]=passw
        fh.upd_members(di)
        print("updated successfully!!")
    else:
        print("member not found !!")

def update_mobile(di):
    if di:
        print(" : list of members : ")
        for i in di:
            print(": ",i," :")
    else:
        print("no memebers yet !!")
        return ""
    mobile = input("enter contact no of member for info :").strip()
    if not mobile:
        print("no input")
        return ""
    found=False
    for i in di:
        found=True
        if mobile == di[i]['mobile']:
            print(f"NAME : {i}")
            print(" : MEMBER INFO :")
            for j in di[i]:
                print(j, ":", di[i][j])
            break
    if found:
        while True:
            mobile = input("enter new mobile no :").strip()
            try:
                int(mobile)
            except:
                print("wrong input !!")
            else:
                if not mobile:
                    print("no input!!")
                    continue
                else:
                    break
        di[i]["mobile"]=mobile
        fh.upd_members(di)
        print("updated successfully!!")
    else:
        print("member not found !!")

def change_mobile():
    while True:
        mobile = input("enter new mobile no :").strip()
        try:
            int(mobile)
        except:
            print("wrong input !!")
        else:
            if not mobile:
                print("no input!!")
                continue
            else:
                break
    return mobile


def change_email():
    email = input("enter new email :").strip()
    return email