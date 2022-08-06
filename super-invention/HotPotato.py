"""In this problem, we want to simulate the game Hot Potato (https://en.wikipedia.org/wiki/Hot_potato). Essentially, we have a list of people that pass the potato to the next person at each turn.

After a certain number of passes (x), the person holding the potato is kicked out of the group. We want to return the final winner of the game (eg: survives all rounds of elimination).

For example, if we have a list ["James", "Jason", "Naoko"], and a number of passes (2), we would pass two times each round.

The first round, we might start with James -> Naoko -> Jason (eliminating Jason first). Then, we would do James -> Naoko -> James (eliminating James second). Then, we only have one contestant left (Naoko), who we return as our result.

You can assume passes will be equal to or greater than 1."""
import collections


c = ["James", 
 "Jason", 
 "Naoko", 
 "Lenny", 
 "Kent", 
 "Linda"]
p = 8 
#kent
#####################################################################
#actually using a queue to simulate passing 
def solution(contestants, passes):
    d = collections.deque(contestants)
    startIndex = 0
    print(len(d))
    while len(d) > 1:
        personWithPotato = passes % len(d) 
        #startIndex %= len(d)
        for i in range(personWithPotato):#number of passes
            leaving = d.popleft()
            
            d.append(leaving)
            
        d.popleft()
                
        #startIndex += 1
    return d[0]
    
print(solution(c,p))


####################################################################
#index solution


c1 = ["James","Naoko"]
p1 = 2

def solution(contestants, passes):
    startIndex = 0
    while len(contestants) > 1: #loop until only one person remains
        startIndex += passes
        qIndex = (startIndex) % len(contestants)
        contestants.pop(qIndex)
        print(contestants)
        
    
    return contestants[0]
        
        
print(solution(c1,p1))
            
    