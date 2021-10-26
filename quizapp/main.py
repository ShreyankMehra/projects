import su,jsonfiles
from jsonfiles import filehandling
from su import mantop,manquiz,inputs




topics=su.mantop.options()
fh=filehandling.fh()
quiz=su.manquiz.options()

inp=su.inputs.inp()

diuser=filehandling.fh().open_user()
ditopic=filehandling.fh().open_topics()
diquiz=filehandling.fh().open_quizes()
ditaker=filehandling.fh().open_taker()

while True: #main menu
    topics.m_m()
    n1=inp.selop()

    if n1=='0':  #exit
        print('Thankyou!!!')
        break
    if n1=='1':  #superuser

        nsu=inp.selsuser()

        if nsu in diuser:


            while True: #superusermenue
                topics.suser_m()
                n2=inp.selop()

                if n2=='0':   #exit
                    break
                if n2=='1':   #managetopics

                    if diuser[nsu]['1']:
                        for i in diuser[nsu]['1']:
                            print(i)
                    else:
                        print("no topics yet")

                    while True:  #topic menu
                        topics.man_topics()
                        n3=inp.selop()
                        if n3=='0':   #Axit
                            break
                        if n3=='1':  #creaate topic


                            temp_topic=inp.cre_top()
                            if temp_topic not in diuser[nsu]['1'] and temp_topic:
                                diuser[nsu]['1'].append(temp_topic)
                                ditopic[temp_topic] = {'1': {}, '2': {}, '3': {}}
                                print('topic added !!')
                            else:
                                print("topic already exit or no input")






                        if n3=='2':   #read
                            if diuser[nsu]['1']:
                                for i in diuser[nsu]['1']:
                                    print(i)

                                temp_t = input("select topic : ").strip()
                                if temp_t in diuser[nsu]['1']:
                                    temp_diff = input("enter difficulty in 1,2,3 :")
                                    if temp_diff in ['1', '2', '3'] and ditopic[temp_t][temp_diff]:
                                        for ques in ditopic[temp_t][temp_diff]:
                                            print('--', ques)

                                            for i in ditopic[temp_t][temp_diff][ques]:
                                                print('-', i)
                                    else:
                                        print("invalid input or no questions available")
                                else:
                                    print("no topic like this")
                            else:
                                print("no topics yet")





                        if n3=='3':#update
                            while True:
                                topics.update_m()
                                n=inp.selop()
                                if n=='0':
                                    break
                                if n=='1':  #add question
                                    temp_t=input("select topic").strip()

                                    if  temp_t in diuser[nsu]['1']:
                                        temp_diff=input('enter diff in 1,2,3:').strip()
                                        if temp_diff in ditopic[temp_t]:
                                            l=len(ditopic[temp_t][temp_diff])
                                            l=str(l)
                                            question=input("question :")
                                            option =input("enter options giving space :").split()
                                            correct=input("enter correct option")
                                            ditopic[temp_t][temp_diff][l]=[]
                                            ditopic[temp_t][temp_diff][l].append(question)
                                            ditopic[temp_t][temp_diff][l].append(option)
                                            ditopic[temp_t][temp_diff][l].append(correct)
                                        else:
                                            print('wrong diff level')
                                    else:
                                        print("wrong topic")
                                if n=='2':   #del question

                                    temp_t=input("select topic : ")
                                    if temp_t in diuser[nsu]['1']:
                                        temp_diff=input("enter difficulty in 1,2,3 :")
                                        if temp_diff in ['1','2','3'] and ditopic[temp_t][temp_diff]:
                                            for ques in ditopic[temp_t][temp_diff]:
                                                print('--', ques)

                                                for i in ditopic[temp_t][temp_diff][ques]:
                                                    print('-', i)
                                            temp_qno=input("enter qno to del :").strip()
                                            if temp_qno in ditopic[temp_t][temp_diff] :
                                                del ditopic[temp_t][temp_diff][temp_qno]





                                        else:
                                            print("invalid input or no questions available")
                                    else:
                                        print("no topic like this")

                                if n=='3':  #update ques
                                    temp_t = input("select topic : ")
                                    if temp_t in diuser[nsu]['1']:
                                        temp_diff = input("enter difficulty in 1,2,3 :")
                                        if temp_diff in ['1', '2', '3'] and ditopic[temp_t][temp_diff]:
                                            for ques in ditopic[temp_t][temp_diff]:
                                                print('--', ques)

                                                for i in ditopic[temp_t][temp_diff][ques]:
                                                    print('-', i)
                                            temp_qno = input("enter qno to del :").strip()
                                            if temp_qno in ditopic[temp_t][temp_diff]:
                                                temp_edit=input("select question(0)/option(1)/correct(2):").strip()

                                                if temp_edit in ['0','1','2']:
                                                    td={'0':'question','1':'option','2':'correct'}
                                                    new_edit=input(f'enter for new {td[temp_edit]} :')

                                                    ditopic[temp_t][temp_diff][temp_qno][int(temp_edit)]=new_edit
                                                    print("updated successfully!!")
                                                else:
                                                    print("invalid input")
                                            else:
                                                print('wrong qno')






                                        else:
                                            print("invalid input or no questions available")
                                    else:
                                        print("no topic like this")










                        if n3=='4': #del topic

                            temp_t = input("input topic name :").strip()
                            if temp_t in diuser[nsu]['1']:
                                del ditopic[temp_t]
                                diuser[nsu]['1'].remove(temp_t)
                                print(diuser, ditopic)
                            else:
                                print("no topic like this.")



                        if n3=='5': #to save all your changes
                            temp_o=input("enter y/Y to confirm :")
                            if temp_o in ['y','Y']:
                                fh.upd_user(diuser)
                                fh.upd_topics(ditopic)

                            else:
                                print("wrong input")

                if n2=='2':
                    if diuser[nsu]['2']:
                        for i in diuser[nsu]['2']:
                            print(i)
                    else:
                        print("no quizes yet")
                    while True:
                        topics.man_quizes()
                        n3 = inp.selop()
                        if n3 == '0':  # Axit
                            break

                        if n3=='1':  #create quiz list
                            temp_topic = inp.cre_quiz()
                            if temp_topic not in diuser[nsu]['2'] and temp_topic:
                                diuser[nsu]['2'].append(temp_topic)
                                diquiz[temp_topic] = {}
                                print('quiz list added !!')
                            else:
                                print("quiz list already exit or no input")

                        if n3=='2':  #reading the quiz list
                            if diuser[nsu]['2']:
                                for i in diuser[nsu]['2']:
                                    print(i)

                                temp_t = input("select name of quiz list: ").strip()

                                if temp_t in diuser[nsu]['2']:

                                    if diquiz[temp_t]:
                                        print("total quizes in this lsit :")
                                        for i in diquiz[temp_t]:

                                            print(i)




                                    temp_diff = input("enter quiz name in quiz list:").strip()
                                    if temp_diff in diquiz[temp_t] and diquiz[temp_t][temp_diff]:
                                        for ques in diquiz[temp_t][temp_diff]:
                                            print('--', ques)

                                            for i in diquiz[temp_t][temp_diff][ques]:
                                                print('-', i)
                                    else:
                                        print("invalid input or no quiz available")
                                else:
                                    print("no quizes like this")
                            else:
                                print("no quizes yet")


                        if n3=='3':  #update

                            while True:
                                topics.updateq_m()
                                n=inp.selop()
                                if n=='0':
                                    break

                                if n=='1':  # add quiz to quiz list
                                    temp_topic=input('enter quiz list in which u want to add quiz :').strip()


                                    if temp_topic in diuser[nsu]['2'] :
                                        temp_no = inp.cre_quizno()

                                        diquiz[temp_topic][temp_no]={}
                                        print('new quiz added to list!!')
                                    else:
                                        print("quiz list not present")


                                if n=='2':  #add question to quiz
                                    temp_q=input("select quiz list name").strip()




                                    if  temp_q in diuser[nsu]['2']:
                                        temp_dif=input('enter quiz name in list').strip()
                                        if temp_dif in diquiz[temp_q]:
                                            l=len(diquiz[temp_q][temp_dif])
                                            l=str(l)


                                            if diuser[nsu]['1']:
                                                print("list of topics :")
                                                for i in diuser[nsu]['1']:
                                                    print(i)
                                            else:
                                                print("no topics yet")
                                            temp_t = input("select topic : ").strip()
                                            if temp_t in diuser[nsu]['1']:
                                                temp_diff = input("enter difficulty in 1,2,3 :")
                                                if temp_diff in ['1', '2', '3'] and ditopic[temp_t][temp_diff]:

                                                    for ques in ditopic[temp_t][temp_diff]:
                                                        print('--', ques)
                                                        question=ques

                                                        for i in ditopic[temp_t][temp_diff][ques]:
                                                            print('-', i)
                                                    temp_tra=input("enter ques no to add in quiz").strip()
                                                    if temp_tra in ditopic[temp_t][temp_diff]:
                                                        question=ditopic[temp_t][temp_diff][temp_tra][0]
                                                        option=ditopic[temp_t][temp_diff][temp_tra][1]
                                                        correct=ditopic[temp_t][temp_diff][temp_tra][2]
                                                        diquiz[temp_q][temp_dif][l] = [question, option, correct]

                                                else:
                                                    print("invalid input or no questions available")
                                            else:
                                                print("no topic like this")



                                        else:
                                            print('wrong quiz name')
                                    else:
                                        print("wrong list name")
                                if n=='3': #del question
                                    if diuser[nsu]['2']:
                                        for i in diuser[nsu]['2']:
                                            print(i)
                                    else:
                                        print("no quizes yet")
                                    temp_t = input("select name of quiz list: ").strip()
                                    if temp_t in diuser[nsu]['2']:
                                        temp_diff = input("enter quiz name in quiz list:").strip()
                                        if temp_diff in diquiz[temp_t] and diquiz[temp_t][temp_diff]:
                                            for ques in diquiz[temp_t][temp_diff]:
                                                print('--', ques)

                                                for i in diquiz[temp_t][temp_diff][ques]:
                                                    print('-', i)



                                            temp_l = input("enter q no to del :")
                                            if temp_l in diquiz[temp_t][temp_diff]:

                                                del diquiz[temp_q][temp_diff][temp_l]
                                            else:
                                                print("wrong q no")
                                        else:
                                            print("invalid input or no question available")
                                    else:
                                        print("no quizes like this")

                        if n3 == '4':

                            while True:
                                topics.delq_m()
                                n = inp.selop()
                                if n == '0':
                                    break
                                if n == '1':  #del q
                                    temp_q = input("select quiz list name").strip()

                                    if temp_q in diuser[nsu]['2']:
                                        temp_dif = input('enter quiz name in list').strip()
                                        if temp_dif in diquiz[temp_q]:
                                            del diquiz[temp_q][temp_dif]
                                        else:

                                            print('wrong quiz name')
                                    else:
                                        print('wrong quiz list')

                                if n == '2':  #del list
                                    temp_q = input("select quiz list name").strip()

                                    if temp_q in diuser[nsu]['2']:


                                        del diquiz[temp_q]
                                        diuser[nsu]['2'].remove(temp_q)


                                    else:
                                        print('wrong quiz list')

                        if n3=='5':  #save
                            temp_o = input(" y/Y to confirm :")
                            if temp_o in ['y', 'Y']:
                                fh.upd_user(diuser)
                                fh.upd_quizes(diquiz)
                            else:
                                print("wrong input")

















        else:
            print('user not found')
            temp_name=inp.cre_user()
            if temp_name not in diuser and temp_name:
                diuser[temp_name]={'1':[],'2':[]}
                fh.upd_user(diuser)
                print("created successfully")

            else:
                print("superuser already exist or no input")

    if n1=='2':
        nsu = inp.seltaker()
        if nsu in ditaker:
           while True:
               topics.taker_m()
               n=inp.selop()
               if n=='0':
                   break
               if n=='2':
                   if diquiz:
                        for quizlist in diquiz:
                            print("quiz list :")
                            print(quizlist)



                        quizlist=input("enter quiz list :")
                        if quizlist in diquiz:
                            if diquiz[quizlist]:

                                for quiz in diquiz[quizlist]:
                                    print("quizes are")
                                    print(quiz)

                                quizlist = input("select quiz list name").strip()

                                if quizlist in diquiz:
                                    quiz = input('enter quiz name :').strip()
                                    if quiz in diquiz[quizlist]:
                                        anslist=[]
                                        marks=0
                                        totalmarks=0
                                        for i in diquiz[quizlist][quiz]:
                                            for j in diquiz[quizlist][quiz][i][0:2]:
                                                print(j)
                                            ans=input("enter your ans :")
                                            anslist.append(ans)

                                        for i,c in enumerate(diquiz[quizlist][quiz]):
                                            if diquiz[quizlist][quiz][str(i)][2] ==anslist[i]:
                                                marks+=10
                                            totalmarks+=10
                                        ditaker[nsu][f'marks obt in {quiz} quiz :']=marks
                                        ditaker[nsu]['percenage are' ]=(marks/totalmarks)*100
                                        print(f"total makrs  obtained :{marks} out of {totalmarks}")







                                    else:

                                        print('wrong quiz name')
                                else:
                                    print('wrong quiz list')







                        else:
                            print("no quizes in this list")

                   else:
                       print("no quiz list yet")

               if n=='1':
                    if ditaker[nsu]:
                        print('name :',nsu)
                        for c,i in enumerate(ditaker[nsu]):
                            print(i,ditaker[nsu][i])

                    else:
                        print('no data')

               if n=='3':
                   temp_o = input(" y/Y to confirm :")
                   if temp_o in ['y', 'Y']:
                       fh.upd_taker(ditaker)

                   else:
                       print("wrong input")




        else:
            print('testtaker not found')
            temp_name = inp.cre_taker()
            if temp_name not in ditaker and temp_name:
                ditaker[temp_name] = {}
                fh.upd_taker(ditaker)
                print("created successfully")

            else:
                print("testtaker already exist or no input")

