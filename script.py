from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)



### Game Set-up ###
num_disks = int(input("\nHow many disks do you want to play with?\n"))

# Checks if user entered in 3 or higher, if not re-prompt the user. #
while num_disks < 3:
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

# Iterate backwards through the range of num_disks and push each onto the stack. #
for i in range(num_disks, 0, -1):
  left_stack.push(i)


# Calculate and return the optimal number of moves to win.
num_optimal_moves = (2 ** num_disks) - 1

print("\nThe fastest you can solve this game is in {moves} moves\n".format(moves=num_optimal_moves))


### Function | Capture user input. #
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {letter} for {name}".format(letter=letter, name=name))
    user_input = input("")
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
      
### Game Execution ###
num_user_moves = 0
while(right_stack.get_size() != num_disks):
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    stack.print_items()
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    # Check if the move is invalid. #
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
    # Check if the move is valid. #
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    # Else executed if user tries to move larger disk onto smaller disk
    else:
      print("\n\nInvalid Move. Try Again")
  print("\n\nYou completed the game in {moves} moves, and the optimal number of moves is {o_moves}".format(moves=num_user_moves, o_moves=num_optimal_moves))
  
  
      
      
      
      
      
      
  





