import os

def mainMenu(): 
  print("""
    Welcome to Nokia Services.
    1. Phone book
    2. Messages
    3. Chat
    4. Call register
    5. Tones 
    6. Settings
    7. Call divert
    8. Games
    9. Calculator
   10. Reminders
   11. Clock
   12. Profiles
   13. SIM services
""")



# choice 1        
def phoneBook():
  print("""
    Phone book
    1. Search
    2. Service Nos.
    3. Add name
    4. Erase
    5. Edit
    6. Assign tone
    7. Send b'card
    8. Options
       a. Type of view
       b. Memory status
        
       
""")
  



# choice 2  
def messages():
  print("""
    Messages
    1. Write messages
    2. Inbox
    3. Outbox
    4. Picture messages
    5. Templates
    6. Smileys
    7. Message settings
       a. Set 1
       b. Common
    
""")
  



# choice 3
def chat():
  print("""
    Chat
    1. New chat
    2. Inbox
    3. Outbox
    4. Chat settings
       a. Set up chat
       b. Common

""")




# choice 4
def call_register():
  print("""
    Call register
    1. Missed calls
    2. Received calls
    3. Dialled numbers
    4. Erase recent call lists
    5. Show call duration
       a. Last call duration
       b. All calls' duration
       c. Received calls' duration
       d. Dialled calls' duration
       e. Clear timers
    6. Show call costs
       a. Last call cost
       b. All calls' cost
       c. Clear counters
    7. Call cost settings
       a. Call cost limit
       b. Show costs in

""")
  

# choice 5
def tones():
  print("""
    Tones
    1. Ringing tone
    2. Ringing volume
    3. Incoming call alert
    4. Composer
    5. Message alert tone
    6. Keypad tones
    7. Warning and game tones
    8. Vibrating alert
    9. Screen saver
""")
    


# choice 6
def settings():
  print("""
    Settings
    1. Call settings
       a. Automatic redial
       b. Speed dialling
       c. Call waiting options
       d. Own number sending
       e. Phone line in use
       f. Automatic answer
    2. Phone settings
       a. Language
       b. Cell info display
       c. Welcome note
       d. Network selection
       e. Lights and indicators
       f. Confirm SIM service actions
    3. Security settings
       a. PIN code request
       b. Call barring service
       c. Fixed dialing
       d. Closed user group
       e. Phone security
       f. Change access codes
    4. Restore factory settings
            

""")



# choice 7
def call_divert():
  print("""
    Call divert
    1. All voice calls
    2. When busy
    3. No answer
    4. Not reachable
    5. All data calls
    6. Cancel all diverts
    7. Activate deflection service
    8. Deactivate deflection service
    9. Query deflection status
""")



# choice 8
def games():
  print("""
    Games
    1. Snake
    2. Space Impact
    3. Bantumi
""")
  

  

# choice 9
def calculator():
  print("""
    Calculator
    1. Standard
    2. Scientific
""")



# choice 10
def reminders():   
  print("""   
    Reminders
    1. Alarm clock
    2. Reminders
""")
  


# choice 11
def clock():
  print("""
     Clock
    1. Alarm clock
    2. Clock settings
       a. Time format
       b. Date format
       c. Set time and date
    3. Date setting
    4. Stopwatch
    5. Countdown timer
    6. Auto update of date and time
                            
  """)



# choice 12
def profiles():
  print("""
    Profiles
    1. General
    2. Silent
    3. Meeting
    4. Outdoor
    5. Personal
    6. Profile settings
       a. Ringing tone
       b. Ringing volume
       c. Incoming call alert
       d. Message alert tone
       e. Keypad tones
       f. Vibrating alert
       g. Screen saver
""")


# choicw 13
def sim_services():
  print("""
    SIM services
    1. My services
    2. SIM toolkit
""")



if __name__ == "__main__":
  mainMenu()
  choice = input("Enter your choice: ")

if choice == "1":
  phoneBook()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected Search.")
  elif sub_choice == "2":
    print("You have selected Service Nos.")
  elif sub_choice == "3":
    print("You have selected Add name.")
  elif sub_choice == "4":
    print("You have selected Erase.")
  elif sub_choice == "5":
    print("You have selected Edit.")
  elif sub_choice == "6":
    print("You have selected Assign tone.")
  elif sub_choice == "7":
    print("You have selected Send b'card.")
  elif sub_choice == "8":
    print("You have selected Options.")
    option_choice = input("Enter option (a/b): ")
    if option_choice == "a":
      print("You have selected Type of view.")
    elif option_choice == "b":
      print("You have selected Memory status.")
  else:
    print("Invalid sub-choice.")



