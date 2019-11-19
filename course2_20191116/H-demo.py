import math

count = 20

red  = 2
white = 8
green = 3
black = 1
gary = 6

arr_list = []
def i_fun(count, num):
    arr_list.append(-math.log2(num/count))
    print(arr_list)
    return -math.log2(num/count)

def h_fun(p):
    print(- p * math.log2(p))
    return - p * math.log2(p)

i_red = i_fun(count,red)
# print(i_red)
i_white = i_fun(count,white)
# print(i_white)
i_green = i_fun(count,green)
# print(i_green)
i_black = i_fun(count,black)
# print(i_black)
i_gray = i_fun(count,gary)
# print(i_gray)

h_x = 0
print(arr_list)

for n in range(len(arr_list)):
   h_x -= h_fun(arr_list[n])

print(h_x)






