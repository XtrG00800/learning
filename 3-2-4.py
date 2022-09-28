
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above we've created four variables: two team names and two
#scores. A team wins if their score is greater than the other
#team's score.
#
#Add to the code below. To print a messages like these
#depending on the values:
#
# - If one team beat the other, print:
#     "[winner] beat [loser] by [margin]"
# - If neither team won, print:
#     "[team_1] played [team_2] and it was a tie"
#
#For example, with the original values in this code, you
#should print "Georgia Tech beat Georgia by 1"
#
#Hint: to make this easier, create three variables: winner,
#loser, and margin. Then, find their values before worrying
#about printing the final message.


#Add your code here!

team_1 = "Georgia Tech"
team_1_score = 29
team_2 = "Georgia"
team_2_score = 28

result = team_1_score - team_2_score

print()
geotechw = "Georgia Tech beat Georgia by"
geow = "Georgia beat Georgia Tech by"
result1 = abs(result)


if team_1_score >= team_2_score and not team_1_score == team_2_score:
    print(geotechw, result1)

else:
    print("")

if team_2_score >= team_1_score and not team_1_score == team_2_score:
    print (geow, result1)

else:
    print("")
    
    
    


if team_1 == "Georgia Tech":
    print("")

else:
    print("")


count = 5
while count > 0:
    print("")
    count -= 1
else:
    print("")

