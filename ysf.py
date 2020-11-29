def move(players,step):
    num = step - 1
    while num > 0:
        tmp = players.pop(0)
        players.append(tmp)
        num = num - 1    
   

    
    return players



def play(players, step, alive):
    """
    模拟约瑟夫问题的函数
    
    Input:
    players: 参加游戏的人数；
    step: 数到step数字的人数淘汰；
    alive: 幸存人数，游戏结束。
    
    Output:
    返回一个列表，列表中的元素为幸存者编号。
    
    """
   
    

    L = [i for i in range(1,players+1)]
    
    while len(L)>alive:
        
        L = move(L,step)
        L.pop(0)    
    return(L)
players_num = int(input("请输入参加游戏的人数"))
step_num = int(input("请输入淘汰的数字"))
alive_num = int(input("请输入幸存的人数"))

alive_list = play(players_num, step_num, alive_num)
print(alive_list)