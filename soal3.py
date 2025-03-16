nilai = float(input("Masukan nilai siswa: "))
grade = "E"
if nilai >=80:
    grade = "A"
elif nilai >=70:
    grade = "B"
elif nilai >=60:
    grade = "C"
elif nilai >=50:
    grade = "D"
print ("Grade: ",grade)