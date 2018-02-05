import sys

def read_file(textfile):
	f=open(textfile,'r')
	next(f)
	i=0
	j=0
	matrix=[[0 for x in range(9)] for y in range(9)]
	while True:
		j=0
		char=f.readline()
		for c in char:
			matrix[i][j]=int(c)
			j=j+1
			if j==9:
				i=i+1
				break
		if i==9:
			break
	return matrix

def check_soduku(row,column,number,matrix_board):
	check=0
	for i in range(0,9):
		if matrix_board[row][i]==number:
			check=1
	for i in range(0,9):
		if matrix_board[i][column]==number:
			check=1
	row=row-row%3
	column=column-column%3

	for i in range(0,3):
		for j in range(0,3):
			if matrix_board[row+i][column+j]==number:
				check=1
	if check==1:
		return False
	else:
		return True
class calls:
	number_of_calls=0
c=calls()

def sudoku_solver(matrix):
	c.number_of_calls=c.number_of_calls+1
	break_condition=0
	checking_range=[]
	for i in range(0,9):
		for j in range(0,9):
			if matrix[i][j]==0:
				break_condition=1
				temp=[]
				temp.append([i,j])
				temp_2=[]
				for num in range(0,10):
					if check_soduku(i,j,num,matrix):
						temp_2.append(num)
				temp.append(len(temp_2))
				checking_range.append(temp)
	if break_condition==0:
		print("Smart Backtracking Algorithm MRV Solution: ")
		for i in matrix:
			print(i)
		print("Amount of Recursions: ")
		print(c.number_of_calls)
		exit(0)

	minimum_range_selection=checking_range[0][0]

	low=checking_range[0][1]
	for i in range(0,len(checking_range)):
		if checking_range[i][1]<low:
			low=checking_range[i][1]
			minimum_range_selection=checking_range[i][0]
	row=minimum_range_selection[0]
	column=minimum_range_selection[1]

	for i in range(0,10):
		if check_soduku(row,column,i,matrix):
			matrix[row][column]=i
			if sudoku_solver(matrix):
				return True
			matrix[row][column]=0
	return False

matrix=read_file(sys.argv[1])
sudoku_solver(matrix)
