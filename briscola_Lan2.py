from collections import deque
import random
import arcade
from network import Network
import numpy as np
import pickle
from briscola_class import *

pixel_w = 50  ## lunghezza base carta
rapp_xony = 497 / 821  ## rapporto tra base ed altezza carta
pixel_h = pixel_w / rapp_xony
dist_card = 4
pos_card = [1 / 4, 3 / 4]
val_glob = {1: "ace",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "jack",
            9: "horse",
            10: "king"}
suit_glob = {"Denari": "g",
             "Coppe": "c",
             "Bastoni": "b",
             "Spade": "s"}
back = arcade.Sprite("sprite/briscola-cards/n_back.png")
background = arcade.Sprite("sprite/briscola-cards/green_felt.jpg")
background._set_scale(600 / background._get_width())
back._set_scale(pixel_w / back._get_width())

'''
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
                    return 1

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
        #random.shuffle(self.cards)
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
'''


class Game(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title, resizable=True)
        self.net = Network()
        self.player = Player("me")
        self.player_o = [Player("other")]
        self.deck = None
        self.order = None
        self.order_old = None
        self.winner = 0
        self.playing = 0
        self.played_card = []
        self.N = 2
        self.wait = 9
        self.wait_o = 9
        self.state = 0
        self.start = 0
        self.start_o = [0]
        self.start_button = None
        self.vai_button = None
        self.y_p = 0
        self.vai = 0
        self.vai_o = 0
        self.id = None
        self.deal_card = 0
        self.seed = None
        self.seed_o = None
        self.given = 0
        arcade.set_background_color(arcade.color.GRAY)

    '''
        @staticmethod
        def parse_data(data):
            print("data =", data)
            try:
                d = data.split(":")[1].split(",")
                print(d)
                #print(int(d[0]), int(d[1]), int(d[2]), int(d[3]), int(d[4]),int(d[5]),int(d[6]),int(d[7]) ,int(d[8]))
                return pickle.load(data)
            except:
                print(" sono in except")
                return 0,0,0,0,0,0,0,0,0
    '''

    def send_data(self):
        """
        Send position to server
        :return: None
        """

        data = [self.seed, self.start, self.wait, self.vai]
        reply = self.net.send(data)
        return reply

    def on_draw(self):
        arcade.start_render()
        # background._set_scale(self.width / background._get_width())
        draw_table(self.width, self.height)
        if self.start == 0:
            arcade.draw_text(" BENVENUTO!\n CLICCA START PER INIZIARE ", self.width / 2, self.height / 2 + 50,
                             arcade.color.WHITE,
                             align="center", anchor_x="center", anchor_y="center", bold=True, font_size=20)
            self.start_button.draw()
        if self.start and self.start_o[0] == 0:
            arcade.draw_text(" ASPETTANDO L'AVVERSARIO... ", self.width / 2, self.height / 2 + 50,
                             arcade.color.WHITE,
                             align="center", anchor_x="center", anchor_y="center", bold=True, font_size=20)
        if self.start and self.start_o[0] and self.playing:  ## INIZIA GIOCO E STIAMO GIOCANDO ##
            ###### DISEGNA CARTE GIOCATE ######
            print(" PRINTO CARTE GIOCATE, LUNGH = ", len(self.played_card))
            if len(self.played_card) < self.N:
                for n in range(len(self.played_card)):
                    p = self.order[n]
                    x_p = self.width / 2
                    ##### VA BENE A TUTTO SCHERMO
                    if self.id == p:
                        y_p = (pixel_h + dist_card) \
                              + pos_card[0] * self.height
                    else:
                        y_p = -(pixel_h + dist_card) \
                              + pos_card[1] * self.height
                    self.y_p = y_p
                    draw_front_card(self.played_card[n], x_p, self.y_p)
            ###### DISEGNO MAZZO #####
            if self.deck.length():
                draw_back_card(self.width / 4 + dist_card, self.height / 2)
                draw_front_card(self.deck.briscola, self.width / 4 + dist_card + pixel_w + 3, self.height / 2)
                arcade.draw_text("N° Carte = " + str(self.deck.length()), self.width / 4 + dist_card,
                                 self.height / 2 - pixel_h / 2 - 4 * dist_card,
                                 arcade.color.WHITE, align="center", anchor_x="center", anchor_y="center",
                                 bold=True, font_size=15)
            ################# DISEGNO CARTE GIOCATORI

            if len(self.played_card) == self.N:
                if self.winner == self.id:
                    t = "HAI VINTO LA MANO!"
                    self.vai_button.draw()
                else:
                    t = self.player_o[0].name + " HA VINTO LA MANO!"
                arcade.draw_text(t, self.width / 2, self.height * 6 / 7, arcade.color.WHITE,
                                 align="center", anchor_x="center", anchor_y="center", bold=True, font_size=18)
                for n in range(self.N):
                    try:
                        if self.order_old[n] == self.winner:
                            arcade.draw_text("WIN", self.width / 2 + (2 * n - (self.N - 1)) * (pixel_w + dist_card) / 2,
                                             self.height / 2 + pixel_h / 2 + 10, arcade.color.RED, align="center",
                                             anchor_x="center",
                                             anchor_y="center", bold=True, font_size=18)
                        draw_front_card(self.played_card[n],
                                        self.width / 2 + (2 * n - (self.N - 1)) * (pixel_w + dist_card) / 2,
                                        self.height / 2)
                    except:
                        print("aspetta")
            else:
                if self.state != self.N:
                    if self.order[self.state] == self.id:
                        tt = "TOCCA A TE"
                        if self.vai == 0:
                            self.vai_button.draw()
                    else:
                        tt = " TOCCA A " + self.player_o[0].name

                    arcade.draw_text(tt, self.vai_button.center_x, self.vai_button.center_y + 50, arcade.color.WHITE,
                                     align="center",
                                     anchor_x="center", anchor_y="center", bold=True, font_size=18)
            ###### DISEGNO CARTE GIOCATORI ########
            for pl in self.player_o:
                for i in range(len(pl.cards)):
                    draw_back_card(self.width / 2 + (i - 1) * (pixel_w + dist_card), self.height * pos_card[1])
            for i in range(len(self.player.cards)):
                draw_front_card(self.player.cards[i], self.width / 2 + (i - 1) * (pixel_w + dist_card),
                                self.height * pos_card[0])
        if self.start and self.start_o[0] and self.playing == 0 :
            arcade.draw_text("PUNTEGGIO FINALE", self.width / 2, self.height / 2 + 20, arcade.color.WHITE,
                             align="center",
                             anchor_x="center", anchor_y="center", bold=True, font_size=18)
            win = 0
            for i in range(len(self.player_o)):
                if self.player_o[i].points > self.player_o[win].points:
                    if self.id==0:
                        win = 1
                    else:
                        win=0

            if self.player.points > self.player_o[win].points:
                win = self.id
            if win == 0 and self.player_o[win].points == 120 / self.N:
                win = None

            text = self.player.name + " " + str(self.player.points)
            if win == self.id:
                arcade.draw_text(text, self.width / 2, self.height / 2, arcade.color.RED, align="center",
                                 anchor_x="center", anchor_y="center", bold=True, font_size=18)
            else:
                arcade.draw_text(text, self.width / 2, self.height / 2, arcade.color.WHITE, align="center",
                                 anchor_x="center", anchor_y="center", bold=True, font_size=18)
            for i in range(len(self.player_o)):
                text = self.player_o[i].name + " " + str(self.player_o[i].points)
                if win != self.id:
                    arcade.draw_text(text, self.width / 2, self.height / 2 - 20 * (i + 1), arcade.color.RED,
                                     align="center",
                                     anchor_x="center", anchor_y="center", bold=True, font_size=18)
                else:
                    arcade.draw_text(text, self.width / 2, self.height / 2 - 20 * (i + 1), arcade.color.WHITE,
                                     align="center",
                                     anchor_x="center", anchor_y="center", bold=True, font_size=18)

    def on_update(self, delta_time):
        self.start_button.set_center(self.width / 2, self.height / 2)
        self.vai_button.set_center(self.width * 3 / 4, self.height / 2)
        self.playing = 1
        if self.seed != None:
            self.seed_o = self.seed
        print("---------------------")
        print("length card player =", self.player.LengthCard())
        print("length card player = ", self.player_o[0].LengthCard())
        print("self.start = ", self.start)
        print("self.playing = ", self.playing)
        print("self.wait = ", self.wait)
        print("self.wait_o = ", self.wait_o)
        print("self.state =", self.state)
        print("self.start_o =", self.start_o)
        print("self.played_card", self.played_card)
        print(" self.id =", self.id)
        print("self.seed =", self.seed)
        print("self.seed_o", self.seed_o)
        print("self.order =", self.order)
        print("self.vai = ", self.vai)
        print("self.vai_o = ", self.vai_o)
        print("given = ", self.given)
        print("---------------------")
        if self.start_o[0] == 0 and self.start:
            self.id = 0
            print("WAITING FOR THE OTHER PLAYER")
        if self.start == 0 and self.start_o[0]:
            self.id = 1
        if self.start and self.start_o[0]:
            print("start e start_o =1")
            if self.deal_card == 0:
                # print(deck)
                print(" sono entrato nel dealer")
                ### FA IL DEALER
                # print("self.deck.cards",self.deck.cards)
                # self.deck.build()
                print("self.seed_o = ", self.seed_o)
                print("self.seed =", self.seed)
                random.seed(self.seed_o)
                random.shuffle(self.deck.cards)
                print("self.deck.cards", self.deck.cards)
                self.deal()
                self.deck.choice_briscola(self.width, self.height)
                self.deal_card = 1
                print("self.player = ", self.player)
                print("self.player_o", self.player_o[0])
                print("self.player.LengthCard() =", self.player.LengthCard())
                print("self.player_o[0].LengthCard() = ", self.player_o[0].LengthCard())
            if self.player.LengthCard() > 0 or self.player_o[0].LengthCard() > 0:
                print("self.state = ", self.state)

                #    print(" l'indice è",i.index)
                if self.state == self.N:
                    # self.stelate = 0
                    self.wait = 9
                    # self.wait_o = 9
                    if self.wait == 9 and self.wait_o == 9 and self.given and (self.vai_o or self.vai):
                        self.state = 0
                        self.played_card = []
                        self.given = 0
                    if self.given == 0 and self.state == self.N:
                        self.given = 1
                        self.winner = self.order[self.Winner(self.played_card)]
                        if self.winner == self.id:
                            print("IL GIOCATORE ", self.player.name, " VINCE LA MANO!")
                            self.player.count_points(self.played_card)
                            print(" punti me",self.player.points)
                        else:
                            print("IL GIOCATORE ", self.player_o[0].name, " VINCE LA MANO!")
                            self.player_o[0].count_points(self.played_card)
                            print("punti other =", self.player_o[0].points)
                        self.order_old = self.order
                        self.order = []
                        for newp in range(self.winner, self.N):
                            self.order.append(newp)
                        for newp in range(self.winner):
                            self.order.append(newp)
                        ###PESCA LE CARTE###
                        for i in range(self.N):
                            ## per me
                            if self.order[i] == self.id:
                                if self.deck.length():
                                    self.player.give_card(self.deck.get_card())
                                else:
                                    if self.player_o[0].LengthCard() == 3:
                                        self.player.give_card(self.deck.briscola)
                            ### per l'altro
                            else:
                                if self.deck.length():
                                    self.player_o[0].give_card(self.deck.get_card())
                                else:
                                    if self.player.LengthCard() == 3:
                                        self.player_o[0].give_card(self.deck.briscola)
                        ###### RI SETTO I CENTRI #######
                        self.vai = 0
                        self.vai_o = 0
                        for c in range(len(self.player.cards)):
                            self.player.cards[c].set_center(self.width / 2 - (c - 1) * 53, self.height * pos_card[0])
                            self.player.cards[c].set_index(c)
                        for c in range(len(self.player_o[0].cards)):
                            self.player_o[0].cards[c].set_center(self.width / 2 - (c - 1) * 53,
                                                                 self.height * pos_card[1])
                            self.player_o[0].cards[c].set_index(c)
                    ########### aspetta per la scelta
                    ### vediamo chi vince###
                    ### assegna punti##
                    ### riordina giocatori###
                else:
                    if self.id != self.order[self.state]:
                        if self.wait_o == 9:
                            print(" IN ATTESA DEL GIOCATORE ", self.order[self.state] + 1)
                        else:
                            self.played_card.append(self.player_o[0].cards[self.wait_o])
                            self.player_o[0].play_card(self.wait_o, self.width, self.height)
                            self.state += 1
                            # self.wait_o = 9
                    else:
                        if self.wait == 9:
                            print("waiting for player ", self.order[self.state] + 1, "...")
                        else:
                            print(" le mia carte sono ", self.player.cards)
                            self.played_card.append(self.player.cards[self.wait])
                            print("played_card me = ", self.played_card)
                            self.player.play_card(self.wait, self.width, self.height)
                            # if self.state<self.N-1:
                            self.state += 1
                            # self.wait = 9

            if (self.player.LengthCard() == 0 or self.player_o[
                0].LengthCard() == 0) and self.deal_card and self.state == 2:
                self.Rank()
                self.playing = 0
        ### COSA MANDIAMO ALL'ALTRO GIOCATORE?  ##

        # if self.start and self.start_o[0] and self.deal_card:
        # print(self.start_o[0],self.played_card,self.state,self.wait,self.deal_card,self.player.cards,self.player_o[0].cards,self.deck.cards,self.deck.briscola)
        # [self.start_o[0],self.played_card,self.state,self.wait,self.deal_card,self.player.cards,self.player_o[0].cards,self.deck.cards,self.deck.briscola] = self.send_data()
        [self.seed, self.start_o[0], self.wait_o, self.vai_o] = self.send_data()
        # else:
        #    print(self.start_o[0],self.played_card,self.state,self.wait,self.deal_card)
        #    self.start_o[0],self.played_card,self.state,self.wait,self.deal_card = self.parse_data(self.send_data())

    def setup(self):
        self.deck = Deck()
        # self.id= self.net.getid()
        # print("Inserisci numero di giocatori:")
        print("il deck è", self.deck)
        self.N = 2
        # pl_name = ["me "," other"]
        #### AGGIUNGIAMO I GIOCATORI
        # for i in range(self.N):
        #   if self.id == i:
        #       self.player=Player(pl_name[i])
        #   else:
        #      self.player_o.append(Player(pl_name[i]))

        self.order = [i for i in range(self.N)]
        self.start_button = StartTextButton(self.width / 2, self.height / 2)
        self.vai_button = VaiTextButton(self.width * 3 / 4, self.height / 2)

    #### DEAL == DAI LE CARTE
    def deal(self):

        for p in range(self.N):
            if self.order[p] == self.id:

                for i in range(3):
                    self.player.give_card(self.draw_card(self.width, self.height, 0, i))
            else:
                for i in range(3):
                    self.player_o[0].give_card(self.draw_card(self.width, self.height, 1, i))

    def on_mouse_press(self, x, y, button, modifiers):
        if self.start == 0:
            check_mouse_press_for_buttons(x, y, [self.start_button])
        else:
            if self.state < self.N:
                if self.order[self.state] == self.id:
                    if self.vai == 0:
                        check_mouse_press_for_buttons(x, y, [self.vai_button])
                    else:
                        check_mouse_press_for_buttons(x, y, self.player.cards)
            else:
                if self.vai == 0:
                    check_mouse_press_for_buttons(x, y, [self.vai_button])

    def on_mouse_release(self, x, y, button, modifiers):
        if self.start and self.start_o[0] and self.vai:
            print(" STO CLICCANDO UNA CARTA")
            a = str(check_mouse_release_for_buttons(x, y, self.player.cards))
            if a == None:
                print("")
            else:
                self.wait = int(a)
            print("self.wait è ", self.wait)

        else:
            if self.start and self.start_o[0] and self.vai == 0:
                print("SONO IN VAI")
                a = str(check_mouse_release_for_buttons(x, y, [self.vai_button]))
                if a == None:
                    print("Vai = 0")
                else:
                    self.vai = int(a)
                print(" gioca! ")
            else:
                if self.start == 0:
                    print("SONO IN START")
                    a = str(check_mouse_release_for_buttons(x, y, [self.start_button]))
                    if a == None:
                        print("Start = 0")
                    else:
                        self.start = int(a)
                    print(" INZIA! ")

    # in python use underscore not camelCase for methods
    def draw_card(self, x, y, p, i):
        crd = self.deck.get_card()
        crd.set_center(x / 2 + (i - 1) * 53, y * pos_card[p])
        crd.set_index(i)
        print("il crd index è ", crd.index)

        # avoid mutating other object properties in other objects
        return crd

    def restart_game(self):
        # simply rebuild the deck - it will reshuffle all cards
        self.deck.build()
        for player in self.player_o:
            player.return_cards()

    def Winner(self, played_card):
        brisc_ind = [0] * len(played_card)
        order_point = [10, 1, 9, 2, 3, 4, 5, 6, 7, 8]
        point = 0
        winner = 0
        for i in range(len(played_card)):
            #### TROVIAMO LE BRISCOLE ###
            if played_card[i].suit == self.deck.briscola.suit:
                brisc_ind[i] = 1
        if sum(brisc_ind) == 0:
            ####mettiamo criteri
            new_brisc = played_card[0].suit
            for i in range(len(played_card)):
                #### TROVIAMO LE BRISCOLE ###
                if played_card[i].suit == new_brisc:
                    brisc_ind[i] = 1

        for k in range(len(brisc_ind)):
            if brisc_ind[k] == 1 and order_point[played_card[k].value - 1] > point:
                point = order_point[played_card[k].value - 1]
                winner = k
        return winner

    def Rank(self):
        if self.given==0:
            self.given=1
            self.winner = self.order[self.Winner(self.played_card)]
            if self.winner == self.id:
                print("IL GIOCATORE ", self.player.name, " VINCE LA MANO!")
                self.player.count_points(self.played_card)
                print(" punti me", self.player.points)
            else:
                print("IL GIOCATORE ", self.player_o[0].name, " VINCE LA MANO!")
                self.player_o[0].count_points(self.played_card)
                print("punti other =", self.player_o[0].points)
            print("I PUNTEGGI SONO:")
            print(self.player.name, " ", self.player.points)
        for i in range(len(self.player_o)):
            print(self.player_o[i].name, " ", self.player_o[i].points)


# card=CardButton(4,"Spade")
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TEXT = "BRISCOLA"
# arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TEXT)
game.setup()
arcade.run()
