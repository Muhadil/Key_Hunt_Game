import sys
import time
import user_class
import zombie_class
import os.path

# THIS GAME IS ABOUT REACHING A PG ROOM WITH A LEAST NUMBER OF ROOM COUNT. PLAYER NEED TO FIND A KEY OTHERWISE THEY CANT
#WIN THIS GAME. SOME ROOM HAS ZOMBIES IN THEM. IF BOTH THE PLAYER WILL END UP KILLED BY THE ZOMBIE THE GAME IS DRAWN.
#IF ONE PLAYER IS KILLED BY ZOMBIE HIS ROOM COUNT WILL BE 0 AND OTHER PLAYER JUST HAVE TO WIN THE GAME.


# Function For importing and Printing Text File Game Name/Game MAP
def text_files (file_name, format):
    f=open(file_name + '.txt', format)
    reading=f.read()
    print(reading)
    f.close

text_files ('Key','r')
print('\n')

# Function for Printing Letter in a Time Lapse Manner
def time_lapse(str):
    for characters in str:
        sys.stdout.write(characters)
        sys.stdout.flush()
        time.sleep(0.0002)

# FUNCTION FOR CREATING GAME MENU
def menu_items():
    menu_msg=('CHOOSE ONE OPTION FROM THE MENU:\n\n'
    '1-->START NEW GAME\n\n'
    '2-->LOAD GAME\n\n'
    '3-->QUIT GAME\n\n')
    time_lapse(menu_msg)
    msg=input('-->>')           
    while True:
        if msg=='1' or msg.upper()=='START NEW GAME':  
            str_msg='PERFECT CHOICE\n LETS SEE HOW YOU PERFORM\n\n'
            time_lapse(str_msg)
            time.sleep(1)
            str_msg_2='BEFORE YOU BEGIN I WANNA GIVE YOU AN ADVICE\n\nTRY TO EXPLORE ALL ROOMS.\n\n SOME ROOMS HAVE MAGIC SPELLS LIKE HEAL, FREEZE AND JUMP, PICK THEM: THEY WILL HELP YOU FIGHT AGAINST ZOMBIES\n\nLAST ADVICE\n\nUSE YOUR SPELLS CLEVERLY\n\nHAVE A SAFE JOURNEY AND SEE YOU ON THE OTHER SIDE\n\n'
            time_lapse(str_msg_2)
            time_lapse('HOLD ON A SEC\n')
            time.sleep(1)
            map_msg='DO YOU WANNA SEE YOURSELF ON THE MAP? # yes OR no\n' 
            time_lapse(map_msg)
            map_answer=input('-->>')
            if map_answer=='yes' or map_answer.upper()=='YES':
                time_lapse('TAKE A DEEP BREATH YOUR MAP IS LOADING......................\n\n')
                time.sleep(1.5)
                text_files ('Map','r')
                map_ms_1='THE ? SIGN ON THE MAP INDICATE WHERE YOU ARE RIGHT NOW\n\n'
                time_lapse(map_ms_1)
                level_0()
                break
            elif map_answer=='NO' or map_answer.lower()=='no':
                level_0() 
                break  
        elif msg=='2' or msg.upper()=='LOAD GAME':
            # time_lapse(f'{name}PLEASE TYPE YOUR USERNAME AGAIN TO LOAD YOUR SAVED PROGRESS\n\n')
            directory='D:\Data Science\Application Programming\CW2'
            # user_name_for_load=input('-->>')
            load_message='PLEASE WAIT YOUR GAME IS LOADING\n' 
            time_lapse(load_message) 

            time.sleep(2)           
            # if os.path.isfile(user_name_for_load+'.txt'):
            if (user_name+'.txt') in os.listdir(directory):
                    load_data=player_profile.load_func()
                    load_room_count=load_data[6]               
                    load_inventory=load_data[7]
                    time_lapse('{}'.format(load_data[1])+' YOU WERE AT LEVEL 1 OF THE LIBRARY\n\nYOU ROOM COUNT WAS {}'.format(load_room_count['count'])+'\nAND YOU HAVE {}'.format(load_inventory['heal']) +' HEAL SPELL, {}'.format(load_inventory['freeze'])+' FREEZE SPELL AND {}'.format(load_inventory['jump'])+' JUMP SPELL IN YOUR INVENTORY\n\n YOU ALSO HAVE {}'.format(load_data[5])+' AS YOUR WEPON TO FIGHT AGAINST ZOMBIES\n\n')
                    level_1()
            else:
                time_lapse(f'{name} YOU DID NOT PLAYED THIS GAME OR YOU DID NOT REACH TO A CHECK POINT IN A GAME. PLAY AGAIN AND REMEMBER TO SAVE YOUR PROGRESS THIS TIME\n')
                un_load_msg=f'{name} PLEASE CHOOSE ONE OPTION FROM MENU\n\n'
                time_lapse(un_load_msg)
                msg=input('-->>')
                continue
            break
        elif msg=='3' or msg.upper=='QUIT GAME':
            exit_message='YOU SAID YOU ARE BRAVE BUT ITS NOT THE CASE HERE\n'
            time_lapse(exit_message)
            sys.exit()
        else:
            error_msg='LOOKS LIKE YOU SELECTED THE WRONG OPTION \n PLEASE CHOOSE ONE OPTION FROM MENU\n'
            time_lapse(error_msg)
            msg=input('-->>')
            continue
