
from collections import deque
import random
import arcade
from collections import deque

#from network import Network
import numpy as np
class TextButton:
    """ Text-based button """

    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center",bold=True)

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False
    def set_center(self,x,y):
        self.center_y = y
        self.center_x = x
class StartTextButton(TextButton):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, 100, 40, "Start", 18, "Arial")

    def on_release(self):
        super().on_release()
        print("RILASCIATO START")
        self.pressed=False

class VaiTextButton(TextButton):
    def __init__(self, center_x, center_y):
        super().__init__(center_x, center_y, 100, 40, "Vai!", 18, "Arial")
    def on_press(self):
        super().on_press()
        print("PRESSATO VAI")
    def on_release(self):
        super().on_release()
        print("RILASCIATO VAI")
        self.pressed=False

pixel_w=50 ## lunghezza base carta
rapp_xony=497/821 ## rapporto tra base ed altezza carta
pixel_h=pixel_w/rapp_xony
dist_card=4
pos_card=[1/4,3/4]
val_glob={1:"ace",
           2:"two",
           3:"three",
           4:"four",
           5:"five",
           6: "six",
           7:"seven",
           8:"jack",
           9:"horse",
           10:"king"}
suit_glob={"Denari":"g",
          "Coppe":"c",
          "Bastoni":"b",
          "Spade":"s"}
back=arcade.Sprite("sprite/briscola-cards/n_back.png")
back._set_scale(pixel_w/back._get_width())
class Card:
    """ Text-based button """

    def __init__(self,suit,value):
        self.value = value
        self.suit = suit
        self.pressed = False
        self.center_x = None
        self.center_y = None
        self.width = pixel_w
        self.height = pixel_w/rapp_xony
        self.index = None
        self.text= "card"
        self.card_image = arcade.Sprite("sprite/briscola-cards/n_"+val_glob[self.value]+"_"+suit_glob[self.suit]+".png")
        self.card_image._set_scale(pixel_w/self.card_image._get_width())

    def set_index(self,index):
        self.index=index
    def on_press(self):
        self.pressed = True
        print("pressato")
    def on_release(self):
        self.pressed = False
        print("rilasciato")
        return self.index
        #arcade.draw_text("BRAVO",300,300)
    def set_center(self,x,y):
        self.center_y = y
        self.center_x = x
        print(self, " ha centro in (",self.center_x,",",self.center_y,")")


    def __repr__(self):
        return '<{} {}>'.format(self.value, self.suit)

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points= 0

    def give_card(self, card):
        self.cards.append(card)

    def return_cards(self):
        self.cards = []

    def __repr__(self):
        return 'Player: {} - [{}]'.format(self.name, ','.join([str(x) for x in self.cards]))
    def LengthCard(self):
        return len(self.cards)
    def play_card(self,ind,w,h):
        self.cards[ind].set_center(w/2,h/2)
        self.cards.pop(ind)
    def count_points(self,played_card):
        points_gen=[11,0,10,0,0,0,0,2,3,4]
        for i in range(len(played_card)):
            self.points += points_gen[played_card[i].value-1]

########### DISEGNA RETRO CARTA, INDIPENDENTE DA CARDBUTTON ######
def draw_back_card(center_x,center_y):
        #arcade.draw_rectangle_filled(center_x , center_y, 50, 70, arcade.color.WHITE)
        #arcade.draw_rectangle_filled(center_x, center_y, 40, 60, arcade.color.BLUE_VIOLET)
        #arcade.draw_rectangle_outline(center_x, center_y, 40, 60, arcade.color.BLACK)
        back.set_position(center_x,center_y)
        back.draw()
######## DISEGNA FRONTE CARTA, DIPENDENTE DA CARDBUTTON###
def draw_front_card(card,center_x,center_y):
        #arcade.draw_rectangle_filled(card.center_x, card.center_y, 50, 70, arcade.color.WHITE)
        #arcade.draw_rectangle_outline(card.center_x, card.center_y, 40, 60, arcade.color.BLACK)
        #arcade.draw_text(str(card.value), card.center_x-3, card.center_y+60/4-5, arcade.color.BLACK, 10, font_name='GARA')
        #arcade.draw_text(str(card.suit), card.center_x-20+3, card.center_y-40/4, arcade.color.BLACK, 10, font_name='GARA')
        card.set_center(center_x,center_y)
        card.card_image.set_position(center_x,center_y)
        card.card_image.draw()

