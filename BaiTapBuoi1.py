
print("Khoảng cách từ nhà đến trường:")
print("1. Gần (≤ 2 km)")
print("2. Xa (> 2 km)")
khoangcach = int(input("Chọn khoảng cách (1-2): "))

    
print("Thời gian còn lại trước giờ học:")
print("1. Nhiều (> 30 phút)")
print("2. Vừa (15 – 30 phút)")
print("3. Ít (< 15 phút)")
thoigian = int(input("Chọn thời gian (1-3): "))

   
if thoigian == 1:
    ansang = "Bạn còn nhiều thời gian, hãy ăn sáng đầy đủ: cơm, phở, trứng."
elif thoigian == 2:
    ansang = "Bạn có ít thời gian, nên ăn nhanh: bánh mì, sữa."
else:
    ansang ="Bạn không còn nhiều thời gian."

phuongtien = ""
    
if khoangcach == 1:
    if thoigian == 1:
        phuongtien ="Bạn ở gần trường, có thể đi bộ hoặc đi xe đạp."
    else:
        phuongtien = "Bạn nên đi xe máy để tiết kiệm thời gian"
elif khoangcach == 2 and thoigian == 3:
    phuongtien = "Bạn ở xa và sắp muộn, nên đi xe máy cho nhanh."
else:
    phuongtien = "Bạn có thể đi xe bus hoặc xe máy tùy ý."

print(" Ăn sáng:", ansang)
print(" Phương tiện:", phuongtien)




