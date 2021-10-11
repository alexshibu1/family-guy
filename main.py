'''

Name: Alex Shibu

'''
def main():

  #Introduction to the game
  import time
  score = 0
  monkeyfind = 0

  roomlist = []

  #North, East, South, West
  #Level 1
  room = ["\n\nYou're in Peter's Living Room\n",2,None,None,1]
  roomlist.append(room)
  room = ["\nYou are now in Peter's Kitchen\nPlease type\033[1m w d s a\033[0m to continue your exploration or you can type \033[1mc\033[0m to take the challenge in this room.\n",None,0,None,None]
  roomlist.append(room)
  room = ["\nYou've walked up stairs and now you're on the second level of the Griffin House\n",None,None,0,28]
  
  #Blank Don't Look Below
  roomlist.append(room)
  room = ["Room",None,None,None,None]
  roomlist.append(room)
  room = ["Room ",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)
  room = ["Blank",None,None,None,None]
  roomlist.append(room)

  #North, East, South, West
  #Level 2
  room = ["\nYou're in Peter & Lois' Room",21,None,None,28]
  roomlist.append(room)
  room = ["\nYou're in Peter & Lois' Bathroom",None,None,20,None]
  roomlist.append(room)
  room = ["\n",28,None,None,None]
  roomlist.append(room)
  room = ["\nIt looks like you've found Stewie's Room\nPlease type\033[1m w d s a\033[0m to continue your exploration or you can type \033[1mc\033[0m to enter Stewies secret weapons room and take the challenge\n",None,28,None,None]
  roomlist.append(room)
  room = ["\nYou're in Chris' Room",26,29,None,None]
  roomlist.append(room)
  room = ["\nYou're in Meg's Room",27,None,None,29]
  roomlist.append(room)
  room = ["\nYou're in Chris' Closet",None,None,24,None]
  roomlist.append(room)
  room = ["\nYou're in Meg's Closet",None,None,25,None]
  roomlist.append(room)
  room = ["\nYou're in Hallway Bottom",29,20,22,23]
  roomlist.append(room)
  room = ["\nYou're in Hallway Top",None,25,28,24]
  roomlist.append(room)


  current_room = 0
  done = False
  
  #Welcome
  print '\033[1m\033[94m\033[94mWelcome to Family Guy - Quest for Survival\033[94m\033[0m'


  print "The game is just like the Griffin house and if you remember the show it's easy. You've been binge watching all of the episodes, suddenly you fall asleep and wake in their house.\n\n\033[1m\033[94mInstructions:\033[94m\033[0m\nYour objective is to go throughout the house complete tasks. Colect Points. When you have\033[1m\033[94m 10 points\033[94m\033[0m you win.\n\nYou're in Peter's Living Room\n"

  print "Use the letters\033[1m\033[94m w d s a\033[94m\033[0m to move around the Peter house"


  while done == False:
    
    direction = raw_input("Which direction do want to explore? \n\nw = North \nd = East\ns = South \na = West\nEnter: ")

    #Noth
    if direction == "w":
      next_room = roomlist[current_room][1]
      if next_room == None:
        print "There Is No Pathway. You're Dead!!\nRestarting...\n\n\n"
        time.sleep(.7)
        main()
      else:
        current_room = next_room
        print roomlist[current_room][0]

    #East
    if direction == "d":
      next_room = roomlist[current_room][2]
      if next_room == None:
        print "There Is No Pathway. You're Dead!!\nRestarting...\n\n\n"
        time.sleep(.7)
        main()
      else:
        current_room = next_room
        print roomlist[current_room][0]

    #South
    if direction == "s":
      next_room = roomlist[current_room][3]
      if next_room == None:
        print "There Is No Pathway. You're Dead!!\nRestarting...\n\n\n"
        time.sleep(.7)
        main()
      else:
        current_room = next_room
        print roomlist[current_room][0]

    #West
    if direction == "a":
      next_room = roomlist[current_room][4]
      if next_room == None:
        print "There Is No Pathway. You're Dead!!\nRestarting...\n\n\n"
        time.sleep(.7)
        main()
      else:
        current_room = next_room
        print roomlist[current_room][0]
   
    if current_room == 1:
      
      if direction == "c":
        print '\nWelcome to the kitchen challenge\n\nYou get 2 points for completing this challenge.\nYou walk into the kitchen to get some snacks but you suddenly hear paws rapidly walking towards the kitchen'
        #Challenge 1
        challenge1 = raw_input("\nWhat do you do? \n\n1 = Jump up on counter top and hide in the cabnet \n2 = Stand againt the wall and hope he doesn't see you\n3 = Jump out thw window\n4 = Hide in the refrigerator\nEnter: ")

        if challenge1 == "1":
          time.sleep(.5)
          print '\n\nYou jump up on counter top and hide in the cabnet. But Brain comes and opens the counter.\n\033[1mYou Die...\033[0m Back to the kitchen\n\n'
        if challenge1 == "2":
          time.sleep(.5)
          print '\n\nYou Stand againt the wall and hope he doesn not see you. But Brain comes in and sees you breathing.\n\033[1mYou Die...\033[0m Back to the kitchen \n\n'
        if challenge1 == "3":
          time.sleep(.5)
          print '\n\nYou Jump out thw window.\n\033[1mYou Die...\033[0m Back to the kitchen\n'
        if challenge1 == "4":
          time.sleep(.5)
          print '\n\nYou Hide in the refrigerator. Brain never sees you.\n\033[1mYou Survive. You Win!\033[0m \n'
          score = score + 2
    
    if current_room == 23:
       #Challenge 2

      if direction == "c":
        print '\nYou are now in Stewies secret weapons room\nYou get 2 points for completing this challenge.\n\nWhat is Stewies middle name?'
        challenge2 = ["\n1) Bobafett \n2) Gilligan \n3) Garrison\n4) Gomer"]

        for ans1 in challenge2:
          print ans1

          challengeOpt2 = raw_input("\nEnter: ")

          if challengeOpt2 == "2":
            time.sleep(.5)
            print '\n\nYour right\n\033[1mYou Win!\033[0m \n'
            score = score + 2
            print 'Now that you got this right their is bonus question that can double the points you earned or you lose all 2 points.\nPlease Answer(y/n):\n\n'
          else:
            print '\n\nSorry but your wrong. We will give you an option to try again to earn the two points you lost earlier but if you get this one wrong you lose 2 points from you current score\nPlease Answer(y/n):\n\n'

          challenge2a =raw_input("Enter: ")
            
          if challenge2a == 'y':
            print "\nWhen Stewie was born, what did the doctor discover in Lois' womb"
            challenge2a = ["\n1) Plans to Bomb Australia \n2) Plans to Bomb Europe \n3)Plans to Bomb Canada \n4) Plans to Bomb Mexico"]
              
            for ans2 in challenge2a:
              print ans2
              challengeOpt2a = raw_input("\nEnter: ")
              if challengeOpt2a == "2":
                time.sleep(.5)
                print '\n\nYour right\n\033[1mYou Survived. You Win!\033[0m Back to Stewies Room\n'
                score = score + 2
              else:
                print 'You just lost 2 point. Sorry. Back to Stewies Room'
                score = score + 2
          elif challenge2a == 'n':
            print '\nBack to Stewies Room for you!\n\n'
    #Challenge 3     
    if current_room == 26:
      print "You just found Chris' Closet you get 4 extra points if you answer this currectly. Which season was the evil monkey fist seen(Ex. 1, 3, 4, ext..)"
      monkey1 = raw_input("Enter: ")
      if monkey1 == "8":
        print "You just got 4 points"
        score = score + 4
        print 'Chris just lost his monkey his is hiding somwhere in the house. Go find him!'
        #Challenge 6
        monkeyfind = 1

      else:
        print 'You are wrong but many hidden places await you. Hint. Hint :)'
        print 'Chris just lost his monkey his is hiding somwhere in the house. Go find him!'
        monkeyfind = 1

    #Challenge 4
    def megCloset():
      monkeyfind = 2

      print "\nYou just found Meg's Closet you get 4 extra points if you answer this currectly. Meg's license shows her weight to be 176 and her height to be 5'5\n(true/false)\n"
      meg1 = raw_input("Enter: ").lower()

      meg1ans = False

      if meg1 == "false":
        meg1ans = True

      if meg1ans == True:
        print "\nYou just got 4 points!\n"
        score=+4
        monkeyfind = 1

        if monkeyfind == 2:
          print "Good Job you just found Chris' monkey. He was hiding in Meg's Closet"

      else:
        print 'You are wrong but many hidden places await you. Hint. Hint :)'
        if monkeyfind == 2:
          print "Good Job you just found Chris' monkey. He was hiding in Meg's Closet"
    
    if current_room == 27:
      megCloset()
    
    #Challenge 5
    if current_room == 20:
      name = 'seth'
      print "\nTo get into this room and get 4 points, type 4 letters of a name that bring this show all togather"
      entry1= raw_input("Enter 4 Letters: ")

      if entry1 ==name:
        print("\nCongrats! You got it, Seth MacFarlane the creator of this and any shows alike. The door is now unlocked\n\nYour currenly in Peters room")
      else:
        print "Sorry You're back to the hallway. But keep trying\n"
        current_room = 28

    if score >= 10:
      done = True
      print 'You have 10 Point,\033[1m You Win!\033[0m '
      
    #Challenge 7
    if current_room == 21:

      print("\n\033[1mWELCOME TO PETER'S BATHROOM\033[0m\n\n") 
      print("The is the ultimate Family Guy Quiz\nYou have 5 questions and if you get all of the correct you can earn up to 10 points with just this quiz.\n Hope you like it! :)\n \n \n")
      print("Instructions:\n")

      print("Remember to answer, just type a, b or c only in lowercase.\n\n")

      #Waiting 1.2 Sec
      time.sleep(1.2)

      #Setting a List with all the question Answers
      answers = ["b", "b", "a", "b", "c"]

      #Print Question 1
      print "How old is Quagmire?"


      #Question 1 Options with differant list
      q1opt = [" a) 55", " b) 61", " c) 42"]
      for item in q1opt:
        print item

      #Receives and stores answer 
      answer1=raw_input("Please Answer: ")

      #Print Question 2
      print "\nPeter's favorite song of all time?"

      #Question 2 Options with varible and adding to string
      a2 = " \n b) Surfing Bird-Thrashmen \n c) Baby I Love Your Way- Peter Frampton"
      print ' a) Shipoopi- Music Man ', a2

      #Receives and stores answer 
      answer2=raw_input("Please Answer: ")

      #Print Question 3
      print "What is Peter's middle name?"

      #Question 3 Options
      print " a) Lowenbrau \n b) Lowanbrau \n c) Lowenbrae \n"

      #Receives and stores answer 
      answer3=raw_input("Please Answer: ")


      #Created a 2D list with two column and 4 rows   
      question452D = []
      #Add variables to the table 
      question452D.append(["Which person does the voice for Cleveland Brown?", "In 'A Very Special Family Guy Freakin' Christmas, what  bands Christmas special does Peter insist on watching?"])
      question452D.append([" a) Mike Henry"," a) Twisted Sister"])
      question452D.append([" b) Will Henry"," b) KISS"])
      question452D.append([" c) Winren Henry"," c) Bon Jovi"])

      #Print question 4 from the list
      print question452D[0][0]

      #Question 4 Options from the table
      print question452D[1][0]
      print question452D[2][0]
      print question452D[3][0]
  
        #Receives Answer and stores it 
      answer4=raw_input("Please Answer: ")

        #Print Question 5 from the table
      print question452D[0][1]

      #Question 5 Options from the table
      print question452D[1][1]
      print question452D[2][1]
      print question452D[3][1]

      #Receives Answer and stores it 
      answer5=raw_input("Please Answer: ")

  
      #wait few seconds
      time.sleep(2)

        #if user ans for question one matches ans from the list add 1
      if answer1 == answers[0]:
        print '\nQuestion 1 Currect - You are Right\n'
        score = score + 2
      elif answer1 != answers:
        #else your wrong
        print '\nQuestion 1 Incorrect - You are Wrong :(\n\n'
 
      #wait few seconds
      time.sleep(1)

      #if user ans for question one matches ans from the list add 1
      if answer2 == answers[1]:
        print 'Question 2 Currect - You are Right\n'
        score = score + 2
      elif answer2 == 'a' or 'b':
        print 'Question 2 Incorrect - You are Wrong :(\n\n'

        #wait few seconds
      time.sleep(1)

      #if user ans for question one matches ans from the list add 1
      if answer3 == answers[2]:
        print 'Question 3 Currect - You are Right\n'
        score = score + 2
      elif answer3 == 'c' or 'b':
      #else your wrong
        print 'Question 3 Incorrect - You are Wrong :(\n\n'

      #wait few seconds
      time.sleep(1)

        #if user ans for question one matches ans from the list add 1
      if answer4 == answers[3]:
        print 'Question 4 Currect - You are Right\n'
        score = score + 2
      elif answer4 == 'c' or 'b':
        #else your wrong
        print 'Question 4 Incorrect - You are Wrong :(\n\n'

      #wait few seconds
      time.sleep(1)

        #if user ans for question one matches ans from the list add 1
      if answer5 == answers[4]:
        print 'Question 5 Currect - You are Right\n'
        score = score + 2
      elif answer5 == 'c' or 'a':
        #else your wrong
        print 'Question 5 Incorrect - You are Wrong :(\n\n'

        #wait few seconds
      time.sleep(3)

        #if score is a number from 0-5 then you get a message
      if score ==10:
        print 'Great Job you got 100%. \nWell You My Friend. You Apple  Content\n' 
      elif score <= 8:
        print 'Sorry But... \nYour Dumb :( \n We have taken you bank to the bathroom type\033[1m C \033[0m'
      elif score == 6 or 4:
        print 'You Did Pretty Well. Good Job!\n'
      elif score == 0 or 2:
        print 'You Did Extremely Bad! You Should Really Replay\n'

      #wait few seconds
      time.sleep(2)

      #if score is a number from 0-5 then you get your mark out of 5
      if score == 5:
         print 'You Got 5/5'
      elif score == 4:
         print 'You Got 4/5'
      elif score == 3:
        print 'You Got 3/5'
      elif score == 2:
        print 'You Got 2/5'
      elif score == 1:
        print 'You Got 1/5'
      elif score == 0:
        print 'You Got 0/5'
    
    #Challenge 8
    if current_room == 22:

      print '\033[1mWelcome to the Main Bathroom \033[0m\n'
      print 'You have 30 seconds to guess how many rooms this house has open to the player.\n\033[1mYou time starts now!!! \033[0m\n'

      roomguess=raw_input("Enter: ")

      timer=int(40)
      while (timer != 0 ):
        timer=timer-1
        time.sleep(1) 
      
      if timer == 0:
        print 'You ran out of time (:'
      
      roomguess=raw_input("Enter: ")
      if roomguess == "12":
        print 'You just got 3 extra points. Great job!'
        score = score + 3 
      elif roomguess != "12":
        print "You're wrong back to the Hallway"

    #wait few seconds
    time.sleep(2)   
    
    if score >= 10:
      done = True
      print 'You have 10 Point,\033[1m You Win!\033[0m \n You just survied in the Peter House.\n Great Job'

    if done == True:
      print "\n\nWould You like to restart the program?(y/n)"
      #Recives y/n
      restart =raw_input("Please Answer(y/n): ")
      #If y then return to main
      if restart == 'y':
       main()
      #If n then exit
      elif restart == 'n':
       exit()

main()
