# # # # # INT: Số nguyên
# # # # age_mother = 68
# # # # age_dad = 75
# # # # print("ba hơn mẹ:", age_dad - age_mother, "tuổi")

# # # # FLOAT: Số thực
# # # height = 1.6667
# # # print("Chiều cao của tôi là:", round(height,2), "m")
# # # print("Chuyển float sang int:", int(height))

# # # # # BOOL: True/False 
# # # # is_staff = True
# # # # if is_staff:
# # # #     print("Tôi là nhân viên Lift.")
# # # # else:
# # # #     print("Tôi không phải nhân viên Lift.")

# # # # # COMPLEX: Số phức
# # # # z = 3 + 4j
# # # # print("Số phức:", z)
# # # # print("Phần thực:", z.real)
# # # # print("Phần ảo:", z.imag)

# # # # # NONETYPE: Biến chưa có giá trị
# # # # address = None
# # # # if address is None:
# # # #     print("Chưa có địa chỉ.")
# # # # else:
# # # #     print("Địa chỉ là:", address)


# # # s = "  Chào cụ Python nhá!  "
# # # name = "Yến"

# # # print("upper():", s.upper())       

# # # #  Xoá khoảng trắng đầu & cuối
# # # print("strip():", s.strip())    

# # # #  Thay thế từ
# # # print("replace():", s.replace("Python", "Yến"))  

# # # #  Độ dài chuỗi
# # # print("len():", len(s))            

# # # #  Lấy ký tự đầu tiên
# # # print("s[0]:", s[0])         

# # # # # Kiểm tra chuỗi con
# # # # print("'Chào' in s:", "Chào" in s)  

# # # # # F-string: chèn biến vào chuỗi
# # # # print(f"f-string: Xin chào, tôi là {name}")  


# # # # Gia_đình = ["Ba", "Má", "Anh2", "Anh3", "Yến"]
# # # # # Thêm phần tử vào cuối danh sách
# # # # Gia_đình.append("Ý")
# # # # print(" Sau append:", Gia_đình)

# # # # # Xoá phần tử theo giá trị
# # # # Gia_đình.remove("Yến")
# # # # print("Gia đình còn lại:", Gia_đình)

# # # # # Xoá phần tử cuối cùng
# # # # last = Gia_đình.pop()
# # # # print(" Sau pop():", Gia_đình)
# # # # print(" Người bị xoá:", last)

# # # # #  Sort
# # # # Gia_đình.sort()
# # # # print("Sau sort():", Gia_đình)

# # # # #  Đảo ngược thứ tự
# # # # Gia_đình.reverse()
# # # # print(" Order lại:", Gia_đình)

# # # # #Lấy phần tử đầu tiên
# # # # print(" Người đầu tiên:", Gia_đình[0])

# # # # # #  Độ dài danh sách
# # # # # print(" Số phần tử:", len(Gia_đình))

# # # # # # Kiểm tra phần tử có trong danh sách
# # # # # print("'Nam' in names:", "Nam" in Gia_đình)
# # # # # print(" Check Anh2:", "Anh2" in Gia_đình)


# # # # # List_member_Automation_class = [("Yến", 25), ("Linh", 18), ("Lộc", 81)]

# # # # # # Lấy phần tử đầu tiên
# # # # # print(" Tên đầu tiên:", List_member_Automation_class[0])  

# # # # # # Độ dài của tuple
# # # # # print("Độ dài tuple:", len(List_member_Automation_class))  

# # # # # # 3. Giải nén tuple thành các biến riêng
# # # # # for name, age in List_member_Automation_class:
# # # # #  print("Name:", name)
# # # # #  print("Age:", age)      


# # # # # my_set = {1, 2, 3, 4}

# # # # # # Thêm phần tử vào set
# # # # # my_set.add(5)
# # # # # print("Set after adding 5:", my_set)

# # # # # # Xóa phần tử khỏi set
# # # # # my_set.remove(3)
# # # # # print("Set after removing 3:", my_set)

# # # # # # Xóa một phần tử không có trong set (sẽ gây lỗi)
# # # # # try:
# # # # #     my_set.remove(10)
# # # # # except KeyError:     
# # # # #     #  ->( Keyword: tên của một loại lỗi (exception) trong Python)
# # # # #     print("Not found!")


# # # # # Khởi tạo dict ban đầu
# # # person = {
# # #     "name": "Tran Thi Kim En", "age": 25,  "job": "Tester"}

# # # # 1. Truy cập giá trị bằng key: d["name"]
# # # print("Họ tên:", person["name"])  

# # # # 2. Truy cập an toàn bằng get() (key tồn tại)
# # # print("Nghề nghiệp:", person.get("job")) 

