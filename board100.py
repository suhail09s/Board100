import random 
import time
trap=[] #initing a list of traps.
hor=[]
ver=[]

def traps(location): # a function to setup traps randomly and check if player have stepped on one :D
    # this part simply select a number of squares as traps.    
    while len(trap)<numberOfTraps: # defining the number of traps, will loop till it reaches the selected number.
        for i in range(0,1): # in range of one, simply to add only one position every time.
            firstTrap=7 # identify the location of the first trap. watch out if the size of the board is too small, will cause an error.
            lastTrap=(sizeOfBoard**2)-2 # identify the location of the last trap.
            t=random.randint(firstTrap,lastTrap) # randomly selecting squares as traps between two numbers. It has to be between 2 and (sizeOfBoard^2)-1 , to avoid placing a trap at the first or final square.
            if (trap.count(t))==0: # to avoid placing two traps on the same square. it will check if the square is not marked as a trap already.
                trap.append(t)      # appending the locations of the traps one by one.
            else:
                break # when the while loop reaches the selected number of traps, will break out of the loop.
        
    
    # this part will check if the player have stepped on a trap, every time the player moves.
    istrap=trap.count(location) # This will check if the player has stepped on a square marked as a trap, check loc
    if istrap==1: # if (istrap) found the current location of the player marked as a trap (exists in the trap list).
        return True # it will return True , which means the player have stepped on a trap.



def ra(): # A simple randomizer function, to move player vertically or horizontally.
    if hor[hor_p]==len(hor)-1: # if reahched the horizontal edge, will move vertically.
      return 2
    if ver[ver_p]==len(ver)-1: # if reahched the vertical edge, will move horizontally.
      return 1
    turn=random.randint(1,2) # 1 = Horizontal move/step , 2 = Vertical move/step.
    return turn



numberOfTraps=1 # Identify the number of traps, watch out if the number of traps is almost equals the number of squares,will be stuck in an infinite loop.
sizeOfBoard=10 # sizeOfBoard=5 means 5x5 board .
for x in range (0,sizeOfBoard+1): # simple loop to build up the horizontal and vertical squares.
    hor.append(x)
    ver.append(x)


hor_p=1 # intial horizontal location.
ver_p=1 # intial vertical location.
location=ver_p*hor_p # inital location of the player.
t=0 # the number of turns.
print('Player started on square ({},{}) {}/{}'.format(hor[hor_p],ver[ver_p],location,sizeOfBoard**2)) # printing the intial location and how far away from the last square.
#trap=[3,8,11,66,9,44]  # you can uncomment this line to identify a specific trap locations, the script will add more traps if the number of traps you have listed < number of traps required
traps(location) # randomly placing traps on the board.
print('Good luck, there are {} traps:{}'.format(str(numberOfTraps),trap))



while not location==sizeOfBoard**2: # will move the player until it reaches the last square.
    t+=1 # counter for the turns
    turn=ra() # with every turn a function is called to get a return value of 1(move horizontally) or 2(move vertically).
    
    if turn==1 and hor_p<len(hor)+1: # move horizontally only if the player haven't reached the horizontal edge.
        hor_p=hor_p+1
    if turn==2 and ver_p<len(ver)+1: # move vertically only if the player haven't reached the vertical edge.
        ver_p=ver_p+1
   
    location=(hor[hor_p])+(sizeOfBoard*(ver[ver_p]))-sizeOfBoard # canculate the position of the player on the board
    print('player on square ({},{}) {}/{} after {} turns'.format(hor[hor_p],ver[ver_p],location,sizeOfBoard**2,t)) 
    time.sleep(0.1) # it will simply sleep for a short period of time (optional), gives smoother prints. You can delete this line to make prints instant.
    istrap=traps(location)
    if istrap==True: # if the current location equals a trap location, player will lose and game will end. 
        print("you lost !!!Muahahaaa\n you have stepped on a trap at ({},{})".format(hor[hor_p],ver[ver_p]))
        break # this will break of the loop and will terminate the game.
    if location==sizeOfBoard**2: # checks if the player has reached the final square and won the game.
        print("you won!!!")
        break
