import math

def Min_Max(Current_Depth, Node, Max_Turn, Scores, Target_Depth):
    if (Current_Depth == Target_Depth):
        return Scores[Node]

    if (Max_Turn):
        return max(Min_Max(Current_Depth + 1, Node * 2, False, Scores, Target_Depth),
                    Min_Max(Current_Depth + 1, Node * 2 + 1, False, Scores, Target_Depth))
    else:
        return min(Min_Max(Current_Depth + 1, Node * 2, True, Scores, Target_Depth),
                    Min_Max(Current_Depth + 1, Node * 2 + 1, True, Scores, Target_Depth))

Scores = [3, 5, 2, 9, 7, 4, 1, 8, 6]
Depth_Of_Tree = math.log(len(Scores), 2)
print("The optimal value is: ", end = "")
print(Min_Max(0, 0, True, Scores, Depth_Of_Tree))

