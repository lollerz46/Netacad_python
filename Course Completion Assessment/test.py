# length = 3

# def board():
#     for i in range(length):
#         for j in range(length):
#             if(i == 0 or i == length - 1 or j == 0 or j == length - 1):
#                 print('*', end = ' ')
#             else:
#                 print(' ', end = ' ')
#         print()
        
# def display_board(board):
#     # The function accepts one parameter containing the board's current status
#     # and prints it out to the console.
#     table = [(a,1,x),(a,2,x),(a,3,x),(b,1,x),(b,2,x),(b,3,x),(c,1,x),(c,2,x),(c,3,x)]
#     print(table)
    
    
# display_board

# def display_board(board):
# 	print("+-------" * 3,"+", sep="")
# 	for row in range(3):
# 		print("|       " * 3,"|", sep="")
# 		for col in range(3):
# 			print("|   " + str(board[row][col]) + "   ", end="")
# 		print("|")
# 		print("|       " * 3,"|",sep="")
# 		print("+-------" * 3,"+",sep="")
  
# print(display_board(1))

x = int(input())
y = int(input())
 
x = x // y
y = y // x
 
print(y)
 