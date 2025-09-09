
def bai_1():
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    c = int(input("Nhập số thứ ba: "))
    print("Số lớn nhất là:", max(a, b, c))
def bai_2():
    lst = list(map(int, input("Nhập các số cách nhau bởi khoảng trắng: ").split()))
    print("Tổng các số trong list:", sum(lst))
def bai_3():
    s = input("Nhập chuỗi: ")
    print("Chuỗi đảo ngược:", s[::-1])
def bai_4():
    n = int(input("Nhập số n: "))
    if n < 0:
        print("Không tồn tại giai thừa cho số âm")
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        print(f"{n}! = {fact}")
def bai_5():
    n = int(input("Nhập số cần kiểm tra: "))
    if n < 2:
        print(n, "không phải số nguyên tố")
        return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(n, "không phải số nguyên tố")
            return
    print(n, "là số nguyên tố")
def bai_6():
    choice = int(input("Chọn 1 hoặc 2:\n1. In các số nguyên tố nhỏ hơn n\n2. In N số nguyên tố đầu tiên\nLựa chọn: "))

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

    if choice == 1:
        n = int(input("Nhập n: "))
        primes = [i for i in range(2, n) if is_prime(i)]
        print(f"Các số nguyên tố nhỏ hơn {n}:", primes)

    elif choice == 2:
        N = int(input("Nhập N: "))
        primes = []
        num = 2
        while len(primes) < N:
            if is_prime(num):
                primes.append(num)
            num += 1
        print(f"{N} số nguyên tố đầu tiên:", primes)
def bai_7():
    def is_perfect(n):
        d = [i for i in range(1, n) if n % i == 0]
        return sum(d) == n

    n = int(input("Nhập số cần kiểm tra: "))
    if is_perfect(n):
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải số hoàn hảo")

    print("Các số hoàn hảo nhỏ hơn 1000 là:")
    for i in range(1, 1000):
        if is_perfect(i):
            print(i, end=" ")
    print()
def bai_8():
    import string
    s = input("Nhập chuỗi: ").lower()
    alphabet = set(string.ascii_lowercase)
    if alphabet.issubset(set(s)):
        print("Chuỗi là Pangram")
    else:
        print("Chuỗi không phải Pangram")
def main():
    while True:
        print("\n===== MENU =====")
        for i in range(1, 9): print(f"{i}. Bài {i}")
        print("0. Thoát")
        chon=input("Chọn bài: ").strip()
        if chon=="0":break
        try: print(globals()[f"bai_{chon}"]())
        except: print("Lỗi hoặc lựa chọn không hợp lệ.")

if __name__=="__main__": main()
