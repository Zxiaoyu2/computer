"""
程序目标：Rock-paper-scissors-lizard-Spock，石头剪刀布蜥蜴史波克
程序作者：周晓宇
"""

import random



# 0 - 石头  rock
# 1 - 史波克  spock
# 2 - 纸    paper
# 3 - 蜥蜴   lizard
# 4 - 剪刀   scissors

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if choice_name=="石头":
        choice_number=0
    elif choice_name=="史波克":
        choice_number=1
    elif choice_name=="纸":
        choice_number=2
    elif choice_name=="蜥蜴":
        choice_number=3
    elif choice_name=="剪刀":
        choice_number=4

    return choice_number

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        comp_name="石头"
    elif number==1:
        comp_name="史波克"
    elif number==2:
        comp_name="纸"
    elif number==3:
        comp_name="蜥蜴"
    else :
        comp_name="剪刀"
    return comp_name

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

    pass #编写执行代码,代码完成后将pass删除


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    player_choice=choice_name

    player_choice_number=name_to_number(player_choice)

    comp_number=random.randrange(0,5)

    comp_choice=number_to_name(comp_number)

    print("计算机的选择为",comp_choice)

    if player_choice_number==0:

        #用户选择为石头

        if comp_choice==0:
            print("您和计算机出的一样呢")
        elif comp_choice==3:
            print("你赢了")
        elif comp_number==4:
            print("你赢了")
        elif comp_number==2:
            print("计算机赢了")
        elif comp_number==1:
            print("计算机赢了")


    elif player_choice_number==1:

        #用户选择为史波克

        if comp_choice ==1:
            print("您和计算机出的一样呢")
        elif comp_choice == 4:
            print("你赢了")
        elif comp_number == 0:
            print("你赢了")
        elif comp_number == 3:
            print("计算机赢了")
        elif comp_number == 2:
            print("计算机赢了")

    elif player_choice_number==2:

        #用户选择为纸

        if comp_choice ==2:
            print("您和计算机出的一样呢")
        elif comp_choice == 1:
            print("你赢了")
        elif comp_number == 0:
            print("你赢了")
        elif comp_number == 3:
            print("计算机赢了")
        elif comp_number == 4:
            print("计算机赢了")

    elif player_choice_number==3:

        #用户选择为蜥蜴

        if comp_choice ==3:
            print("您和计算机出的一样呢")
        elif comp_choice == 1:
            print("你赢了")
        elif comp_number == 2:
            print("你赢了")
        elif comp_number == 0:
            print("计算机赢了")
        elif comp_number == 4:
            print("计算机赢了")

    elif player_choice_number==4:

        #用户选择为剪刀

        if comp_choice ==4:
            print("您和计算机出的一样呢")
        elif comp_choice == 3:
            print("你赢了")
        elif comp_number == 2:
            print("你赢了")
        elif comp_number == 0:
            print("计算机赢了")
        elif comp_number == 4:
            print("计算机赢了")






    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”




# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name == "石头" or choice_name == "剪刀" or choice_name == "纸" or choice_name == "史波克" or choice_name == "蜥蜴":
    rpsls(choice_name)
else:
    print("Error: No Correct Name")