# # # # 3. Truy cập bằng get() với key không tồn tại
# # # print("Quốc tịch:", person.get("nationality", "Không xác định")) 

# # # # 4. Lấy danh sách keys
# # # print("Các key:", list(person.keys()))  

# # # # 5. Lấy danh sách values
# # # print("Các giá trị:", list(person.values()))  

# # # # 6. Lấy danh sách (key, value) bằng items()
# # # print("Thông tin chi tiết:")
# # # for k, v in person.items():
# # #     print(f"  {k} : {v}")

# # # # 7. Update dict bằng
# # # person.update({"age": 26, "nationality": "Vietnamese"})
# # # print("Sau update:", person)



# # # # BT from Teacher 
# # # name - Average: 8.17

# # students = [ {"name": "An", "scores": [8.0, 7.5, 9]},
# #              {"name": "Bình", "scores": [6, 5.5, 7.0]},
# #                {"name": "Cường", "scores": [9, 9.5, 10]} ]

# # print("Tên và điểm trung bình của từng sinh viên")
# # name_hs_0 = students[0]["name"]
# # name_hs_1 = students[1]["name"]
# # name_hs_2 = students[2]["name"]

# # avg_hs_0 = sum(students[0]["scores"]) / len(students[0]["scores"])
# # avg_hs_1 = sum(students[1]["scores"])  / len(students[1]["scores"])
# # avg_hs_2 = sum(students[2]["scores"])  / len(students[2]["scores"])

# # avg_hs_0 = round(avg_hs_0, 2)
# # avg_hs_1 = round(avg_hs_1, 2)
# # avg_hs_2 = round(avg_hs_2, 2)

# # print(name_hs_0, "- Average:", avg_hs_0)
# # print(name_hs_1, "- Average:", avg_hs_1)
# # print(name_hs_2, "- Average:", avg_hs_2)


# # # 1/ Add thêm student vào list
# # new_student = {"name": "Yến", "scores": [1.0, 2.0, 3]}
# # students.append(new_student)
# # print("\nsau khi add new hs:", students)


# # # 2/Xoá student cuối cùng ra khỏi list
# # last = students.pop()
# # print("\nlist sau khi xoá:", students)
# # print("người bị xoá:", last)

# # # 3/ Đếm số student có điểm trung bình trên 8.0
# # count = 0
# # for students in students:
# #     # avg = sum(student["scores"]) / len(student["scores"])
# #     if sum(students["scores"]) / len(students["scores"]) > 8.0:
# #         count += 1
# # print("\nSố student có điểm trung bình trên 8.0:", count)


# # # for student in students:   => xét từng student trong list 
# # # #     print(student["name"])
            
# # Exam#2
# students = [
#     {"name": "An", "scores": {"Toán": 8.0, "Lý": 7.5, "Hóa": 9}},
#     {"name": "Bình", "scores": {"Toán": 6, "Lý": 5.5, "Hóa": 7.0}},
#     {"name": "Cường", "scores": {"Toán": 9, "Lý": 9.5, "Hóa": 10}}
# ]
# # # 1.1/ In ra tên và điểm trung bình của từng sinh viên theo định dạng (Cách viết 1)
# print("In ra tên và điểm trung bình của từng sinh viên (Cách viết 1)")

# Hs_An= students[0]["name"]
# Lấy_dict_diem_hs_An= students[0]["scores"]
# tong_diem = 0 
# for diem in Lấy_dict_diem_hs_An.values():
#     tong_diem += diem
# avg_hs_An = tong_diem / len(Lấy_dict_diem_hs_An)
# print(f"{Hs_An} - Average: {round(avg_hs_An,2)}")

# Hs_Bình= students[1]["name"]
# Lấy_dict_diem_hs_Bình= students[1]["scores"]
# tong_diem = 0 
# for diem in Lấy_dict_diem_hs_Bình.values():
#     tong_diem += diem
# avg_hs_Bình = tong_diem / len(Lấy_dict_diem_hs_Bình)
# print(f"{Hs_Bình} - Average: {round(avg_hs_Bình,2)}")

# Hs_Cường= students[2]["name"]
# Lấy_dict_diem_hs_Cường= students[2]["scores"]
# tong_diem = 0 
# for diem in Lấy_dict_diem_hs_Cường.values():
#     tong_diem += diem
# avg_hs_Cường = tong_diem / len(Lấy_dict_diem_hs_Cường)
# print(f"{Hs_Cường} - Average: {round(avg_hs_Cường,2)}")