####### CONTROLLA QUALE CARTA è SELEZIONATA #########
def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()

def check_mouse_release_for_buttons(_x, _y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()
            if button.text=="card":
                return button.index
            else:
                if button.text =="Start":
                    return 1
                else:
                    print("SONO QUA")
                    return 0

def draw_table(x,y):
    arcade.draw_rectangle_filled(x/2,y/2,x,y,arcade.color.BROWN)
    arcade.draw_rectangle_filled(x/2,y/2,x*4/5,y*4/5,arcade.color.BANGLADESH_GREEN)

    # Keep the window open until the user hits the 'close' button


class Deck:
    def __init__(self):
        self.cards = deque()
        self.build()
        self.briscola = []

    def build(self):
        for i in ["Bastoni", "Denari", "Spade", "Coppe"]:
            for j in range(1,11):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)
    def length(self):
        return len(self.cards)

    def get_card(self):
        return self.cards.popleft()
    def choice_briscola(self,width,height):
        self.briscola= self.get_card()
        self.briscola.set_center(width/4+4+50+3, height/2)
    def show_briscola(self):
        return "LA BRISCOLA E' {}".format(self.briscola)

    def __repr__(self):
        return 'Deck: [{} Cards]'.format(self.length())


class Game(arcade.Window):
    def __init__(self, width,height,title):

        super().__init__(width,height,title,resizable=True)
        self.players = []
        self.deck = None
        self.order = None
        self.winner=0
        self.is_playing=[1,0]
        self.playing=0
        self.played_card=[]
        self.N= 2
        self.coperto=1
        self.wait=10
        self.state=0
        self.start =0
        self.start_button = None
        self.vai_button = None
        self.y_p=0
        arcade.set_background_color(arcade.color.GRAY)


    def on_draw(self):
        arcade.start_render()
        draw_table(self.width,self.height)

        if self.start==0:
            arcade.draw_text(" BENVENUTO!\n CLICCA START PER INIZIARE ", self.width/2,self.height/2+50,arcade.color.WHITE,
                             align="center",anchor_x="center", anchor_y="center",bold=True,font_size=20)
            self.start_button.draw()

        if self.start and self.playing: ## INIZIA GIOCO E STIAMO GIOCANDO ##
            ###### DISEGNA CARTE GIOCATE ######
            print(" PRINTO CARTE GIOCATE, LUNGH = ", len(self.played_card))
            if len(self.played_card)<self.N:
                for n in range(len(self.played_card)):
                    p=self.order[n]
                    x_p= self.width/2
                    if self.players[p].cards:
                        y_p= -(2*p-1)*(self.played_card[n].height +dist_card) \
                         + self.players[p].cards[0].center_y
                        self.y_p=y_p
                    draw_front_card(self.played_card[n],x_p,self.y_p)
            ###### DISEGNO MAZZO #####
            if self.deck.length():
                draw_back_card(self.width/4+4, self.height/2)
                draw_front_card(self.deck.briscola,self.width/4+4 +pixel_w+3,self.height/2)
                arcade.draw_text("N° Carte = " + str(self.deck.length()), self.width/4+4, self.height/2-pixel_h/2 -4*dist_card,
                                 arcade.color.WHITE, align="center",anchor_x="center", anchor_y="center",
                                 bold=True,font_size=15)

            #########  SE DEVO ASPETTARE  IL GIOCATORE ( VAI =1) TUTTE RETRO
            ######## ALTRIMENTI GIOCA ####
            ###### DISEGNO CARTE COPERTE PER ENTRAMBI I GIOCATORI########
            if self.coperto:
                if len(self.played_card)==self.N:
                    t=self.players[self.winner].name+" HA VINTO LA MANO!"
                    arcade.draw_text(t, self.width/2, self.height*6/7, arcade.color.WHITE,
                                     align="center",anchor_x="center", anchor_y="center", bold=True, font_size=18)
                    for n in range(self.N):
                        if self.Winner(self.played_card)==n:
                            print(" self.order = " ,self.order," self.winner = ",self.winner," n= ",n)
                            arcade.draw_text("WIN",self.width/2 + (2*n-(self.N-1))*(pixel_w+dist_card)/2,
                                             self.height/2+pixel_h/2+10,arcade.color.RED,align="center", anchor_x="center",
                                             anchor_y="center",bold=True,font_size=18)
                        draw_front_card(self.played_card[n],self.width/2 + (2*n-(self.N-1))*(pixel_w+dist_card)/2,
                                        self.height/2)
                tt=" TOCCA A " + self.players[self.order[self.state]].name
                arcade.draw_text(tt,self.vai_button.center_x,self.vai_button.center_y+50,arcade.color.WHITE,align="center",
                                 anchor_x="center", anchor_y="center",bold=True,font_size=18)
                self.vai_button.draw()
                #scrivo cose
                p=0
                for pl in self.players:
                    for i in range(len(pl.cards)):
                        draw_back_card(self.width/2 +(i-1)*(pixel_w+dist_card),self.height*pos_card[p])
                    p+=1
            else:
            ###### DISEGNO CARTE SCOPERTE PER IL GIOCATORE ########
                for pl in self.players:
                    for i in range(len(pl.cards)):
                        if pl.name == "PLAYER_1":
                            if self.is_playing[0]:
                                draw_front_card(pl.cards[i],self.width/2 +(i-1)*(pixel_w+dist_card),self.height*pos_card[0])
                            else:
                                draw_back_card(self.width/2 +(i-1)*(pixel_w+dist_card),self.height*pos_card[0])
                        else:
                            if self.is_playing[1]:
                                draw_front_card(pl.cards[i],self.width/2 +(i-1)*(pixel_w+dist_card),self.height*pos_card[1])
                            else:
                                draw_back_card(self.width/2 +(i-1)*(pixel_w+dist_card), self.height*pos_card[1])
        if self.start and self.playing==0 and self.players[self.order[-1]].LengthCard() == 0:
            arcade.draw_text("PUNTEGGIO FINALE",self.width/2,self.height/2+20,arcade.color.WHITE,align="center",
                             anchor_x="center", anchor_y="center",bold=True,font_size=18)
            win=0
            for i in range(len(self.players)):
               if self.players[i].points>self.players[win].points:
                   win=i
            if win==0 and self.players[win].points==60:
                win=None
            for i in range(len(self.players)):
                text = self.players[i].name + " " + str(self.players[i].points)
                if win == i:
                    arcade.draw_text(text,self.width/2,self.height/2-20*i,arcade.color.RED,align="center",
                                     anchor_x="center", anchor_y="center",bold=True,font_size=18)
                else:

                    arcade.draw_text(text,self.width/2,self.height/2-20*i,arcade.color.WHITE,align="center",
                                     anchor_x="center", anchor_y="center",bold=True,font_size=18)

    def on_update(self,delta_time):
        self.start_button.set_center(self.width/2,self.height/2)
        self.vai_button.set_center(self.width*3/4,self.height/2)
        self.playing=1
        print("self.start = ",self.start)
        print("self.coperto = ",self.coperto)
        print("self.playing = ",self.playing)
        if self.start and self.players[self.order[-1]].LengthCard() > 0 :
            # print(deck)
            if self.state==0 and self.coperto==0:
                self.played_card = []
            self.is_playing = [0] * self.N
            self.is_playing[self.order[self.state]] = 1
            print("self.state = ",self.state)
            # print("LA BRISCOLA E' ", self.deck.briscola)
                #### vediamo le carte del giocatore ( lo chiedo perchè magari giocano sullo
                #### stesso pc e non vuole farlo vedere###
                ###### METTIAMO VALORE PER MOSTRARE TUTTO COPERTO #####
            #for i in self.players[self.order[self.state]].cards:
            #    print(" l'indice è",i.index)
            if self.coperto:
                print(" CARTE COPERTE IN ATTESA DEL GIOCATORE ",self.order[self.state]+1)
            else:

                if self.wait == 10:
                    print("waiting for player ",self.order[self.state]+1,"...")
                else:
                    self.played_card.append(self.players[self.order[self.state]].cards[self.wait])
                    self.players[self.order[self.state]].play_card(self.wait,self.width,self.height)
                    self.coperto=1
                    if self.state<self.N-1:
                        self.state+=1
                        self.wait=10
                    else:
                        self.winner = self.order[self.Winner(self.played_card)]
                        self.players[self.winner].count_points(self.played_card)
                        self.state=0
                        self.wait=10
                        print("5")
                        ########### aspetta per la scelta
                        ### vediamo chi vince###
                        ### assegna punti##
                        print("IL GIOCATORE ", self.players[self.winner].name, " VINCE LA MANO!")
                        ### riordina giocatori###
                        self.order = []
                        for newp in range(self.winner, self.N):
                            self.order.append(newp)
                        for newp in range(self.winner):
                            self.order.append(newp)
                        ###PESCA LE CARTE###
                        for newp in self.order:
                            if self.deck.length():
                                self.players[newp].give_card(self.deck.get_card())
                            else:
                                if self.players[self.order[0]].LengthCard() == 3:
                                    self.players[newp].give_card(self.deck.briscola)

                        ###### RI SETTO I CENTRI #######
                        p = 0
                        for pl in self.players:
                            for c in range(len(pl.cards)):
                                if p:
                                    pl.cards[c].set_center(self.width / 2 - (c - 1) * 53, self.height * 2 / 3)
                                    pl.cards[c].set_index(c)
                                else:
                                    pl.cards[c].set_center(self.width / 2 - (c - 1) * 53, self.height / 3)
                                    pl.cards[c].set_index(c)
                            p+=1
        else:
            if self.start:
                self.Rank()
                self.playing=0
        ### da modificare  ##
    def setup(self):
        self.deck = Deck()
        #print("Inserisci numero di giocatori:")
        self.N = 2
        pl_name = ["PLAYER_1","PLAYER_2"]
        #### AGGIUNGIAMO I GIOCATORI
        for i in range(len(pl_name)):
            self.players.append(Player(pl_name[i]))

        self.order=[i for i in range(self.N)]
        self.start_button=StartTextButton(self.width/2,self.height/2)
        self.vai_button =VaiTextButton(self.width*3/4,self.height/2)


        #for i in range(N):
        #    print("Inserisci nome giocatore ", i + 1)
        #    name = input("")
        #    print("Benvenuto ", name, "!")
        #    pl_name.append(name)
        #    self.players.append(Player(name))
        self.deal()
        self.deck.choice_briscola(self.width,self.height)
