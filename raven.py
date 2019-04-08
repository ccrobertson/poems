#Save this code to your desktop. 
#Open a terminal
#Navigate to the directory where it is saved
#Type `python raven.py` to watch the parody unfold 

import time
import random

PoeLines = [ "Lenore?", 
            "Ghastly grim and ancient Raven tell me what thy lordly name is on the Nights Plutonian shore",
            "Tis some visitor tapping on my chamber door. Only this and nothing more.",
            "The silken, sad, uncertain rustling of each purple curain thrilled me",
            "Filled me with fantastic terrors never felt before",
            "Some late visitor entreating entrance at my chamber door. This it is and nothing more.",
            "I was napping, and so gently you came rapping",
            "All my soul within me burning",
            "Tis the wind and nothing more",
            "For we cannot help agreeing that no living human being ever yet was blessed with seeing bird or beast with such a name as Nevermore",
            "Doubtless what it utters is its only stock and store", 
            "God hath lent thee - he hath sent respite and nepenth from thy memories of Lenore!",
            "Prophet!",
            "Is there balm in Gilead?",
            "Tell this soul with sorrow laden if it shall clasp a sainted maiden",
            "Be that word our sign of parting, bird of fiend!", 
            "Leave my loneliness unbroken!"]


def QuoththeRaven(x, n):
    xlist = x.split()
    if "dreary" in xlist:
        response="Nevermore! "*random.sample(range(1,n+1),1)[0]
    elif len(xlist)>10:
        if 'soul' in xlist:
            response="Nevermore! "*random.sample(range(1,n+1),1)[0]
        elif 'thrilled':
            response="Nevermore! "*random.sample(range(1,n+1),1)[0]
    elif ("God" in xlist) and (len(xlist)>5):
        if 'bird' or 'fiend':
            response="Nevermore! "*random.sample(range(1,n+1),1)[0]
        else:
            response="Nevermore! "*random.sample(range(1,n+1),1)[0]
    else:
        response="Nevermore! "*random.sample(range(1,n+1),1)[0]
    return response

  
print("The Python and the Raven")
time.sleep(1.5)
print(" ")
print("by Cassie Robertson")
print(" ")
time.sleep(4)
    
n=0
while n < 25:
    n = n + 1
    question=random.sample(PoeLines, 1)[0]    
    print("Poe: " + question)
    time.sleep(5/float(n))
    print("Raven: " + QuoththeRaven(question, n))
    time.sleep(5/float(n))
    print(" ")

print("NEVERMORE!")
