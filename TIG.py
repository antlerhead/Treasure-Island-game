print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

door = input("left or right? ")

if door == "left":
  print("walk into another room ")
else:
  print("game over")

door_2 = input("swim or wait ")

if door_2 == "swim":
  print("shark attack GAME OVER")
else:
  print("proceeeeeed touch nothing but the LAMP! ")

door_3 = input("which door? Red, Blue or Yellow ")

if door_3 == "Red":
  print("burned by fire")
elif door_3 == "blue":
  print("eaten, GAME OVER")
elif door_3 == "Yellow":
  print("You win!")
else:
 print("eaten, GAME OVER") 