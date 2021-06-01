D=True

def in_values():
    if D:
        begin_val=int(input("시작값을 입력하세요"))
        end_val=int(input("종료값을 입력하세요"))

    if D:
        print("begin_val={}, end_val={}" .format(begin_val,end_val))

    retrun begin_val, end_val

def get_sum(start,end):
    if D:
        sum=0
        for num in range(start, end+1):
            sum+=num
    if D:
        print(sum)
    return sum

if D:
    print("main starts")
    
in_v, out_v=in_values()