#### DEAL == DAI LE CARTE
    def deal(self):
        p=0
        for player in self.players:
            for i in range(3):
                player.give_card(self.draw_card(self.width,self.height,p,i))
            p+=1

    def on_mouse_press(self, x, y, button, modifiers):
        if self.start==0:
            check_mouse_press_for_buttons(x, y, [self.start_button])
        else:
            if self.coperto:
                check_mouse_press_for_buttons(x, y, [self.vai_button])
            else:
                check_mouse_press_for_buttons(x, y, self.players[self.order[self.state]].cards)


    def on_mouse_release(self, x, y, button,modifiers):
        if self.start and self.coperto==0:
            print(" STO CLICCANDO UNA CARTA")
            a = str(check_mouse_release_for_buttons(x, y, self.players[self.order[self.state]].cards))
            if a==None:
                print("")
            else:
                self.wait= int(a)
            print("self.wait è ",self.wait)

        else:
            if self.start and self.coperto:
                print( "SONO IN VAI")
                a = str(check_mouse_release_for_buttons(x, y, [self.vai_button]))
                if a == None:
                    print("Vai = 0")
                else:
                    self.coperto = int(a)
                print(" gioca! ")
            else:
                print("SONO IN START")
                a = str(check_mouse_release_for_buttons(x, y, [self.start_button]))
                if a==None:
                    print("Start = 0")
                else:
                    self.start= int(a)
                print(" INZIA! ")

    # in python use underscore not camelCase for methods
    def draw_card(self,x,y,p,i):
        crd=self.deck.get_card()
        if p:
            crd.set_center(x/ 2 + (i - 1) * 53, y*2/3)
            crd.set_index(i)
        else:
            crd.set_center(x/ 2 + (i - 1) * 53, y/3)
            crd.set_index(i)
        print(crd.index)

        # avoid mutating other object properties in other objects
        return crd

    def restart_game(self):
        # simply rebuild the deck - it will reshuffle all cards
        self.deck.build()
        for player in self.players:
            player.return_cards()

    def Winner(self,played_card):
        brisc_ind= [0]*len(played_card)
        order_point=[10,1,9,2,3,4,5,6,7,8]
        point=0
        winner=0
        for i in range(len(played_card)):
            #### TROVIAMO LE BRISCOLE ###
            if played_card[i].suit==self.deck.briscola.suit:
                brisc_ind[i]=1
        if sum(brisc_ind) ==0:
            ####mettiamo criteri
            new_brisc = played_card[0].suit
            for i in range(len(played_card)):
                #### TROVIAMO LE BRISCOLE ###
                if played_card[i].suit == new_brisc:
                    brisc_ind[i]=1

        for k in range(len(brisc_ind)):
            if  brisc_ind[k]==1 and order_point[played_card[k].value-1]>point:
                point=order_point[played_card[k].value-1]
                winner= k
        return winner
    def Rank(self):
        print("I PUNTEGGI SONO:")
        for i in range(len(self.players)):
            print(self.players[i].name," ",self.players[i].points)

