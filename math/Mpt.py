import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


St = ['\n\nwlecome','........','to','..........','python MULTIPLIER\n']
for x in St:
    print (x)


def rount():
    Anum = int(input("\nwhat is the multiple number\t"))
    Anum_1 = Anum -1
    num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    global mnum
    mnum = num[Anum_1]
    print("\npractice multiples of " + str(mnum), " \n" )
    input("Press Enter to start\t")
    start_time = time.time()
    C_a = []
    W_a = []
    M_pul = 0
    while M_pul < len(num) + 1:
        inp = int(input(str(mnum) + ' x ' + str(M_pul) +' = '))
        if inp != mnum * M_pul:
            print("answer wrong\n")
            W_a.append('')
        else:
            print("excelent\n")
            C_a.append('')
        M_pul = M_pul + 1
    
    input("Press Enter to stop\t")
    end_time = time.time()

    print('\nanswers correcr =',len(C_a))
    print('answers wrong =', len(W_a),'\n') 

    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

    global rep
    rep = (input("\ndo you want to repeat for another test\n'N'-for no 'Y'-for yes\t")).upper()

rount()   

if rep == 'Y':
    rount()
else:
    exit()


