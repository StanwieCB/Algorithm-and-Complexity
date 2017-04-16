# programmed twice
# 03-04-2017
# author:hank zhang(StanwieCB)

# A SIMPLE VISUALIZATION OF SORTING NETWORK WITH 2^K INPUTS
#############################################################

import Tkinter

# input test
_k = input("please enter exponential k:")

# initialize canvas
root = Tkinter.Tk()
c = Tkinter.Canvas(root, width=1200, height=500, bg='white')

_upper_limit = 20
_lower_limit = 480
_left_limit_1 = 20
_left_limit_2 = 50
_right_limit_1 = 1180
_right_limit_2 = 1150
# c.create_line(_upper1, _upper2)
# c.create_line(_lower1, _lower2)

# main counter
_num_of_wires = pow(2, _k)
_gap1 = float((_lower_limit - _upper_limit))/(_num_of_wires - 1)

_num_of_blocks = _k
_num_of_slides = (pow(2, _k) - 1) * 2 - _k
#print _num_of_slides
_gap2 = float((_right_limit_2 - _left_limit_2))/(_num_of_slides - 1)

for i in range(_num_of_wires):
    c.create_line((_left_limit_1,_upper_limit + i*_gap1),
                  (_right_limit_1,_upper_limit + i*_gap1))

# draw
t = 0
for i in range(1, _num_of_blocks+1):
    # draw merger
    merger_num = _num_of_wires/pow(2, i)
    for j in range(pow(2, i-1)):
        for k in range(merger_num):
            c.create_line((_left_limit_2+t*_gap2, _upper_limit+(pow(2, i)*k+j)*_gap1),
                          (_left_limit_2+t*_gap2, _upper_limit+(pow(2, i)*(k+1)-1-j)*_gap1))
        t += 1
    # draw half cleaner
    num = _num_of_wires/2
    if i >= 2:
        for j in range(i-1):
            t0 = t
            for k in range(num):
                if k*pow(2, i-1)/pow(2,j) > (t-t0+1)*(_num_of_wires-1):
                    # print "bigger!"
                    t += 1
                # print t
                c.create_line((_left_limit_2+t*_gap2, _upper_limit+((k*pow(2, i-1)/pow(2,j))%_num_of_wires+t-t0)*_gap1),
                             (_left_limit_2+t*_gap2, _upper_limit+((k*pow(2, i-1)/pow(2,j)+pow(2, i)/pow(2,j+2))%_num_of_wires+t-t0)*_gap1))
                # print (k*pow(2, i-1)/pow(2,j))%(_num_of_wires-1) ## problems here
                # print (k*pow(2, i-1)/pow(2,j)+pow(2, i)/pow(2,j+2))%(_num_of_wires-1)
            t += 1

print "finish!"

# display
c.pack()
root.mainloop()