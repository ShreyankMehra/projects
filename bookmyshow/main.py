from cinema import *
import options


temp_c=cinema()
temp_c.create()
temp_c.validseatsupdate()
temp_c.chars()


while True:
    options.display()

    inp=input('\nSelect option to proceed :')

    if inp.strip()=='0':
        print("\nThankyou!!")
        break


    if inp.strip()=='1':
        temp_c.show_the_seats()

    if inp.strip()=='2':
        temp_c.book_your_ticket()
        print("\nBooked Successfully")

    if inp.strip()=='3':
        print('\n',temp_c.get_bookedtick(),sep="")
        print(temp_c.get_percentage(),)

        print(temp_c.get_currentincome())
        print(temp_c.get_totalincome())

    if inp.strip()=='4':
        temp_c.get_ticketinfo()


    if inp.strip() not in['0','1','2','3','4']:
        print("WRONG INPUT, try again!")










