


class cinema:
    temp_seating={}
    validseatno = []
    charl=[]
    bookedtickets=0
    bookedtickno=[]
    percent=0


    def get_bookedtick(self):
        return f'Total booked tickets are {cinema.bookedtickets}'





    @staticmethod
    def chars():

        cinema.charl = [" ",]
        for i in range(65, 91):
            cinema.charl.append(chr(i))
        for i in range(97, 123):
            cinema.charl.append(chr(i))


    @staticmethod
    def get_percentage():
        t=len(cinema.validseatno)
        cinema.percent=((cinema.bookedtickets/t)*100)
        return 'Percentage Booked is {0:.2f} %'.format(cinema.percent)


    def get_totalincome(self):
        if len(cinema.validseatno)<=60:
            r=self.rows*self.seats*10
            return f'Total Income is {r}$'
        else:

            r=((self.rows//2)*10*self.seats)+(((self.rows//2)+1)*8*self.seats)
            return f'Total Income is {r}$'

    def get_currentincome(self):
        r=0
        if len(cinema.validseatno) <= 60:
            r=len(cinema.bookedtickno)*10
            return f'Current Income is {r}$'
        else:
            for i in cinema.bookedtickno:
                if i <=int(str(self.rows//2)+str(self.seats)):
                    r+=10
                else:
                    r+=8
            return f'Current Income is {r}$'






    def create(self):
         while True:
            try:

                rows=int(input('\nenter no of rows : '))
                self.rows=rows
            except:
                print('please provide integer value')
            else:
                break
         while True:
            try:
                seats=int(input("\nenter no of seats: "))
                self.seats = seats

            except:
                print("please provide integer value\n")
            else:
                break



    def show_the_seats(self):

        print("\nCurrent bookings :\n")

        for i in range(0,self.rows+1):

            for j in range(0,self.seats+1):
                ticketnos = int(str(i) + str(j))
                if  i ==0 and j ==0 :
                    print("    ",end="")



                elif i==0 and j!=0:
                    print(j,end=" ")
                    if i==0 and j==self.seats:
                        print('\n',end='')
                elif  i!=0 and i<10 and j==0:
                    print(str(i) + "   ", end="")

                elif  i>=10 and j==0:
                    print(str(i) + "  ", end="")



                elif i!=0 and j!=0 and j<10 :
                    if ticketnos not in cinema.temp_seating:
                        print("S ", end='')
                    else:
                        print("B ", end="")
                elif i!=0 and j!=0 and j>=10 :
                    if ticketnos not in cinema.temp_seating:
                        print("S  ", end='')
                    else:
                        print("B  ", end="")


            print('\n',end='')
            #if i!=self.rows:
                #print('\n',i+1, end=' ')

    def validseatsupdate (self):

        for i in range(1,self.rows+1):
            for j in range(1, self.seats +1):
                cinema.validseatno.append(int(str(i) + str(j)))


    def book_your_ticket(self):

        print("\nEnter the seat number/numbers to be booked seperated by comas :")
        while True:
            try:
                temp_l=list(map(int,input().split(',')))
            except:
                print("provide integer value")
            else:
                break




        for c,i in enumerate(temp_l):
            while True:
                if i not in cinema.validseatno:

                    while True:
                        try:
                            temp_l[c]=int(input(f"seat no {i} not present, enter another seatno instead of {i}:"))
                            i=temp_l[c]
                        except:
                            print('provide single integer value')
                        else:
                            break
                else:
                    break

        for c,i in enumerate(temp_l):
            while True:
                if temp_l.count(i)!=1:
                    while True:
                        try:
                            temp_l[c]= int(input(f'seat no {i} repeated, enter another seat no instead of {i} :'))
                            i=temp_l[c]
                        except:
                            print(" provide single integer value")
                        else:
                            break
                else:
                    break




        for c,i in enumerate(temp_l):
            while True:
                if i in cinema.temp_seating:
                    while True:
                        try:
                            temp_l[c]=int(input(f"Already booked for seat no {i}, Enter other seat no instead of {i}:"))
                            i=temp_l[c]
                        except:
                            print("provide single integer value")
                        else:
                            break
                else:
                    break

        for i in temp_l:
            cinema.bookedtickets+=1
            cinema.bookedtickno.append(i)
            print(f'\nEnter details for seat no {i}')
            cinema.temp_seating[i]={'Name':"",'Gender':"",'Phone':"",'Age':""}

            while True:
                    wrong=False
                    cinema.temp_seating[i]['Name'] =input("enter name :")
                    for j in cinema.temp_seating[i]['Name']:
                        if j not in cinema.charl:
                            wrong=True
                            print("use no special characters or nums in name!")
                            break
                    if wrong==False:
                        break


            while True:
                l=['male','female','other']

                cinema.temp_seating[i]['Gender']=input("enter gender in male/female/other :")
                if cinema.temp_seating[i]['Gender'] in l:
                    break
                else:
                    print("invalid input")
            while True:

                try:
                    cinema.temp_seating[i]['Phone']=int(input('enter phone no :'))
                except:
                    print("phone no should be integer!")
                    continue


                if len(str(cinema.temp_seating[i]['Phone']))==10:
                    break
                else:
                    print("enter 10 digit phone no")
            while True:

                try:
                    cinema.temp_seating[i]['Age']=int(input("enter age :"))
                except:
                    print("invalid input")
                else:
                    break

    def get_ticketinfo(self):
        while True:
            try:
                print("\nEnter the seat number/numbers seperated by comas :")
                inp=list(map(int, input().split(',')))
            except:
                print("invalid input")
                continue
            else:
                break
        notbooked = []
        notpresent = []
        for i in inp:

            if i in cinema.bookedtickno:
                print(f"\nInfo for seat no {i}")
                for j in cinema.temp_seating[i]:
                    print(j,":",cinema.temp_seating[i][j])
            elif i in cinema.validseatno:
                notbooked.append(str(i))

            else:
                notpresent.append(str(i))
        if notbooked:
            print(f"\nSeat not booked yet:{','.join(notbooked)}")
        if notpresent:

            print(f"Seat not available :{','.join(notpresent)}")












        
'''
a=cinema()
a.create()
a.show_the_seats()
a.validseatsupdate()
a.chars()
a.book_your_ticket()

print(a.bookedtickets,a.get_bookedtick())
print(a.get_percentage())
print(a.get_totalincome())
print(a.get_currentincome())
a.show_the_seats()
a.book_your_ticket()
a.show_the_seats()'''