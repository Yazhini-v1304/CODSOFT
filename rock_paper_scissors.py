import random
def get_computer_choice():
  return random.choice(["rock","paper","scissors"])

def get_winner(user,computer):
  if user == computer:
    return "Its a tie!"

elif(user == "rock" and computer == "scissors') or  
     (user == "scissors" and computer == "paper") or
     (user == "paper" and computer == "rock"):
     return "You win!"
else:
     return "Computer wins!"
def play_game():
  user_score =0
  computer_score=0
  while True:
    print("\n Choose rock, paper, or scissors:")
    user_choice = input("Your choice:").lower()
    if user_choice not in["rock","paper","scissors"]:
      print("Invalid choice. Try again.")
      continue

computer_choice = get_computer_choice()
print(f"Computer chose: {computer_choice}")

result = get_winner(user_choice, computer_choice)
print(result)

if "You win" in result:
  user_score +=1

elif"Computer wins" in result:
  computer_score +=1

print(f"Score → You: {user_score} | Computer: {computer_score}")

play_again = input("Do you want to play again? (yes/no): " ).lower()
if play_again !="yes":
  print("Thanks for playing!")
  break

play_game()
  