# # # 1.2/ In ra tên và điểm trung bình của từng sinh viên theo định dạng (Cách viết 2)
# print("\nIn ra tên và điểm trung bình của từng sinh viên (Cách viết 2)")
# for hs in students:
#     ten_hs = hs["name"]
#     diem_hs = hs["scores"]
#     khoi_tao_tong_diem_hs = 0
#     count_phan_tu_vong_lap_di_qua_diem_cua_tung_hs = 0
#     for diem in diem_hs.values():
#         khoi_tao_tong_diem_hs += diem
#         count_phan_tu_vong_lap_di_qua_diem_cua_tung_hs += 1
#     avg = khoi_tao_tong_diem_hs / count_phan_tu_vong_lap_di_qua_diem_cua_tung_hs
#     avg = round(avg,2)
#     print(f"{ten_hs} - Average: {avg}")

# # # 2.1/ Tìm sinh viên có điểm trung bình cao nhất (cách viết 1)
# print("\nTìm sinh viên có điểm trung bình cao nhất (cách viết 1)")
# List= [{"name": Hs_An, "diem": avg_hs_An}, {"name": Hs_Bình, "diem": avg_hs_Bình},
#         {"name": Hs_Cường, "diem": avg_hs_Cường}]
# print(List)

# high_mark = 0
# gioi_nhat = ""
# for hs in List:
#  if hs["diem"] > high_mark:
#     high_mark = hs["diem"]
#     gioi_nhat = hs["name"]
# print(f" {gioi_nhat} có điểm cao nhất: {high_mark}")

# # # 2.2/ Tìm sinh viên có điểm trung bình cao nhất (cách viết 2)
# print("\nTìm sinh viên có điểm trung bình cao nhất (cách viết 2)")
# for hs in students:
#     ten_hs = hs["name"]
#     diem_hs = hs["scores"]
#     tong_diem_hs = 0
#     count_phan_tu_vong_lap_di_qua_diem_cua_tung_hs = 0
#     high_mark = 0
#     hs_gioi_nhat = ""
#     for diem in diem_hs.values():
#         tong_diem_hs += diem
#         count_phan_tu_vong_lap_di_qua_diem_cua_tung_hs += 1
#     avg = round(tong_diem_hs / count_phan_tu_vong_lap_di_qua_diem_cua_tung_hs, 2)
#     if avg > high_mark:
#        high_mark = avg 
#        hs_gioi_nhat = ten_hs
# print(f"{hs_gioi_nhat} có điểm trung bình cao nhất: {high_mark}")
    
# # # 3. Tính điểm trung bình của từng môn
# print("\nĐiểm trung bình của từng môn")
# tan_so_mon_toan = 0
# tan_so_mon_ly = 0
# tan_so_mon_hoa = 0
# tong_diem_mon_toan= 0
# tong_diem_mon_ly= 0
# tong_diem_mon_hoa= 0
# for hs in students:
#     dict_diem_hs = hs["scores"]
#     for mon, diem in dict_diem_hs.items():
#         if mon == "Toán":
#            tan_so_mon_toan += 1
#            tong_diem_mon_toan +=diem
#         elif mon == "Lý":
#            tan_so_mon_ly += 1
#            tong_diem_mon_ly +=diem
#         elif mon == "Hóa": 
#            tan_so_mon_hoa += 1
#            tong_diem_mon_hoa +=diem
# avg_mon_toan = tong_diem_mon_toan / tan_so_mon_toan
# avg_mon_ly = tong_diem_mon_ly / tan_so_mon_ly
# avg_mon_hoa = tong_diem_mon_hoa / tan_so_mon_hoa

# print (f" điểm trung bình môn Toán là: {round(avg_mon_toan, 2)}")
# print (f" điểm trung bình môn Lý là: {round(avg_mon_ly, 2)}")
# print (f" điểm trung bình môn Hoá là: {round(avg_mon_hoa, 2)}")
        


# # tong_diem_tung_mon = {}
# # so_luong_mon = {}
# # # Gộp điểm và đếm số lượng
# # for hs in students:
# #     for mon, diem in hs["scores"].items():
# #         if mon not in tong_diem_tung_mon:
# #             tong_diem_tung_mon[mon] = 0
# #             so_luong_mon[mon] = 0
# #         tong_diem_tung_mon[mon] += diem
# #         so_luong_mon[mon] += 1
# # # Tính trung bình và in ra sau khi đã tổng hợp xong
# # for mon in tong_diem_tung_mon:
# #     avg = tong_diem_tung_mon[mon] / so_luong_mon[mon]
# #     print(f"{mon}: {round(avg, 2)}")


