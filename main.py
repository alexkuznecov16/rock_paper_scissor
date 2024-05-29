from tkinter import *
from tkinter import messagebox
import random

round_count = 0 # count of passed rounds
user_score = 0 # count of user score by rounds
computer_score = 0 # count of computer score by rounds

# function for game
def game(container):
  global round_count # count of passed rounds
  round_count += 1 # after each round will be added 1 to round count
  if round_count <= 3:
    # Clean full container
    for widget in container.winfo_children():
      widget.grid_forget()
    
    text = Label(container, text='Choose rock, scissor or paper') # Output text for user choose
      
    # button for rock selection
    btn_rock = Button(
      container,
      background="deepskyblue",
      foreground="white",
      highlightthickness=2,
      highlightbackground="red",
      highlightcolor="red",
      activebackground="gray",
      activeforeground="black",
      cursor='hand1',
      border=0,
      text='Rock',
      height=3,
      font=('Arial', 14, 'bold'),
      command=lambda: result(container, 'Rock')
    )
    
    # button for scissor selection
    btn_scissor = Button(
      container,
      background="deepskyblue",
      foreground="white",
      highlightthickness=2,
      highlightbackground="red",
      highlightcolor="red",
      activebackground="gray",
      activeforeground="black",
      cursor='hand1',
      border=0,
      text='Scissor',
      height=3,
      font=('Arial', 14, 'bold'),
      command=lambda: result(container, 'Scissor')
    )
    
    # button for paper selection
    btn_paper = Button(
      container,
      background="deepskyblue",
      foreground="white",
      highlightthickness=2,
      highlightbackground="red",
      highlightcolor="red",
      activebackground="gray",
      activeforeground="black",
      cursor='hand1',
      border=0,
      text='Paper',
      height=3,
      font=('Arial', 14, 'bold'),
      command=lambda: result(container, 'Paper')
    )
    
    
    text.grid(column=1, row=0, pady=20, padx=30) # text position
    
    # Buttons position
    btn_rock.grid(column=0, row=1, padx=5, pady=5) # button for rock choose
    btn_scissor.grid(column=1, row=1, padx=5, pady=5) # button for scissor selection
    btn_paper.grid(column=2, row=1, padx=5, pady=5) # button for paper selection
  else:
    # if steps are greater than the allowed value
    result(container) # call the result function with container argument
  
  
# Function for score and result processing
def result(container, user_choose=None):
  # find global variables
  global round_count # count of passed rounds
  global user_score # count of user score by rounds
  global computer_score # count of computer score by rounds
  
  # Check and result processing
  if user_choose:
    random_choose = random.choice(['Rock', 'Scissor', 'Paper']) # random computer choice
    
    if (user_choose == 'Rock' and random_choose == 'Scissor') or (user_choose == 'Scissor' and random_choose == 'Paper') or (user_choose == 'Paper' and random_choose == 'Rock'):
      user_score += 1 # add 1 to user score
      messagebox.showinfo("Round result", f"Win!\nComputer choice: {random_choose}\nScore: {user_score} : {computer_score}") # notification window: to show live results
      
    elif user_choose == computer_score:
      messagebox.showinfo("Round result", f"Draw!\nComputer choice: {random_choose}\nScore: {user_score} : {computer_score}") # notification window: to show live results
      
    else:
      computer_score += 1 # add 1 to computer score
      messagebox.showinfo("Round result", f"Defeat!\nComputer choice: {random_choose}\nScore: {user_score} : {computer_score}") # notification window: to show live results
      
    if round_count <= 3:
      # if round count is smaller than 3
      game(container) # continue the game
      
    else:
      # Clean full container
      for widget in container.winfo_children():
        widget.grid_forget()
        
      # Result output and processing
      text = Label(container, text=f'Your result: {user_score}\n{"You won against computer!" if user_score >= 2 else f"You won! {user_score} : {computer_score}"}') # Final result output
      text.grid(column=1, row=0, pady=20, padx=30) # text position
      
      # button for game restart
      btn_restart = Button(container, text='Restart', command=lambda: restart_game(container), font=40) # clicking to the button will be called the function for game restart
      btn_restart.grid(row=3, column=1, padx=20, pady=20) # Button position
  else:
    # Clean full container
    for widget in container.winfo_children():
      widget.grid_forget()
      
    # Result output and processing
    text = Label(container, text=f'Your result: {user_score}\n{"You won against computer!" if user_score >= 2 else f"You lost! {user_score} : {computer_score}"}') # Final result output
    text.grid(column=1, row=0, pady=20, padx=30) # text position
    
    # button for game restart
    btn_restart = Button(container, text='Restart', command=lambda: restart_game(container), font=40) # clicking to the button will be called the function for game restart
    btn_restart.grid(row=3, column=1, padx=20, pady=20) # Button position
 
# Function for values and game restart
def restart_game(container):
  global round_count # count of passed rounds
  global user_score # count of user score by rounds
  global computer_score # count of computer score by rounds
  
  round_count = 0 # refresh passed rounds
  user_score = 0 # refresh user score
  computer_score = 0 # refresh computer score
  game(container) # play new game
  

# main function
def main():
  root = Tk() # Creating an app window
  root.title('Rock, scissor, paper') # App title
  root.minsize(200, 400) # App sizes
  
  container = Frame(root) # App container
  container.pack(expand=True) # Pack this container to root
  
  # buttons
  btn_start = Button(container, text='Start', command=lambda: game(container), font=40) # button to start game
  btn_close = Button(container, text='Close', command=root.destroy, font=40) # button to close the app
  
  #buttons position
  btn_start.grid(row=0, column=0, padx=20, pady=20) # start button position
  btn_close.grid(row=0, column=1, padx=20, pady=20) # close button position
  
  root.mainloop() # start app
  

# to run the main code
if __name__ == '__main__':
  main() # main function