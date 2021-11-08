import filehandling
import menus
import input
import crudregime as reg
import crudmemebers as mem
fh=filehandling.fh()
menu=menus.options()
inp=input.inp()


diuser=filehandling.fh().open_user()
dimembers=filehandling.fh().open_members()
dibmi=filehandling.fh().open_bmi()
while True: #main menu
    menu.m_m()
    n=inp.selop()

    if n=='0':  #exit
        print('Thankyou!!!')
        break

    if n=='1':  #superuser
        menu.create_suser_m()
        n=inp.selop()
        if n == '1':  # create superuser
            reg.create_su(diuser)



        if n== '2':  #login superuser
            login=reg.login_su(diuser)
            if login :

                while True:
                    menu.suser_m()  #superuser_menu
                    n=inp.selop()
                    if n=='0':
                        break

                    if n=='1': #create member
                       mem.create_members(dimembers)

                    if n=='2':  #view members
                        bmi=mem.view_member(dimembers)
                        if bmi != "" and bmi != None:
                            mem.find_bmi_regime(bmi,dibmi)

                    if n=='3': #delete member
                        mem.del_member(dimembers)

                    if n=="4": #update member
                        while True:
                            menu.su_members_m()
                            n=inp.selop()
                            if n=="0":
                                break
                            if n=="1": #udpate membership
                                mem.update_membership(dimembers)
                            if n=="2": #update password
                                mem.update_mobile(dimembers)
                            if n=="3":  #update mobile
                                mem.update_password(dimembers)






                    if n=='5':
                        reg.create_regimen(dibmi)
                    if n=='6':
                        reg.viewregime(dibmi)
                    if n=='7':
                        reg.del_regimen(dibmi)
                    if n=='8':
                        reg.update_regimen(dibmi)

    if n=='2': #member
        member = mem.login_member(dimembers)
        if member:
            while True:


                menu.members_m()
                n=inp.selop()
                if n=='0': #exit
                    break
                if n=='1':  #view my regimen
                    mem.find_bmi_regime(float(dimembers[member]['bmi']),dibmi)

                if n=='2': #view my profile
                    mem.view_single_member(member,dimembers)

                if n=='3': #update profile
                    while True:
                        menu.members_m2()
                        n=inp.selop()
                        if n=='0':
                            break
                        if n=="1":#change mobile
                            mobile=mem.change_mobile()
                            dimembers[member]['mobile']=mobile
                            fh.upd_members(dimembers)

                        if n=='2':#change email
                            email=mem.change_email()
                            dimembers[member]['email'] = email
                            fh.upd_members(dimembers)






















