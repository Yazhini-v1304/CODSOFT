import random
import string
def generate_password(length):
  characters=string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters)for _ in range(length))
  return password
  
def main():
    print("Welcome to the password generator!")
  try:
    length = int(input("Enter desired password length:"))
    if length < 4:
      print("Password length should be atleast 4 characters.")
      return
    password = generate_password(length)
    print(f"Your generated password is: {password}")

  except ValueError:
    print("Invalid input. Please enter a numeric value.")

main()
    
