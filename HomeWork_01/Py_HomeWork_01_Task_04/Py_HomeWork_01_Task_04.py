# ������ 4
# �������� ��������� ���������� ����� ������������ ����� �� 1 �� N.
# ������: ����� N = 4, ����� [ 1, 2, 6, 24 ]

def rowMultiply(number):
    row = []
    i = 1
    temp = 1
    for i in range(1,number+1):
        temp *= i
        row.append(temp)
    print(row)

rowMultiply(4)