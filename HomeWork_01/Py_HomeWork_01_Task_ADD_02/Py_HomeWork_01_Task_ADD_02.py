# ���.������ 2
# 2. ���� ����� ���� - ���������. ��� ����� ����� �������� � ����� ������ ���������. 
# ��������, ����� "�����". ����� ���� �������� ���������. 
# ���� ��� �������� ������ ����� (124 - 421) �� ���������� �� �� �����, �� ��� ������������ (124+421) � ����������� �����. 
# ���������� �������� �������, ��������� �������� ���������.

import random

def search_palindrom():
    start_number = random.randint(10, 99999) 
    polindrom = 0
    
    while start_number != polindrom:
        start_number += polindrom
        temp = start_number
        polindrom = 0
        while temp != 0:
            polindrom = polindrom*10 + temp%10
            temp //=10

    print(f"polindrom = {polindrom}")


search_palindrom()