# FUNCTION FOR CREATING PLAYER PROFILE. PLAYER CAN RELOAD THERE GAME BY TYPING THE SAME USERNAME THEY DID WHILE SAVING 
# THERE GAME.
def character_creation():
    user_name=str(input('-->> PLEASE TYPE YOUR USERNAME FOR THE GAME. YOU CAN USE THIS TO LOAD YOUR GAME::'))
    name=str(input('-->> TYPE SELECT YOUR CHARACTER NAME::'))
    age=input('-->> ENTER YOUR AGE:')
    prof=input('-->> PLEASE CHOOSE YOUR PROFESSION (student or prof)::')
    gender=input('-->> ENTER YOUR GENDER (male OR female)::')
    weapon=input('-->> CHOOSE YOUR WEAPON TO FIGHT WITH ZOMBIES (Magic stick OR Sword)::')
    time_lapse('YOU HAVE SUCCESSFULY CREATED YOUR PLAYER PROFILE FOR THIS GAME. NOW LETS BEGIN THE REAL FUN\n\n')

    return (user_name,name,age,prof,gender,weapon)
###############################################################################
#FUNCTION FOR LEVEL 0 OF THE LIBRARY IN THE GAME. EVEYRY ROOM AND LEVEL IN THE GAME IS COSTRUCTED BY FUNCTIONS.
def level_0():
    time_lapse('THIS IS YOUR STARTING POINT. \n\nYOU CAN ENTER IN THE ROOM BY REPLYING WITH ROOM NUMBER LIKE (0.1 or 0.2) AND ALSO YOU CAN CHANGE THE LEVEL BY (l1 or l2 or l3)\n\nYOU CAN ONLY SELECT WHAT IS IN FRONT OF YOU\n\nYOU HAVE THREE ROOMS INFRONT OF YOU AT LEVEL 0. YOU CAN GO ANYWHERE YOU WANT\n\n-->>R 0.1\n-->>R 0.2\n-->>R 0.3\n\n')
    levl_0_reply=input('-->>')
    if levl_0_reply=='0.1':
        room01()
    elif levl_0_reply=='0.2':
        room02()
    elif levl_0_reply=='0.3':
        room03()
    else:
        time_lapse('YOU HAVE ENTERED AN INCORRECT ROOM NUMBER. YOU ARE HERE\n')
        time.sleep(2)
        level_0()       