elif choice == "2":
  messages()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected Write messages.")
  elif sub_choice == "2":
    print("You have selected Inbox.")
  elif sub_choice == "3":
    print("You have selected Outbox.")
  elif sub_choice == "4":
    print("You have selected Picture messages.")
  elif sub_choice == "5":
    print("You have selected Templates.")
  elif sub_choice == "6":
    print("You have selected Smileys.")
  elif sub_choice == "7":
    print("You have selected Message settings.")
    option_choice = input("Enter option (a/b): ")
    if option_choice == "a":
      print("You have selected Set 1.")
    elif option_choice == "b":
      print("You have selected Common.")
  else:
    print("Invalid sub-choice.")



elif choice == "3":
  chat()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected New chat.")
  elif sub_choice == "2":
    print("You have selected Inbox.")
  elif sub_choice == "3":
    print("You have selected Outbox.")
  elif sub_choice == "4":
    print("You have selected Chat settings.")
    option_choice = input("Enter option (a/b): ")
    if option_choice == "a":
      print("You have selected Set up chat.")
    elif option_choice == "b":
      print("You have selected Common.")
  else:
    print("Invalid sub-choice.")

elif choice == "4":
  call_register()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected Missed calls.")
  elif sub_choice == "2":
    print("You have selected Received calls.")
  elif sub_choice == "3":
    print("You have selected Dialled numbers.")
  elif sub_choice == "4":
    print("You have selected Erase recent call lists.")
  elif sub_choice == "5":
    print("You have selected Show call duration.")
    option_choice = input("Enter option (a-e): ")
    if option_choice == "a":
      print("You have selected Last call duration.")
    elif option_choice == "b":
      print("You have selected All calls' duration.")
    elif option_choice == "c":
      print("You have selected Received calls' duration.")
    elif option_choice == "d":
      print("You have selected Dialled calls' duration.")
    elif option_choice == "e":
      print("You have selected Clear timers.")
  elif sub_choice == "6":
    print("You have selected Show call costs.")
    option_choice = input("Enter option (a-c): ")
    if option_choice == "a":
      print("You have selected Last call cost.")
    elif option_choice == "b":
      print("You have selected All calls' cost.")
    elif option_choice == "c":
      print("You have selected Clear counters.")
  elif sub_choice == "7":
    print("You have selected Call cost settings.")
    option_choice = input("Enter option (a/b): ")
    if option_choice == "a":
      print("You have selected Call cost limit.")
    elif option_choice == "b":
      print("You have selected Show costs in.")
  else:
    print("Invalid sub-choice.")



elif choice == "5":
  tones()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected Ringing tone.")
  elif sub_choice == "2":
    print("You have selected Ringing volume.")
  elif sub_choice == "3":
    print("You have selected Incoming call alert.")
  elif sub_choice == "4":
    print("You have selected Composer.")
  elif sub_choice == "5":
    print("You have selected Message alert tone.")
  elif sub_choice == "6":
    print("You have selected Keypad tones.")
  elif sub_choice == "7":
    print("You have selected Warning and game tones.")
  elif sub_choice == "8":
    print("You have selected Vibrating alert.")
  elif sub_choice == "9":
    print("You have selected Screen saver.")
  else:
    print("Invalid sub-choice.")