# # # 4. In xếp loại học lực cho từng sinh viên\
# print("\n Tạo List")
# List= [{"name": Hs_An, "diem": avg_hs_An}, {"name": Hs_Bình, "diem": avg_hs_Bình},
#         {"name": Hs_Cường, "diem": avg_hs_Cường}]
# print(List)

#     # Xếp loại theo thang điểm
# print("\n Xếp loại theo thang điểm")

# for hs in List:
#        name = hs["name"]
#        diem = hs["diem"]
#        if diem >= 9:
#            loai = "Xuất sắc"
#        elif diem >= 8:
#            loai = "Giỏi"
#        elif diem >= 6.5:
#            loai = "Khá"
#        elif diem >= 5:
#            loai = "Trung bình"
#        else:
#            loai = "Yếu"
#        print(f"{name} - Điểm TB: {round(diem, 2)} - Xếp loại: {loai}")


#  Giải phương trình bậc nhất ax + b = 0

# a = float(input("Nhập hệ số a: "))
# b = float(input("Nhập hệ số b: "))

# if a == 0:
#     if b == 0:
#         print("Phương trình có vô số nghiệm.")
#     else:
#         print("Phương trình vô nghiệm.")
# else:
#     x = -b / a
#     print(f"Nghiệm của phương trình là x = {x}") 

# for i in range(1, 101):  # Duyệt từ 1 đến 100
#     if i % 3 == 0:       # Nếu chia hết cho 3
#         print(i)

# n = int(input("Nhập số nguyên dương n: "))
# tong = 0
# for i in range(1, n + 1):
#     if i % 2 != 0:  
#         tong += i 
# print(f"Tổng các số lẻ từ 1 đến {n} là: {tong}")


# nums = [3, -2, 0, 7, -5, 0, 1] 
# so_duong = 0
# so_am = 0
# so_0 = 0

# # Duyệt qua từng phần tử trong list
# for n in nums:
#     if n > 0:
#         so_duong += 1
#     elif n < 0:
#         so_am += 1
#     else:
#         so_0 += 1

# # In kết quả
# print(f"Số dương: {so_duong}")
# print(f"Số âm: {so_am}")
# print(f"Số bằng 0: {so_0}")

# n = int(input("Nhập số nguyên dương n: "))

# # Khởi tạo biến tổng ban đầu là 0
# tong = 0

# # Duyệt từ 1 đến n
# for i in range(1, n + 1):
#     # Nếu i là số lẻ (chia 2 kq #0)
#     if i % 2 != 0:
#         tong = tong + i  # Cộng i vào tổng

# # In kết quả ra màn hình
# print("Tổng các số lẻ từ 1 đến", n, "là:", tong)


# n = int(input("Nhập số nguyên n: "))

# la_so_nguyen_to = True

# # Số nhỏ hơn 2 không phải là số nguyên tố
# if n < 2:
#     la_so_nguyen_to = False
# else:
#     # nếu range(2,n+1) -> n=5, range (2,5+1) -> in ra: 2,3,4,5 -> xét n/i = 5/5 =0 -> nó sẽ rơi vào case false
#     for i in range(2, n):
#         if n % i == 0:
#             # i là số nằm trong vòng lặp từ 2 trở đi. Nếu n chia hết cho i thì không phải số nguyên tố,
#             #  ví dụ i=2, n= 5 -> xét n/2; i=3, n=5 -> xét n/3
#             la_so_nguyen_to = False
            
# if la_so_nguyen_to:
#     print(n, "là số nguyên tố.")
# else:
#     print(n, "không phải là số nguyên tố.")


# # In bảng cửu chương từ 2 đến 9
# for i in range(2, 10):        
#     for j in range(1, 11):    
#         ket_qua = i * j
#         print(f"{i} x {j} = {ket_qua}")

# diem = float(input("Nhập điểm (0 - 10): "))

# if diem >= 9:
#     print("Xếp loại: Xuất sắc")
# elif diem >= 8:
#     print("Xếp loại: Giỏi")
# elif diem >= 6.5:
#     print("Xếp loại: Khá")
# elif diem >= 5:
#     print("Xếp loại: Trung bình")
# else:
#     print("Xếp loại: Yếu")

# n = int(input("Nhập số nguyên n: "))

# for i in range(1, n + 1):        
#     # In từ 1 đến i
#     for j in range(1, i + 1):    
#     #  số trên 1 dòng cách nhau dấu cách
#         print(j, end=" ")  
# # Xuống dòng sau mỗi dòng
#     print()  

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

nums = [10, 8, 3, 20, 15, 20]

# Xoá các giá trị trùng lặp bằng set
unique_nums = list(set(nums))
#  Sắp xếp giảm dần
unique_nums.sort(reverse=True)
print("Số lớn thứ 2 là:", unique_nums[1])
