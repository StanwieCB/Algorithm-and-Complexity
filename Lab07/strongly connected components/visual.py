import Tkinter
import tkFont
import math

color = \
[
'#F0F8FF',
'#FAEBD7',
'#00FFFF',
'#7FFFD4',
'#F0FFFF',
'#F5F5DC',
'#FFE4C4',
'#FFEBCD',
'#0000FF',
'#8A2BE2',
'#A52A2A',
'#DEB887',
'#5F9EA0',
'#7FFF00',
'#D2691E',
]

def draw_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)


def main():
    center_x = 700
    center_y = 400
    rr = 350
    r = 20
    v_num = 0

    '''get the adjacent matrix'''
    f = open('input.txt')
    while 1:
        char = f.read(1)
        if not char:
            break
        if char == '\n':
            v_num += 1
    f.close()

    edgeM = [[] for i in range(v_num)]
    l = 0
    f = open('input.txt')
    while 1:
        char = f.read(1)
        if not char:
            break
        if char == '\n':
            l += 1
        elif char == '1':
            edgeM[l].append(1)
        elif char == '0':
            edgeM[l].append(0)
    f.close()
    '''debug code'''
    '''print edgeM'''

    '''get the SCC'''
    c_num = 0
    f = open('output.txt')
    while 1:
        char = f.read(1)
        if not char:
            break
        if char == '\n':
            c_num += 1
    f.close()

    c_num /= 2
    sccM = [[] for i in range(c_num)]
    l = 0
    f = open('output.txt')
    while 1:
        char = f.read(1)
        if not char:
            break
        if char == '\n':
            l += 1
        elif char.isalpha() and (l % 2):
            sccM[l/2].append(char)
    f.close()
    '''debug code'''
    '''print sccM'''
    '''count coordinate of vertices'''
    v_list = [[], []]
    for i in range(v_num):
        v_list[0].append(center_x + rr * math.cos(float(i)/v_num*2*math.pi-0.5*math.pi))
        v_list[1].append(center_y + rr * math.sin(float(i)/v_num*2*math.pi-0.5*math.pi))

    root = Tkinter.Tk()
    cv = Tkinter.Canvas(root, width=1200, height=800, bg='white')

    '''debug code'''
    '''print v_list'''
    '''draw circles'''
    c_list = []

    for i in range(v_num):
        c_list.append(draw_circle(cv, v_list[0][i], v_list[1][i], r))
        cv.create_text(v_list[0][i], v_list[1][i], text=chr(i+65), fill="black")

    '''draw edges'''
    for i in range(v_num):
        for j in range(v_num):
            if edgeM[i][j] == 1:
                del_x = v_list[0][j]-v_list[0][i]
                del_y = v_list[1][j]-v_list[1][i]
                l3 = math.sqrt(math.pow(del_x, 2)+math.pow(del_y, 2))
                cv.create_line((v_list[0][i]+(r*del_x/l3), v_list[1][i]+(r*del_y/l3)),
                              (v_list[0][j]-(r*del_x/l3), v_list[1][j]-(r*del_y/l3)),
                              width=2, arrow="last", arrowshape=(10, 19, 5))

    '''draw SCC'''
    for i in range(v_num):
        for j in range(c_num):
            flag = 0
            for k in range(len(sccM[j])):
                if sccM[j][k] == chr(i+65):
                    cv.itemconfig(c_list[i], fill=color[j])
                    flag = 1
                    break
            if flag == 1:
                break

    '''draw notes'''
    step1 = (700-100)/(c_num-1)
    for j in range(c_num):
        draw_circle(cv, 100, 100+j*step1, r, fill=color[j])
        cv.create_text(100+4*r, 100+j*step1, text="SCC"+str(j+1),
                       font=tkFont.Font(family="Helvetica", size=14))

    cv.pack()
    root.mainloop()

main()