def room01():
    player_profile.count_fun()
    time_lapse(f'YOU HAVE NOW ENTERED IN R 0.1 OF THE LIBRARY. OOO THERE IS A HEAL AND FREEZE SPELL. THEY CAN HELP YOU FIGHT AGAINST ZOMBIES\n {name} DO YOU WANT THEM IN YOUR INVENTORY? TYPE (y) or (n)\n')
    inv_reply_01=input('-->>')
    if inv_reply_01=='y':
        players_inventory.update(heal=players_inventory['heal']+1)
        players_inventory.update(freeze=players_inventory['freeze']+1)
        time_lapse('YOU HAVE ADDED {}'.format(players_inventory['heal']) + ' HEAL SPELL AND {}' .format(players_inventory['freeze']) +' FREEZE SPELL TO YOUR INVENTORY\n')
    else:
        time_lapse(f'{name} YOU SHOULD HAVE PICK UP THOSE SPELL. YOU ARE THINKING ABOUT FIGHTING ZOMBIES WITHOUT SPELL. YOU LOOK BRAVE..LETS SEE\n\n')

    time_lapse('\nLETS EXPLORE SOME HIDDEN TREASURE IN OTHER ROOMS\nSELECT ANY OPTION FROM BELOW\n\n')
    time_lapse('-->> R 0.2\n-->> R 0.3\n-->> ENTER LEVEL 1 (TYPE l1)\n\n')
    room01_reply=input('-->>')
    if room01_reply=='0.2' or room01_reply=='02' or room01_reply=='R 0.2':
        room02()
    elif room01_reply=='0.3'or room01_reply=='03' or room01_reply=='R 0.3':
        room03()
    elif room01_reply=='l1' or room01_reply.upper()=='LEVEL 1':
        level_1()
    else:
        time_lapse('YOU HAVE ENTERED AN INCORRECT ROOM NUMBER. YOU ARE HERE\n')
        time.sleep(2)
        room01()
def room02():
    player_profile.count_fun()
    time_lapse('LOOK THERE IS JUMP SPELL HERE. IT CAN HELP YOU SKIPPING ONE LEVEL IN A GAME. IF YOU WANT THIS IN YOUR INVENTORY TYPE (y) otherwise (n)\n')
    jump_pick_reply=input('-->>')
    if jump_pick_reply=='y':
        players_inventory.update(jump=players_inventory['jump']+1)
        time_lapse('VERY NICE\n\nYOU ARE DOING VERY WELL\n\nYOU HAVE NOW ADDED {}'.format(players_inventory['jump'])+' JUMP SPELL\n\nTO YOUR INVENTORY\n\nYOU HAVE NOW GOT\n {}'.format(players_inventory['heal'])+' HEAL SPELL\n {}'.format(players_inventory['freeze'])+' FREEZE SPELL AND {}'.format(players_inventory['jump'])+' JUMP SPELL IN YOUR INVENTORY\n\n')
    elif jump_pick_reply=='n':
        time_lapse('I GAVE YOU AN ADVICE EARLIER..YOUR SPELLS CAN HELP YOU WIN THIS GAME...BUT NO WORRIES YOU CAN STILL WIN THIS GAME\n\n')
    time_lapse('KEEP SEARCHING YOU ARE ALMOST THERE TO FIND THE KEY. YOU ARE FREE TO PICK ANYONE YOU LIKE\n-->> R 0.1\n-->> R 0.3\n-->> PROCEED TO LEVEL 1 (TYPE l1)\n-->> JUMP TO LEVEL 2 USING JUMP SEPLL (TYPE l2)\n\n')
    r_02_msg=input('-->>')
    if r_02_msg=='0.1' or r_02_msg=='R 0.1':
        room01()
    elif r_02_msg=='0.3' or r_02_msg== 'R 0.3':
        room03()
    elif r_02_msg=='l1' or r_02_msg=='level 1':
        level_1()
    elif r_02_msg=='l2' and players_inventory['jump']>0:
        level_2()
    else:
        time_lapse('YOU EITHER DONT HAVE A JUMP SPELL IN YOUR INVENTORY OR YOU HAVE ENTERED AN INCORRECT ROOM NUMBER. YOU ARE HERE\n')
        time.sleep(2)
        room02()        
