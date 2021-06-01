#D = True 
D = False

import random
import turtle

polygon_type_dic  = { 0: ">> 삼각형이 아닙니다.",
                                 1: ">> 직각 삼각형입니다.",
                                 2: ">> 둔각 삼각형입니다.",
                                 3: ">> 예각 삼각형입니다." ,
                                 4: ">> 사각형이 아닙니다.",
                                 5: ">> 정사각형 또는 직사각형입니다.",
                                 6: ">> 정사각형 또는 직사각형이 아닙니다." }

def input_n():

    range_ok = True
    print("\n>> 다각형을 생성하고자 한다")

    num_of_n = int(input(">> 각의 수 n 을 입력하시오. (3 <= n <= 10) :  "))
    print("    입력하신 값은 ", num_of_n, "입니다. ")
    
    while range_ok == True:

        if 3 <= num_of_n <= 10:
            range_ok == False
            return num_of_n

        else:
            print("\n>> 입력한 값 {}이(가)  3 <= n <= 10 범위를 벗어납니다. 다시 입력해 주세요 :"
                      .format(num_of_n))
            
            num_of_n = int(input("     n = "))            
            continue


def sum_of_internal_angle_of_npolygon(in_n):

    sum_of_internal_angle = 180 * (in_n - 2) 
    print("\n>> {}각형의  내각의 합은 {}도 입니다.".format(in_n, sum_of_internal_angle))

    return sum_of_internal_angle


def generate_internalAngles_list(in_n, sum_of_ang):

    if D:
        print("\ng1) in_n =", in_n)
        print("g2) sum_of_ang =", sum_of_ang)

    gen_OK = True
    gen_angles_list =[]
    
    while gen_OK == True:
        
        for i in range(0, in_n):
            angle = random.randint(1, 360)
            gen_angles_list.append(angle)

        if sum(gen_angles_list) == sum_of_ang:
            gen_OK = False
            gen_angles_list.sort()
            
            tuple_gen_angles_list = tuple(gen_angles_list)

            print("\n>> Random으로 생성된 {}각형의 내각값(tuple) : {}"
                  .format(in_n, tuple_gen_angles_list))
                
            return tuple_gen_angles_list
        
        else:
            gen_angles_list =[]


def check_triangle_type(int_angles):
    if D:
        print("ct1) int_angles :", int_angles)

    print("\n>> 입력된 삼각형의 타입을 출력합니다.")

    angle_sum = sum(int_angles)

    if angle_sum != 180 or len(int_angles) != 3 or min(int_angles) <= 0:
        type_of_triangle = 0

        if D:
            print("ct2) 삼각형이 아닙니다.:", type_of_triangle)

    if 90 in int_angles:
        type_of_triangle = 1

        if D:
            print("ct3) 직각 삼각형 입니다. type :",  type_of_triangle)
   
    elif max(int_angles) > 90:
        type_of_triangle = 2

        if D:
            print("ct4) 둔각 삼각형 입니다. type :", type_of_triangle)
    
    elif min(int_angles) < 90:
        type_of_triangle = 3

        if D:
            print("ct5) 예각 삼각형 입니다. type :",  type_of_triangle)

    print(polygon_type_dic[type_of_triangle])


def check_quadrangle_type(int_angles):
    if D:
        print("cq1) int_angles :", int_angles)

    print("\n>> 입력된 사각형의 타입을 출력합니다.")

#    int_angles = (90, 90, 90, 90) 
    angle_sum = sum(int_angles)
    
    if D:
        print("cq2) angle_sum :", angle_sum)
        
    if angle_sum != 360 or len(int_angles) !=4 or min(int_angles) <= 0:
        type_of_quadrangle = 4

        if D:
            print("cq3) 사각형이 아닙니다.:", type_of_quadrangle)

    else:
        quad_flag = True
        
        for i in int_angles:
            if i != 90:
                quad_flag = False

        if quad_flag == True:
            type_of_quadrangle = 5 # 정(직)사각형
            if D:
                print("cq4) 정(직)사각형 입니다. type :", type_of_quadrangle)
                
        else :
            type_of_quadrangle = 6 # 정(직)사각형 아님
            if D:
                print("cq5) 정(직)사각형이 아닙니다. type :", type_of_quadrangle)

    print(polygon_type_dic[type_of_quadrangle])


def draw_polygon(in_n):

    print("\n>> 정{}각형을 그립니다.".format(in_n))
    
    s = turtle.Screen()
    t = turtle.Turtle()

    for i in range(in_n):      # n번 반복
        t.forward(100)
        t.right(360 / in_n)

      
def main():
    n = input_n()               # 값을 받아들이는 함수
    if D:
        print("1) n =", n)

    returned_sum_of_internal_angle = sum_of_internal_angle_of_npolygon(n)
    if D:
        print("\n2) sum_of_angles =", returned_sum_of_internal_angle)

    returned_angle_list = generate_internalAngles_list(n, returned_sum_of_internal_angle)
    if D:
        print("\n3) returned_angle_list =", returned_angle_list)

    if n == 3: #삼각형의 경우 삼각형의 타입을 출력
        check_triangle_type(returned_angle_list)

    if n == 4: #사각형의 경우 정사각형 / 직사각형 타입을 출력. 즉 4개의 각이 모두 같은 지 확인 
        check_quadrangle_type(returned_angle_list)

    draw_polygon(n)
    
#main
main()
