

numbers = "77002846291"
num_list = []
odd_num_list = []
sum:int = 0

for i in numbers:
    if i.isdigit():
        sum = sum + int(i)

for k in numbers:
    if k.isdigit():
        num_list.append(k)
    if ((int(k)%2) != 0):
        odd_num_list.append(k)

def p():
    print(f'Sondagi toq sonlar quyidagilar{odd_num_list}')
    print(f'Bu sonning raqamlar yig\'indisi: {sum} ga teng')
    print(f"Bu sondagi eng katta raqam {max(num_list)} ga teng")
    print(f"Bu sondagi eng kichik raqam {min(num_list)} ga teng")
def main():
    p()

if __name__=='__main__':
    exit(main())