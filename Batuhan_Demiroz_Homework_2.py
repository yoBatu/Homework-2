import math
n = int(input("How many points: "))

if n <= 0:
    print("Error, input more than 1")

coor = []

for i in range(n):
    print("Enter point "+ str(i+1))
    x = float(input("x: "))
    y = float(input("y: "))
    coor.append(tuple([x,y]))

x_centerofmass = 0
y_centerofmass = 0

def centerofmass(mylist, x_centerofmass, y_centerofmass):

    for i in range(len(mylist)):
        x_centerofmass += mylist[i][0]  
        y_centerofmass += mylist[i][1]

    x_centerofmass /= len(mylist)
    y_centerofmass /= len(mylist)

    return [x_centerofmass, y_centerofmass]

my_result = centerofmass(coor, x_centerofmass, y_centerofmass)

print("Center of mass of x values is: ", my_result[0])
 
print("Center of mass of y values is:", my_result[1])

d_list = []

def euc(my_result, coor):
    closest = 0 
    farthest = 0
    coor_f = []
    coor_c = []

    x_square = math.pow(abs(my_result[0] - coor[0][0]), 2)
    y_square = math.pow(abs(my_result[1] - coor[0][1]), 2)
    closest = math.sqrt(x_square + y_square)

    for i in range(len(coor)):
        x_square = math.pow(abs(my_result[0] - coor[i][0]), 2)
        y_square = math.pow(abs(my_result[1] - coor[i][1]), 2)

        if farthest < math.sqrt(x_square + y_square):
            farthest = math.sqrt(x_square + y_square)
            coor_f = coor[i]
        
        if closest > math.sqrt(x_square + y_square):
            closest = math.sqrt(x_square + y_square)
            coor_c = coor[i]
            
        d_list.append(math.sqrt(x_square + y_square))

    print("List of distances from points to the center of mass:", d_list)
    print("Farthest point from the center of mass is ", coor_f)
    print("Closest point from the center of mass is", coor_c)

euc(my_result, coor)