def room03():    
    time_lapse('YOU HAVE ENTERED R 0.3\n\n OOPS THERE IS A ZOMBIE HERE\n\nIF YOU HAVE ANY HEAL OR FREEZE SPELL USE THEM BY pressing (y) or FIGHT THE ZOMBIE WITH YOUR WEAPON type (n)\n\n')
    roo_03_spell_reply=input('-->>')
    if roo_03_spell_reply=='y' and players_inventory['heal']>0 and players_inventory['freeze']>0:
        player_profile.count_fun()
        time_lapse('NICE WORK BY FREEZING THE ZOMBIES....BUT THAT WILL BE BACK SOON\n\n')
        time.sleep(3)
        time_lapse(f'THEY ARE BACK NOW.....\n\nTAKE OUT YOUR {weapon}\n\nZOMBIE HIT YOU FIRST.....NICE YOU HAVE DONE DAMAGE TO ZOMBIE WITH YOUR {weapon}\n\n')
        zom_room_obj.z_1_attack()
        time_lapse(f'{name} YOU HAVE NOW THESE OPTION TO CHOOSE FROM BUT BEWARE OF ZOMBIES. THEY WILL BE HAUNTING YOU KNOW AS YOU MURDERED ONE OF THEM.... \n\n-->>R 0.1\n-->>R 0.2\n-->>Level 1 (l1)\n\n')
        zom_kil_reply=input('-->>')
        if zom_kil_reply=='R 0.1' or zom_kil_reply=='0.1':
            room01()
        elif zom_kil_reply=='R 0.2' or zom_kil_reply=='0.2':
            room02()
        elif zom_kil_reply.upper()=='LEVEL 1' or zom_kil_reply.lower()=='l1':
            level_1()
    else:
        player_profile.count_zero()
        time_lapse(f'YOU DONT HAVE ANY SPELLS IN YOUR INVENTORY\n\n{name} GRAB YOUR {weapon}\n\n')
        zom_room_obj.z_2_attack()
    return i
def level_1():
    time_lapse(f'THIS IS LEVEL 1 OF THE LIBRARY {name}\n\nPLAYERS USUALLY GET KILLED BY ZOMBIES HERE \nDO YOU HAVE COURAGE TO SEARCH ROOMS AT THIS LEVEL\n\n IF YOU THINK YOU ARE BRAVE SEARCH THE ROOMS HERE AND FIND KEY OR IF YOU WANT TO PLAY SMART JUMP ONTO THE NEXT LEVEL USING YOUR JUMP SPELL\n\nYOU HAVE THREE OPTIONS ON THIS LEVEL CHOICE IS YOURS\n-->>R 1.1\n-->>R 1.2\n-->>ENTER LEVEL 3 (Type l3)\n\n')
    l_1_reply=input('-->>')
    if l_1_reply=='1.1' or l_1_reply=='11':
        room_11()
    elif l_1_reply=='1.2' or l_1_reply=='12':
        room_12()
    elif l_1_reply=='l3' and players_inventory['jump']>0:
        level_3() 
    else:
        time_lapse('YOU EITHER DONT HAVE JUMP SPELL IN YOUR INVENTORY OR YOU HAVE TYPED A WRONG ROOM NUMBER.\n NOW FACE THE CONSEQUENCE\n YOU HAVE BEEN RETURNED BACK TO LEVEL 0\n')
        level_0()
