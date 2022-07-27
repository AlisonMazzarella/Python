import time 

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes", "YES"]
no = ["N", "n", "no", "NO"]

sword = 0
gold = 0

required = ("\nUse only A, B, or C\n")

def intro():
  print ("""

  After a feverish night out with friends celebrating the winter solstice, you awaken the next morning alone in a foggy, dark forest.
  Unsure how you got there you try to sit up and recall the nights events. 
  You feel a sickening twist of despair in your stomach when you hear an animalistic snarl coming from behind you. 
  A ravenous werewolf is bareling towards you at high speeds. 
  What will you do? 
  
  """)
  time.sleep(1)
  print ("""  A. Grab a nearby hatchet and throw it at the werewolf
  B. Lie down and wait to be eaten alive
  C. Run away""")
  choice = input(">>> ") 
  if choice in answer_A:
    option_hatchet()
  elif choice in answer_B:
    print ("\nWhy would you choose that option. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_run()
  else:
    print (required)
    intro()

def option_hatchet(): 
  print ("\nThe werewolf is stunned, in all its years of eating elves none of them have ever fought back. He quicky regains his senses and begins "
  "running towards you again, ready to attack even harder. Will you:")
  time.sleep(1)
  print ("""  A. Run far far away and scream for help
  B. Throw a broken arrowhead
  C. Climb a nearby tree and hide""")
  choice = input(">>> ")
  if choice in answer_A:
    option_run()
  elif choice in answer_B:
    print ("\nYou decide to throw the broken arrowhead, even though " 
    "the hatchet did no damage. The arrowhead sails right over the "
    "werewolfs head. You missed and for revenge he eats you. \n\nYou died!")
  elif choice in answer_C:
    option_tree()
  else:
    print (required)
    option_hatchet()

def option_tree():
  print ("\nYou hesitate, since the tree is so tall and "
  "has hardly any branches. Before you fully reach the top though you notice a glowing silver sword on "
  "the ground. Do you climb down and pick it up, YES / NO? ")
  choice = input(">>> ")
  if choice in yes:
    sword = 1 
  else:
    sword = 0
  print ("\nWhat do you choose to do next?")
  time.sleep(1)
  print ("""  A. Climb the tree all the way to the top and hide
  B. Attack
  C. Run""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nWell that's surprising! You would rather waste your energy climbing a bald tree? I am pretty "
    "sure the werewolf can see you up there, and can climb trees? Not sure, but "
    "I'm going with YES, so if that's really what you choose then...\n\nCongrats! You died!")
  elif choice in answer_B:
   if sword > 0:
    print ("\nYou hide behind a nearby boulder and wait. Your heavy breathing and scent of perspiration "
    "attracts the werewolf, which has no idea you found the sword of destiny. As he creeps "
    "closer and closer, your heart begins to beat rapidly, your stomach turns and you want to throw up. As the werewolf "
    "reaches out to grab you, you stab the blade deep into "
    "its heart. \n\n Amazing survival instincts! You survived!")
   else:
     print ("\nYou should have picked up the sword. You have no "
     "more hatchets or arrowheads. \n\nI am sorry but...You died!")
  elif choice in answer_C:
    print ("As the werewolf ascends to the highest peak of the tree, you descend down a hole in the core "
    "and land safely on your feet. You're several paces away, before the werewolf reaches "
    "the top and notices you're gone.")
    option_run()
  else:
    print (required)
    option_tree()

def option_run():
  print ("\nYou run as quickly as possible, but the werewolf has giant paws and is "
  "just too quick. He has almost caught up with you. What will you do? ")
  time.sleep(1)
  print ("""  A. Hide behind another boulder
  B. Fight because you're tired of running and hiding
  C. Run towards the cart path and hopefully find help""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("At this point the werewolf easily catches your scent and eats you alive. "
    "\n\nYou died!")
  elif choice in answer_B:
    print ("\nWith no more weapons to defend yourself with the werewolf easily overpowers you. "
    "\n\nYou died!")
  elif choice in answer_C:
    option_help()
  else:
    print (required)
    option_run()
    
def option_help():
  print ("\nWhile running for your life, you notice a beautiful gilded "
  "sword lying in manure. Holding your breath from the stench you quickly bend down and grab it, "
  "but the hilt is too slippery from all the dung. You try to quiet your nerves as you hide "
  "behind an old burned down inn, hoping the werewolf will not come "
  "sneaking around the corner. While waiting you notice a huge sack of gold "
  "near your foot. Do you dare pick it up? YES / NO")
  choice = input(">>> ")
  if choice in yes:
    gold = 1 
  else:
    gold = 0
  print ("You hear its ragged claws drag across the stone floor and ready yourself for "
  "the impending doom.")
  time.sleep(1)
  if gold > 0:
    print ("\nYou quickly hold out the gold, as a peace offering "
    "hoping it will stop the werewolf from trying to kill you. Success! The werewolf accepts the peace offering and promises to leave you alone. "
    "\n\nTotally unexpected, but you survived!")
  else:
     print ("\nMaybe you should have taken a risk and picked up the sack of gold. "
     "\n\nYou died!")

intro()