import time
import sys
import pickle

#Just a Function for Printing Letter in a Time Lapse Manner
def time_lapse(str):
    for characters in str:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.0002)

# User class storing user data, saving it and then loading it again also has
# an exit method if user want to eixt the game.
class user_details:
    room_count={'count':0}
    def __init__(self,user_name,name,age,profession,gender,weapon):
        self.player_id=user_name
        self.player_name=name
        self.age=age
        self.prof=profession
        self.gender=gender
        self.player_weapon=weapon
    # SAVE METHOD TO SAVE PLAYER PROGRESS
    def save_func(self,inventory_list):
        user_inventory=inventory_list
        sav_var=open(self.player_id +'.txt','wb')
        pickle.dump([self.player_id,self.player_name,self.age,self.prof,self.gender,self.player_weapon,self.room_count,user_inventory],sav_var)
        sav_var.close()
        sav_msg='YOUR PROGRESS HAS BEEN SAVED\n'
        time_lapse(sav_msg)
    # LOAD METHOD TO LOAD PLAYER PROGRESS
    def load_func(self):
        load_var= open(self.player_id +'.txt','rb')
        load_progress=pickle.load(load_var)
        return load_progress
    # COUNT METHOD TO INCREMENT ROOM NUMBER COUNT WHEN PLAYER SEARCHED DIFFERNT ROOMS
    def count_fun(self):
        self.room_count.update(count=self.room_count['count']+1)
        

    #### FOR PLAYERS WHO ARE GOING TO DIE BY ENTERING ZOMBIE ROOM.. I HAVE CHANGED THERE ROOM COUNT HERE TO 0    
    def count_zero(self):
        self.room_count.update(count=0)

    ### EXIT METHOD TO EXIT THE GAME
    def exit_func(self):
        ext_msg='YOU ARE ABOUT TO EXIT THE GAME. DO YOU WANT TO SAVE YOUR PROGRESS? # yes OR no'
        time_lapse(ext_msg)
        ext_prompt=input('-->>')
        if ext_prompt=='yes':
            self.save_func()
        elif ext_prompt=='no':
            sys.exit(0)


