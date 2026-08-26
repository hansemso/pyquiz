# pyquiz\ARCHITECTURE.md  |  today's date: 8.15.26


# Synopsis: 
- This file is just for the architecture, the blueprint of pyquiz as it grows. So it should be kept as like a blueprint. Everything else goes in devlog.md
- 
- quiz.py and cards.py are the core files. main.py is like a simple breaker box.  
-  



 

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














