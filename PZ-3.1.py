N = int(input('������� ����� ��������������� �����: '))
if (N // 1000 == N % 10) and (N // 100 % 10 == N // 10 % 10): # ��������
    print("True")
else:
    print("False")