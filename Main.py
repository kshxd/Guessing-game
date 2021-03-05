from questions import questions

question_prompts = [
    "what is the capital of nigeria? \n(a) Abuja \n(b) Copenhagen \n(c) Nur-Sultan \n answer :   ",
    "what is the best programing language for games? \n(a) python \n(b) c++ \n(c) Java \n answer :  " ,
    "which one isnt korean ? \n(a) Samsung \n(b) Xiaomi \n(c) hyundai \n answer :  "
]

questions = [
     questions(question_prompts[0] , "a") ,
     questions(question_prompts[1] , "b") , 
     questions(question_prompts[2] , "b") 
] 

def runtest(answers) :
     score = 0
     for questions in answers  :
         x = input(questions.prompt) 
         if x == questions.answer:  
          score += 1

     print("you got   " + str(score) + "/" + "3" + "    right" )



runtest(questions) 
