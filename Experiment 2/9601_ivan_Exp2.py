import random
x=[]
o=[]
empty =[1,2,3,4,5,6,7,8,9]
corner = [6,2,8,4]
board =[[" "," "," "],[" "," "," "],[" "," "," "]]
flag =True
game_over = False
temp = False
num_index={
 9: [0, 2],
 8: [0, 1],
 7: [0, 0],
 6: [1, 2],
 5: [1, 1],
 4: [1, 0],
 3: [2, 2],
 2: [2, 1],
 1: [2, 0]}
#do num magic change in name
index_magic ={
    9:4,
    8:3,
    7:8,
    6:9,
    5:5,
    4:1,
    3:2,
    2:7,
    1:6
 }
 #do  magic num change in name
magic_index ={
    4:9,
    3:8,
    8:7,
    9:6,
    5:5,
    1:4,
    2:3,
    7:2,
    6:1
 }
def winPoss(arr):
  for i in range(0,len(arr)):
      for j in range(i+1,len(arr)):
        ans = 15-(arr[i]+arr[j])
        for num in empty:
          if num == ans:
            return True, magic_index[ans]
  return False, 0
  i = 3
  while i>0:
   if flag  :
    if len(corner)==0:
       bot = random.choice(empty)
    else:
       bot = random.choice(corner)
       t=corner.remove(bot)
   else:
    bot = random.choice(empty)
  t=empty.remove(bot)
  x.append(bot)
  print(x)
  bot = magic_index[bot]
  board[num_index[bot][0]][num_index[bot][1]] ="X"
  print('\n'.join(map(str,board)))
  player = int(input("Enter position for 'O' "))
  empty.remove(index_magic[player])
  try:
      t = corner.remove(index_magic[player])  
  except :
      pass
  o.append(index_magic[player])
  board[num_index[player][0]][num_index[player][1]]= "O"
  print('\n'.join(map(str,board)))
  if (player == 5):
    i=i-1
    flag = False
  i = i -1
while not game_over:
  winx,num = winPoss(x)
  if winx:
      game_over = True
      board[num_index[num][0]][num_index[num][1]] ="X"
      print('\n'.join(map(str,board)))
      t=empty.remove(index_magic[num])
      x.append(index_magic[num])
      print("Machine is the winner")
      break

  else :
      wino,num1 = winPoss(o)
      if wino:
        board[num_index[num1][0]][num_index[num1][1]] ="X"
        x.append(index_magic[num1])
        t=empty.remove(index_magic[num1])
        print('\n'.join(map(str,board)))
      else:
        bot = random.choice(empty)
        t=empty.remove(bot)
        bot = magic_index[bot]
        board[num_index[bot][0]][num_index[bot][1]] = "X"
        x.append(bot)
        print('\n'.join(map(str,board)))
  print(empty)
  if len(empty) == 0 :
   print("Draw")
   break
  player = int(input("Enter position for 'O' "))
  empty.remove(index_magic[player])
  o.append(index_magic[player])
  board[num_index[player][0]][num_index[player][1]]= "O"
  print('\n'.join(map(str,board))) 
  for i in range(0,len(o)):
    for j in range (i+1,len(o)-1):
      sum = o[i]+o[j]+o[j+1]
      if sum == 15:
        temp =True
        break
  if temp :
      game_over = True
      winner = "x"