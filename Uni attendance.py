import datetime

now = datetime.datetime.now()
D = now.strftime("%d-%m-%y")

x = ''' '''

h = '''
                                  CLASS ATTENDANCE
                             COURSE: BSC IN CSE, BATCH: #66
  '''
print(h)

print('Today date is:', D)
print(x)

# For TASINUR RAHMAN
t = '''
Name: Tasinur Rahman

Roll: 2024000000313

Batch: #66'''
print(t)
print(x)
p = input('Present, Absent, or Sick: ')
if 'present' in p:
    print(x)
    print('PRESENT: 1 ABSENT: 0')
elif 'sick' in p:
    print(x)
    print('PRESENT: 0 ABSENT: 1')
elif 'absent' in p:
    print(x)
    print('PRESENT: 0 ABSENT: 1')
else:
    print('Give answer on present, absent, or sick')
print(x)

# For REFAT KHONDOKAR
r = '''
Name: Refat Khondokar

Roll: 2024000000284

Batch: #66'''
print(r)
print(x)
q = input('Present, Absent, or Sick: ')
if 'present' in q:
    print(x)
    print('PRESENT: 1 ABSENT: 0')
elif 'sick' in q:
    print(x)
    print('PRESENT: 0 ABSENT: 1')
elif 'absent' in q:
    print(x)
    print('PRESENT: 0 ABSENT: 1')
else:
    print('Give answer on present, absent, or sick')

# For ABED HOSSAIN CHOWDHURY
r = '''
Name: Niloy Chowdhury

Roll: 2024000000283

Batch: #66'''
print(r)
print(x)
q = input('Present, Absent, or Sick: ')
if 'present' in q:
    print(x)
    print('PRESENT: 1 ABSENT: 0')
elif 'sick' in q:
    print(x)
    print('PRESENT: 0 ABSENT: 1')
elif 'absent' in q:
    print(x)
    print('PRESENT: 0 ABSENT: 1')
else:
    print('Give answer on present, absent, or sick')
