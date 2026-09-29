def converts_temperatur (value, unit) :
    if unit == 'c':
        return (value * 9/5) + 32
    elif unit == 'f':
        return (value -32) * 5/9
    else :
        print("tidak ada unit yang sesuai")
value = int(input("masukan nilai suhu :"))
unit = input ("masukan unit suhu (F/C)")
result = converts_temperatur(value,unit)
print(f"hasil konversi: {result}")