def room_11():
    player_profile.count_fun()
    time_lapse('YOU ARE NOW AT ROOM 1.1\n\nLOOK ITS A SAVE CHECKPOINT IN THE GAME\nDO YOU WANY TO SAVE YOUR PROGRESS. IF YES REPLY (y) else (n)\n\n')
    save_response=input('-->>')
    if save_response=='y' or save_response.upper()=='YES':
        player_profile.save_func(players_inventory)
    else:
        time_lapse(f'{name.upper()} YOU SHOULD HAVE SAVE YOUR PROGREES..DONT WORRY YOU ARE STILL IN THE GAME\n\n CARRY ON WITH YOUR HUNT\n\n ')
    time_lapse(f'HEY {name.upper()} ITS AN EMPTY ROOM. YOU SHOULD HAVE WENT SOMEWHERE ELSE. THERE IS NOTHING HERE.\n\nEXPLORE ANOTHER ROOM OR SEARCHJED ANOTHER LEVLE FOR A KEY\n-->>R 1.2\n-->>ENTER LEVEL 2 (TYPE l2)\n\n')
    l1_reply=input('-->>')
    if l1_reply=='1.2':
        room_12()
    elif l1_reply=='l2':
        level_2()
    else:
        time_lapse('YOU HAVE ENTERED AN INCORRECT ROOM NUMBER. YOU ARE HERE\n')
        time.sleep(2)
        room_11()
def room_12():
    player_profile.count_fun()
    players_inventory.update(key=True)
    time_lapse('YOU HAVE NOW ENTERD LEVEL 2\n\n LOOK\n\nTHERE IS A KEY HERE\n\nDO YOU WANT TO PICK THE KEY FOR PG ROOM (type yes or no)\n\n')
    key_replyy=input('-->>')
    if key_replyy=='y' or key_replyy.lower()=='yes':
        players_inventory.update(key=True)
        time_lapse('YOU HAVE PICKED THE KEY NOW YOU ONLY HAVE TO FIND PG ROOM\nGO AHEAD YOU ALMOST MADE IT\n\n')
    else:
        time_lapse('WHY DID NOT YOU PICK THE KEY...HOW TOU ARE GOING TO WIN THIS GAME NOW\n\nTHERE IS STILL ONE WAY TO WIN THIS GAME BUT YOU HAVE TO SORT THIS OUT YOURSELF..I CAN GIVE YOU ONE HINT (WONDER AROUND)')
    time_lapse('CHOOSE ONE YOU LIKE MOST\n-->>1.1\n-->>ENTER LEVEL 2 (TYPE l2)\n')
    room_12_rep=input('-->>')
    if room_12_rep=='1.1':
        room_11()
    elif room_12_rep=='l2' or room_12_rep.upper()=='LEVEL 2':
        level_2()
    else:
        time_lapse('YOU HAVE ENTERED AN INCORRECT ROOM NUMBER. YOU ARE HERE\n')
        time.sleep(2)
        room_12()

def level_2():
    time_lapse(f'YOU HAVE REACHED TO LEVEL 2\n{name.upper()} IF YOU WANNA SEE YOURSELF ON THE MAP PRESS (y) otherwise type (n)\n')
    map_answerl2=input('-->>')
    if map_answerl2=='y':
        time_lapse('TAKE A DEEP BREATH YOUR MAP IS LOADING......................\n')
        time.sleep(1.5)
        text_files ('level_2','r')
    elif map_answerl2=='n':
        time_lapse('YOU ARE NOW STANDING AT LEVEL 2 OF THE LIBRARY\n')
    time_lapse('THERE IS ONLY TWO ROOMS HERE.\nMAY BE YOU WILL FIND PG ROOM HERE. LETS SEE\n-->>R 2.1\n-->>R 2.2\n-->>ENTER LEVEL 3 (TYPE l3)\n')
    level_2_reply=input('-->>')
    if level_2_reply=='2.1':
        room21()
    elif level_2_reply=='2.2':
        room22()
    elif level_2_reply=='l3' or level_2_reply.upper()=='LEVEL 3':
        level_3()
    else:
        time_lapse('YOU EITHER DONT HAVE JUMP SPELL IN YOUR INVENTORY OR YOU HAVE TYPED A WRONG ROOM NUMBER.\n NOW FACE THE CONSEQUENCE\n YOU HAVE BEEN RETURNED BACK TO LEVEL 2\n')
        level_2()
