# pyquiz\ARCHITECTURE.md  |  today's date: 6_10_26

# Synopsis: 
- quiz.py and cards.py are the core files. main.py is like a simple breaker box.  
-  


# Recent Development:
8.6.26 Added note attachment feature to tkinter popup. Now when user inputs answer, answer explanation shows in popup to go with answer check. Can be edited in 3. Edit mode. So now there is an enlargeable popup of the question and an attachable note for the answer. 
7.20.26 Added pyquiz_demo.gif to repo showing pyquiz features. 
6.10.26: Finally got Tkinter to work with pyquiz. Trick was to start over by attaching a relay as it were called "display" then to toggle on/off popup window per question by adding it to Edit Mode as, t = toggle. Defensive development as it were. So user will see Type I card question in terminal window and at once zoomed up as desired in Tkinter popup window. Then added g = toggle gui as well for the whole card so user can zoom up all questions on Tkinter display at once instead of toggling each one.
6.11.26: Decided not to for Type II cards put multi-line question on Tkinter as with Type I single-line questions. Because since mline question allows unicode diagrams there is no point of blowing it up in size using Tkinter display which is for zooming up single-line question input by user. 
2. 
3.
4.
 

# Architecture (by file):  

## quiz.py [shuffle,
 
```
get_answer(prompt, multiline=False)  # router

Type I  -> input()           -> user_ans
Type II -> multiline_input() -> user_ans

user_ans -> normalize() -> compare with answer from JSON
```

- Card shuffle:
 - (all cards) -> quiz-range() -> auto mode(fixed). 
 - Type I -> run_quiz() -> auto shuffle on/off -> single-line qa pairs
 - Type II cards -> no shuffle(multi-line qa for coding exercises)  

 




## cards.py [data, flags

1. Cards are divided into Type I and II: 
 - Type I: single-line qa-pair fields.    
 - Type II: multi-line qa for coding exercises 
2. qa.get("display", "text").lower() -> key="display" -> read value="text" -> attach to qa as Tkinter gui popup display(gui on/off to attach/detach) 
3. "Directory" = user's topic ranges menu card.get() -> user Index or Directory in Edit Mode]














