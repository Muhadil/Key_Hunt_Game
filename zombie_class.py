import time
import sys
def time_lapse(str):
    for characters in str:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.0002)
class zombies_info_and_players_health:
    plyrs_health=100
    plyrs_damage_power=20
    def __init__(self):
        self.zombie_1_name='MEAT FACE'
        self.zombie_1_health=60
        self.zombie_1_dp=10
        self.zombie_2_name='SLAUGHTER'
        self.zombie_2_health=100
        self.zombie_2_dp=20
    def z_1_attack(self):
        self.player_health=(self.plyrs_health-self.zombie_1_dp)
        self.zombie_1_health=(self.zombie_1_health-self.plyrs_damage_power)
        #time_lapse(f'{self.zombie_1_name} ZOMBIE ATTACKED YOU FOR {self.zombie_1_dp} DAMAGE,\n\n YOUR HEALTH IS NOW {self.player_health}, YOU ATTACKED THE ZOMBIE, {self.zombie_1_name} RECIEVES {self.plyrs_damage_power} DAMAGE\n\n KEEP FIGHTING, YOU HAVE DONE A LOT OF DAMAGE TO ZOMBIE.\n\n YOU HAVE KILLED THE {self.zombie_1_name}\n\n')
        return self.player_health
    
    def z_2_attack(self):
        self.player_health=(self.plyrs_health-self.zombie_2_dp)
        self.zombie_2_health=(self.zombie_2_health-self.plyrs_damage_power)
        time_lapse(f'{self.zombie_2_name} ZOMBIE ATTACKED YOU FOR {self.zombie_2_dp} DAMAGE, YOUR HEALTH IS NOW {self.player_health}, YOU ATTACKED THE ZOMBIE, {self.zombie_2_name} RECIEVES {self.plyrs_damage_power} DAMAGE\n\n KEEP FIGHTING, YOU HAVE DONE A LOT OF DAMAGE TO ZOMBIE, {self.zombie_1_name} HAVE NOW COME OUT OF NO WHERE.\n\n YOU HAVE BEEN KILLED BY ZOMBIES.\n\n ')

        





    