def room21():
    player_profile.count_fun()
    time_lapse('THERE ARE ZOMBIES EVERY WHERE\nZOMBIES ATTACKED YOU\nREMEMBER MY ADVICE ABOUT SPELLS\nIF YOU WANT TO SURVIVE::TAKE OUT YOUR FREEZE AND HEAL SPELLS..REPLY (y or n) IF YOU WANNA USE YOUR SPELLS\n\n')
    spell_reply=input('-->>')
    if spell_reply=='y' and players_inventory['freeze']>0 and players_inventory['heal']>0:
        players_inventory.update(freeze=players_inventory['freeze']-1)
        players_inventory.update(heal=players_inventory['heal']-1)
        time_lapse(f'{name} YOU HAVE FREEZED THE ZOMBIES\n,FREEZE EFFECT IS GONE--THEY ARE BACK KNOW\nTAKE OUT YOUR {weapon}\n\nZOMBIE HIT YOU FIRST.....NICE YOU HAVE DONE DAMAGE TO ZOMBIE WITH YOUR {weapon}\n\n')
        zom_room_obj.z_1_attack()
        time_lapse('YOU HAVE USED YOUR HEAL SPELL\n\n !!!NICE WORK!!!!\n\nYOU HAVE ONE MORE ROOMS LEFT TO EXPLORE\n\nBUT THERE CAN BE ZOMBIES THERE AS WELL\n\n-->>R 2.2\n-->>ENTER LEVEL 3 (l3)\n\n')
        room21_reply=input('-->>')
        if room21_reply=='2.2':
            room22()
        elif room21_reply=='l3' or room21_reply.upper()=='LEVEL 3':
            level_3()
    elif spell_reply=='n' or players_inventory['freeze']==0 or players_inventory['heal']==0:
        player_profile.count_zero()
        time_lapse(f'{name} YOU DONT HAVE ANY SPELLS IN YOUR INVENTORY. TAKE OUT YOUR {weapon}. \n\nYOU CAN KILL THIS ZOMBIE.\n\n{name} YOU ARE STILL FIGHTING WITH ZOMBIES. ZOMBIES ARE COMING CLOSE\n\n')
        zom_room_obj.z_2_attack()
    else:
        time_lapse('YOU EITHER DONT HAVE SPELLS IN YOUR INVENTORY OR YOU HAVE ENTERED AN INCORRECT NUMBER.\n\n YOU ARE STANDING AT ROOM 2.1 AND SURROUNDED BY ZOMBIES\n\n')
        room21()
def room22():
    player_profile.count_fun()
    time_lapse('WRONG ROOM AGAIN. YOU SHOULD HAVE WENT TO NEXT LEVEL\n ZOMBIES ARE ATTACKING YOU AGAIN\nIF YOU HAVE ANY HEAL OR FREEZE SPELL USE THEM BY pressing (y) other wise type (n)\n\n')
    roo_22_spell_reply=input('-->>')
    if roo_22_spell_reply=='y' and players_inventory['heal']>0 and players_inventory['freeze']>0:
        time_lapse('NICE WORK BY FREEZING THE ZOMBIES....BUT THAT WILL BE BACK SOON\n')
        time.sleep(3)
        time_lapse(f'THEY ARE BACK NOW.....\n\nTAKE OUT YOUR {weapon}\n\nZOMBIE HIT YOU FIRST.....NICE YOU HAVE DONE DAMAGE TO ZOMBIE WITH YOUR {weapon}\n\n')
        zom_room_obj.z_2_attack()
    else:
        player_profile.count_zero()
        time_lapse(f'YOU DONT HAVE ANY SPELLS IN YOUR INVENTORY\n\nBUT YOU CAN STILL KILL THE ZOMBIE WITH YOUR {weapon}``TAKE OUT YOUR {weapon}\n\nYOU ATTACKED THE ZOMBIE\n\n ')
        zom_room_obj.z_2_attack()
    return i
