# ���� ����� ����� A � B (A < B). ������� ��� ����� ����� �� A �� B ������������; ��� ���� ����� A
# ������ ���������� 1 ���, ����� A + 1 ������ ���������� 2 ���� � �. �.  
try:
    A = int(input("������� �����: "))
    B = int(input("������� �����, ������ �����������: "))
    for i in range(A, B + 1): # ������ �����
        if i == A + 1:
            print(i)
            print(i)
        else:
            print(i)
except ValueError:
    print('�� ����� ������������ ��������')