import a

print("top-level in B.py")
print("a.py에 있는 a.func() 호출")
a.func()

if __name__ == "__main__":
    print("3)b.py가 직접 실행")

else:
    print("4)b.py가 import되어 사용됨")