def level_3():

    time_lapse('YOU HAVE NOW ENTERED LEVEL 3 OF THE LIBRARY\n THERE IS ONLY ONE ROOM HERE\n GO ON CHECK THIS ROOM\nITS MAY BE ONE YOU WERE LOOKING FOR\n-->>R 3.1\n')
    level_3_reply=input('-->>')
    if level_3_reply=='3.1' and players_inventory['key']==True:
        room_31()
    else:
        time_lapse(f'ITS A PG ROOM. THE ONE YOU WERE LOOKING FOR\n\n   WHERE IS THE KEY?     \n\n {name} YOU DONT HAVE A KEY\n\nYOU HAVE TO FIND KEY TO UNLOCK THIS ROOM\n WHERE DO THINK KEY WILL BE..CHOOSE\n\n')
        time_lapse('-->> BACK TO LEVEL 0 (STARTING POINT) type (l0)\n\n-->> BACK TO LEVEL 1 (l1)\n\n-->>BACK TO LEVEL 2 (l2)\n\n')
        key_not_reply=input('-->>')
        if key_not_reply=='l1' or key_not_reply.upper()=='LEVEL 1':
            level_1()
        elif key_not_reply=='l2' or key_not_reply.upper()=='LEVEL 2':
            level_2()
        elif key_not_reply=='l0' or key_not_reply.upper()=='LEVEL 0':
            level_0()
        else:
            time_lapse(f'{name} YOU HAVE ENTERETD AN INCORRECT LEVEL NO\n\n YOU ARE GOING BACK TO STARTING POINT TO FIND KEY\n\n')
            level_0()
def room_31():
    player_profile.count_fun()
    time_lapse('ITS A ONE YOU WERE LOOKING FOR\n\n   CHEERS!     \n\nYOUR COUNT OF ROOMS TO REACH PG HAS BEEN SAVED\n\nLETS SEE WHO WIN')
# ################################################

#PYTHON DICTIONARY FOR STORING PLAYER SPELLS AND KEY STATUS
players_inventory={'heal':0,
                    'freeze':0,
                    'jump':0,
                    'key':False}
story='1970:\n\n      DAY BEFOR EXAM \nYOU ARE COMING BACK FROM PARTY AND REALIZES THAT YOU HAVE AN EXAM AND YOU HAVE NO WHERE TO GO OTHER THAN LIBRARY TO PREPARE YOURSELF FOR TOMORROW EXAM.\nIT IS RAINING HEAVILY.\nSOMEONE APPROACHED YOU AND SAID:\nARE YOU SERIOUS TO ENTER THE LIBRARY THIS TIME. \nPEOPLE DO NOT USUALLY COME BACK ONCE THEY ENTERED AS SOME ROOMS HAS ZOMBIES IN THEM \nYOU ARE SCARED BUT WANT TO ENTER PG ROOM\nBUT YOU DO NOT HAVE A KEY. NOW YOU NEED TO CHECK DIFFERNT ROOM TO FIND KEY.\nARE YOU BRAVE ENOUGH TO FIND A KEY AND REACH PG ROOM FIRST AS THERE IS ONLY ONE AVAILABLE SPACE IN THE ROOM. THERE IS ANOTHER STUDENT WAITING TO ENTER THE ROOM. IF YOU ENTER THE ROOM WITH LEAST NUMBER OF ROOM COUNT WHILE SEARCHING THE KEY YOU WILL WIN THIS GAME\n\nLETS HUNT THE KEY\n\n'
#A LIST STORING THE PLAYER TOTAL NUMBER OF ROOM COUNT AFTER HE OR SHES HAS WON THE GAME OR KILLED BY ZOMBIE.
room_scores=[]

