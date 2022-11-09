# l=int(input("ligne : "))
# h=int(input("colonne : "))
# tableau=""
# #rajouter '-' dans un tableau 3x3
#     #peut être en faisant une liste ou créé une fonction
# for l in solution:
#     tableau = tableau + "- "

# tableau= tableau +[]

# for i in range(1, h+1):
#     for j in range(1, l+1):
#         if i == 1 or i == h :#or j == 1: #or j == c+1:
#             #print("* ",end="")
#             print("- ",end="")
#         elif j == 1 or j == l:
#             print("| ",end="")
#         else:
#             print("  ",end="")
#     print()

M=[['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]

for i in range(len(M)):
    for j in range(len(M)):
        print(M[i][j], end=" ")
    print("")