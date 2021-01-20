# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint
import numpy as np
import math

def print_hi(name): # do czego ta funkcja?
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_game_map(gun1,gun2,width,height,path):
    for j in range(width):
        for i in range(height):
            t=(i,j)
            if gun1==t:
                print("X",end='')
            elif gun2==t:
                print("X",end='')
            elif t in path:
                print("* ",end='')
            else:
                print("  ",end='')
        print("\n",end='')


def find_parabole_equation(p1, p2, vertex): # nieczytelne nazwy
    A = np.array([[p1[0] ** 2, p1[0], 1], [p2[0] ** 2, p2[0], 1], [vertex[0] ** 2, vertex[0], 1]])
    b = np.array([p1[1], p2[1], vertex[1]])

    return np.linalg.solve(A, b)


def generate_path(width,height,y):
    g1=int(0.10*width)
    g2=int(0.90*width)

    g=[]
    current_y=y
    path=[]
    for j in range(width):
        move_y=randint(-1, 1)
        if current_y>0 and current_y<height:
            current_y+=move_y
        if g1==j:
            g.append((g1,current_y))
        elif g2==j:
            g.append((g2,current_y))

        path.append((j,current_y))
    return path,g

def calculate_parabole_value(parameters,x):
	return parameters[0]*x**2+parameters[1]*x+parameters[2]


def create_parabole(p1, p2, vertex, step=1) -> object:
    parameters = find_parabole_equation(p1, p2, vertex)

    start_point_x = p1[0]
    parabole_points = []

    for i in range(abs(p1[0] - p2[0])):
        parabole_points.append((start_point_x + i, int(calculate_parabole_value(parameters, start_point_x + i))))

    return parabole_points

def create_crater_in_path(current_path,crater):
    crater_path=[]
    for cp in current_path:
        crater_added = False
        for c in crater:
            if c[0]==cp[0]:
                crater_path.append(c)
                crater_added=True
                break
        if crater_added==False:
            crater_path.append(cp)

    return crater_path

def get_dist(p1,p2):
    return  math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def get_dist_point_path(path,point):
    min_dist=get_dist(path[0],point)
    min_dist_point=path[0]
    for p in path:
        current_dist=get_dist(p,point)
        if min_dist>current_dist:
            min_dist=current_dist
            min_dist_point=p

    return current_dist,min_dist_point

def get_dist_x(p1,p2):
    return abs(p1[0]-p2[0])

def shot_bullet(gun,direction,angle,init_velocity,width,path):
    g=1
    distances=[]
    north=True
    last_y=0
    y=0
    if direction.upper()=='RIGHT':
        start_pos=gun[0]

        for x in range(0,width):
            last_y=y
            y=int(x*math.tan(angle)-(g*x**2)/(2*(init_velocity**2)*(math.cos(angle))**2))

            if last_y>y:
                north=False
            if north==False:    # if not north
                temp_x=gun[0]+x
                temp_y=gun[1]-y
                distances.append(get_dist_point_path(path,(temp_x,temp_y)))

    if direction.upper()=='LEFT':
        start_pos=gun[0]    # DRY

        for x in range(0,start_pos):
            last_y=y
            y=int(x*math.tan(angle)-(g*x**2)/(2*(init_velocity**2)*(math.cos(angle))**2))   # ZeroDivisionError

            if last_y>y:
                north=False
            if north==False:
                temp_x=gun[0]-x
                temp_y=gun[1]+y
                distances.append(get_dist_point_path(path,(temp_x,temp_y)))

    return distances

def get_minimum_distance(distances):
    min_dist=distances[0][0]
    min_point=distances[0][1]
    for d in distances:
        if d[0]<min_dist:
            min_dist=d[0]
            min_point=d[1]
    return min_dist,min_point

if __name__ == '__main__':  # lepiej zawartość tego if'a przenieść do funkcji main
    h=30    # sugeruję pełnym słowem
    w=30
    path,g=generate_path(w,h,h/2)

    print_game_map(g[0],g[1],w,h,path)
    print("Enter bullet power (only int): ")
    depth=int(input())
    current_gun="GUN1"
    running_game=True
    while running_game:
        print(current_gun)
        if current_gun=="GUN1":
            print("Velocity: ")
            v=float(input())
            print("Angle (radians)")
            a=float(input())

            distances=shot_bullet(g[0],'RIGHT',a,v,w,path)
            if distances==[]:
                print("Bullet out of map")
                current_gun="GUN2"
            else:
                hit_point=get_minimum_distance(distances)[1]
                if get_dist_x(hit_point,g[1])>4:
                    ppoints=create_parabole(path[hit_point[0]-4],path[hit_point[0]+4],(hit_point[0],hit_point[1]+depth))

                    path=create_crater_in_path(path,ppoints)
                    print_game_map(g[0], g[1], w, h, path)
                    current_gun="GUN2"
                else:
                    print("GUN1 has won!!!")
                    running_game=False
        else:
            print("Velocity: ") # DRY
            v = float(input())
            print("Angle (radians)")
            a = float(input())

            distances = shot_bullet(g[0], 'LEFT', a, v, w, path)
            if distances==[]:
                print("Bullet out of map")
                current_gun="GUN1"
            else:
                hit_point = get_minimum_distance(distances)[1]

                if get_dist_x(hit_point,g[0])>4:
                    ppoints = create_parabole(path[hit_point[0] - 4], path[hit_point[0] + 4],
                                              (hit_point[0], hit_point[1] + depth))

                    path = create_crater_in_path(path, ppoints)
                    print_game_map(g[0], g[1], w, h, path)
                else:
                    print("GUN2 has won!!!")
                    running_game=False