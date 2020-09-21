import random





# import random
# a1=['张','金','李','王','赵']
# a2=['玉','明','龙','芳','军','玲']
# a3=['立','玲','','国',]
# print()
# for i in range(1):
#     name=random.choice(a1)+random.choice(a2)+random.choice(a3)
# print(name)

# def s():
#     import random
#     a = random.choices("0123456789",k=8)
#     return print(('134')+''.join(a))
# s()
#
# def s(q,w):
#     import random
#     a = random.choices(q,k=w)
#     print(''.join(a))
# s("rerueyu65468",6)


import random

#
# def phone():
#     hao_duan_list = ["131",'185','181','183','182','184','186','187','188','189',"131","130","132","133","134","135","136"]
#     hao_duan = random.choice(hao_duan_list)
#     res = random.choices("0123456789",k=8)
#     ba_wei = "".join(res)
#     return hao_duan + ba_wei
#
# print(phone())


print()
try:
    r = open("b.txt","r")
except (Exception) as e :
    print(e)
    print("程序遇到了问题")

except ZeroDivisionError as e:
    print("重新打开文件")
else:
    print("程序运行没报错")
finally:
    print("不管程序有没有报错都会运行")
    print("打开文件")

     ##########################################
    #################################
    #############################