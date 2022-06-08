# Guess the number Game Programme
n1 = 20 #the number what you have to Guess
i = 0
while(True):
    print("Enter Your Number")
    u1 = int(input())# user input
    i = i + 1
    if u1 == n1:
        print("Congrats You Win\n", "Your Total Attemps is 9\n", "You Have Left", 9 - i )
        break
    elif u1 > n1:
        print("Your Number is Bigger Than The Magic Number\n" "Your Total Attemps is 9",  "You Have Left", 9 - i, "Try Again")
        continue
    elif i==9 :
        print("Game Over You Loose", "Your Total Attemps is 9",  "You Have Left", 0,)
        break
    else:
        print("Your Number is Smaller Than The Magic Number\n",  "Your Total Attemps is 9\n", "You Have Left", 9 - i, "Try Again")
        continue