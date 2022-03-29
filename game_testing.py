import unittest
from user_class import user_details
from zombie_class import zombies_info_and_players_health
# from Game import character_creation


class test_user_cred(unittest.TestCase):
    # def setup():
    #     self.player=user_details()
    # TO TEST THE ROOM COUNT FUNCTION OF THE GAME WETHER THIS COUNT HAD ANY INCREMENT IN THAT OR NOT
    def test_profile(self):
        player_1=user_details('adil_003','Mo',22,'student','male','magic_stick')
        player_2=user_details('ronaldo_07','GOT',25,'prof','male','sword')
        self.assertEqual(player_1.room_count['count'],0)
        self.assertEqual(player_2.room_count['count'],0)
        player_1.room_count.update(count=3)
        self.assertEqual(player_1.room_count['count'],3)
    
    # TO TEST THE WETHER ZOMBIE AND PLAYER LOSSE THERE HP IN A BATTLE
    def test_zombie_func(self):
        zombie_obj=zombies_info_and_players_health()
        self.zombie_1_name='MEAT FACE'
        self.zombie_1_health=60
        self.zombie_1_dp=10
        self.plyrs_health=100
        self.plyrs_damage_power=20
        self.player_health=(self.plyrs_health-self.zombie_1_dp)
        self.assertEqual(zombie_obj.z_1_attack(),self.player_health)
    # TO TEST WETHER LOAD FUNCTION IS WORKING FINE IN THE GAME
    def test_load(self):
        player_1=user_details('adil_007','ADIL','22','student','male','sword')
        room_count={'count':2}
        players_inventory={'heal':0,
                    'freeze':0,
                    'jump':0,
                    'key':False}
        # print(player_1.load_func())
        self.assertEqual(player_1.load_func(),['adil_007','ADIL','22','student','male','sword',room_count,players_inventory])
        
    

