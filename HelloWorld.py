secret_number = int(input("Enter The Secret Number"))
while True:
 guess_number = int(input("\tGuess The Number"))
 if guess_number == secret_number:
      print("\nCorrect Guess")
      break

 else:
  print("Try Again")