elif choice == "6":
  settings()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected Call settings.")
    option_choice = input("Enter option (a-f): ")
    if option_choice == "a":
      print("You have selected Automatic redial.")
    elif option_choice == "b":
      print("You have selected Speed dialling.")
    elif option_choice == "c":
      print("You have selected Call waiting options.")
    elif option_choice == "d":
      print("You have selected Own number sending.")
    elif option_choice == "e":
      print("You have selected Phone line in use.")
    elif option_choice == "f":
      print("You have selected Automatic answer.")
  elif sub_choice == "2":
    print("You have selected Phone settings.")
    option_choice = input("Enter option (a-f): ")
    if option_choice == "a":
      print("You have selected Language.")
    elif option_choice == "b":
      print("You have selected Cell info display.")
    elif option_choice == "c":
      print("You have selected Welcome note.")
    elif option_choice == "d":
      print("You have selected Network selection.")
    elif option_choice == "e":
      print("You have selected Lights and indicators.")
    elif option_choice == "f":
      print("You have selected Confirm SIM service actions.")
  elif sub_choice == "3":
    print("You have selected Security settings.")
    option_choice = input("Enter option (a-f): ")
    if option_choice == "a":
      print("You have selected PIN code request.")
    elif option_choice == "b":
      print("You have selected Call barring service.")
    elif option_choice == "c":
      print("You have selected Fixed dialing.")
    elif option_choice == "d":
      print("You have selected Closed user group.")
    elif option_choice == "e":
      print("You have selected Phone security.")
    elif option_choice == "f":
      print("You have selected Change access codes.")
  elif sub_choice == "4":
    print("You have selected Restore factory settings.")
  else:
    print("Invalid sub-choice.")



elif choice == "7":
  call_divert()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected All voice calls.")
  elif sub_choice == "2":
    print("You have selected When busy.")
  elif sub_choice == "3":
    print("You have selected No answer.")
  elif sub_choice == "4":
    print("You have selected Not reachable.")
  elif sub_choice == "5":
    print("You have selected All data calls.")
  elif sub_choice == "6":
    print("You have selected Cancel all diverts.")
  elif sub_choice == "7":
    print("You have selected Activate deflection service.")
  elif sub_choice == "8":
    print("You have selected Deactivate deflection service.")
  elif sub_choice == "9":
    print("You have selected Query deflection status.")
  else:
    print("Invalid sub-choice.")



elif choice == "8":
  games()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected Snake.")
  elif sub_choice == "2":
    print("You have selected Space Impact.")  
  elif sub_choice == "3":
    print("You have selected Bantumi.")
  else:
    print("Invalid sub-choice.")



elif choice == "9":
  calculator()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected Standard.")
  elif sub_choice == "2":
    print("You have selected Scientific.")
  else:
    print("Invalid sub-choice.")



elif choice == "10":
  reminders()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected Alarm clock.")
  elif sub_choice == "2":
    print("You have selected Reminders.")
  else:
    print("Invalid sub-choice.")



elif choice == "11":
  clock()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected Alarm clock.")
  elif sub_choice == "2":
    print("You have selected Clock settings.")
    option_choice = input("Enter option (a-c): ")
    if option_choice == "a":
      print("You have selected Time format.")
    elif option_choice == "b":
      print("You have selected Date format.")
    elif option_choice == "c":
      print("You have selected Set time and date.")
  elif sub_choice == "3":
    print("You have selected Date setting.")
  elif sub_choice == "4":
    print("You have selected Stopwatch.")
  elif sub_choice == "5":
    print("You have selected Countdown timer.")
  elif sub_choice == "6":
    print("You have selected Auto update of date and time.")
  else:
    print("Invalid sub-choice.")



elif choice == "12":
  profiles()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected General.")
  elif sub_choice == "2":
    print("You have selected Silent.")
  elif sub_choice == "3":
    print("You have selected Meeting.")
  elif sub_choice == "4":
    print("You have selected Outdoor.")
  elif sub_choice == "5":
    print("You have selected Personal.")
  elif sub_choice == "6":
    print("You have selected Profile settings.")
    option_choice = input("Enter option (a-g): ")
    if option_choice == "a":
      print("You have selected Ringing tone.")
    elif option_choice == "b":
      print("You have selected Ringing volume.")
    elif option_choice == "c":
      print("You have selected Incoming call alert.")
    elif option_choice == "d":
      print("You have selected Message alert tone.")
    elif option_choice == "e":
      print("You have selected Keypad tones.")
    elif option_choice == "f":
      print("You have selected Vibrating alert.")
    elif option_choice == "g":
      print("You have selected Screen saver.")
  else:
    print("Invalid sub-choice.")



elif choice == "13":
  sim_services()
  sub_choice = input("Enter sub-choice: ")
  if sub_choice == "1":
    print("You have selected My services.")
  elif sub_choice == "2":
    print("You have selected SIM toolkit.")
  else:
    print("Invalid sub-choice.")


else:
  print("Invalid choice. Please try again.")