'''
def on_update_WIP(self):
    self.order = np.arange(self.N)
    self.winner = 0
    while (self.players[self.order[-1]].LengthCard() > 0):
        #print(deck)
        self.played_card = []
        for i in self.order:
            #print("LA BRISCOLA E' ", self.deck.briscola)
            #### vediamo le carte del giocatore ( lo chiedo perchè magari giocano sullo
            #### stesso pc e non vuole farlo vedere###
            self.is_playing =[0]*self.N
            self.is_playing[i]=1
            ###### METTIAMO VALORE PER MOSTRARE TUTTO COPERTO #####
            self.coperto=1
            #print("Tocca a ", self.players[i].name, "! Clicca un tasto per iniziare")
            #input("")
            self.coperto=0
            #### scegliamo la carta####
            #err2 = 1
            self.wait=10
            while (self.wait==10):
                ########### aspetta per la scelta
            self.played_card.append(players[i].cards[self.wait])
            self.players[i].play_card(self_wait)
                    ### vediamo chi vince###
        self.winner = self.order[self.Winner(self.played_card)]
        self.players[self.winner].count_points(self.played_card)
        ### assegna punti##
        print("IL GIOCATORE ", self.players[winner].name, " VINCE LA MANO!")
        ### riordina giocatori###
        self.order = []
        for newp in range(self.winner, self.N):
            self.order.append(newp)
        for newp in range(winner):
            self.order.append(newp)
        ###PESCA LE CARTE###
        for newp in self.order:
            if self.deck.length():
                self.players[newp].give_card(self.deck.get_card())
            else:
                if self.players[self.order[0]].LengthCard() == 3:
                    self.players[newp].give_card(self.deck.briscola)

        ###### RI SETTO I CENTRI #######
        p=0
        for pl in self.players:
            for c in range(len(pl.cards)):
                if p:
                    pl.cards[c].set_center(x / 2 - (c - 1) * 53, y * 2 / 3)
                    pl.cards[c].index=c
                else:
                    pl.cards[c].set_center(x / 2 - (c - 1) * 53, y / 3)
                    pl.cards[c].index = c
        input("Invio per andare avanti")
'''

#card=CardButton(4,"Spade")
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TEXT ="BRISCOLA"
#arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

game=Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TEXT)
game.setup()
arcade.run()


