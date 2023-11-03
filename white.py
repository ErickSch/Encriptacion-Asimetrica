mip = input("ingresa: ")

mip = mip.replace('[', '')
mip = mip.replace(']', '')
mip = mip.split(', ')
mip = (int(num) for num in mip)
mip = list(mip)

print(mip)
print(type(mip[0]))

# [290, 545, 424, 564, 895, 281]