game_message=('WOULD YOU LIKE TO PLAY A GAME? ::KEY HUNT:: # yes OR no\n')
time_lapse(game_message)
message=input('-->>')
if message =='yes':
    brave_msg=('LET ME TELL YOU STORY\n')
    time_lapse(brave_msg)
    time_lapse(story.upper())
elif message=='no':
    mesg=f'YOU SHOULD HAVE TRY THIS GAME. BUT NO WORRIES SEE YOU NEXT TIME\n\n  '
    time_lapse(mesg)
    time.sleep(2)
    sys.exit()

####################################loop creation######################
# A LIST FOR STORING PLAYER NAME. SO THAT IT CAN BE USED AT THE END TO MENTIONED WHICH PLAYER HAS WON THE GAME
players_name=[]
# THE FOOR LOOP IS USED HERE TO RUN THE GAME. IT RANGES FROM 0 TO 2 BUT IF THERE ARE MORE THAN 2 PLAYER WHO WANT
# THE GAME THEN I SIMPLY HAVE TO CHANGE THE RANGE VALUE.
  
for i in range (0,2):
    time_lapse('FIRST CREATE YOUR PLAYER PROFILE FOR THE KEY HUNT GAME:\n\n')
    user_name,name,age,prof,gender,weapon=character_creation()
    #BELOW I AM CREATING AN OBJECT FOR PLAYER FROM USER_DETAILS CLASS
    player_profile=user_class.user_details(user_name,name,age,prof,gender,weapon)
    players_name.append(name)
    #BELOW I AM CREATING A ZOMBIE OBJECT FROM THE CLASS. BECAUSE ZOMBIES ALSO HAVE A PHYSICAL EXISTENCE IN THE GAME
    #THAT IS WHY I MADE A ZOMBIE CLASS IN THIS GAME
    zom_room_obj=zombie_class.zombies_info_and_players_health()
    menu_items()
    room_scores.append(player_profile.room_count['count'])
    # print(room_scores[0])
    time_lapse(f'\n\n{name} YOUR SCORE HAS BEEN SAVED\n\n ITS THE NEXT PLAYER TURN NOW\n\n')
    #UPDATING A ROOM COUNT BACK TO 0 FOR THE NEXT PLAYER
    player_profile.room_count.update(count=0) 
    #UPDATING A DICTIONARY BACK TO THE INITIAL VALUE AFTER ONE PLAYER HAS FINISHED THE GAME
    players_inventory.update(heal=0,
                    freeze=0,
                    jump=0,
                    key=False)
time.sleep(3)
###BELOW IS AN IF AND ELSE CONDITION TO DECIDE WHICH PLAYER HAS WON THE GAME
if room_scores[0]==room_scores[1]:
    time_lapse(f'{players_name[0]} AND {players_name[1]} YOU BOTH HAVE EXACTLY SAME NUMBER OF ROOM COUNTS..SO\n\n GAME IS DRAWN\n\n')
elif room_scores[0]==0 and room_scores[1]>0 :
    time_lapse(f'{players_name[1]} HAS WON THIS GAME BECAUSE {players_name[0]} HAS BEEN KILLED BY THE ZOMBIE')
elif room_scores[1]==0 and room_scores[0]>0:
    time_lapse(f'{players_name[0]} HAS WON THIS GAME BECAUSE {players_name[1]} HAS BEEN KILLED BY ZOMBIE')
elif room_scores[0]<room_scores[1]:
    time_lapse(f'{players_name[0]} YOU HAVE WON THE GAME\n\n')
elif room_scores[0]>room_scores[1]:
    time_lapse(f'{players_name[1]} HAS WON THE GAME\n\n')
# elif room_scores[0]==room_scores[1]:
#     time_lapse('YOU BOTH HAVE ENDED UP IN A ZOMBIE ROOM SO, GAME IS DRAWN')

sys.exit(0)


# HAVE TO CHANGE COUNT IN ZOMBIES ROOM