import socket
from _thread import *
import sys
from collections import deque
import pickle
import arcade
import random
import json

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

### scelgo il seed
sd=random.randint(0,1000)



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
        print(self, " ha centro in (",self.center_x,",",self.center_y,") ed indice ", self.index)


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
                print("button index", button.index)
                return button.index
            else:
                if button.text =="Start":
                    return 1
                else:
                    print("SONO QUA")
                    return 1

def draw_table(x,y):
    #arcade.draw_rectangle_filled(x/2,y/2,x,y,arcade.color.BROWN)
    arcade.draw_rectangle_filled(x/2,y/2,x,y,arcade.color.BANGLADESH_GREEN)

    #background._set_height(y)
    #background.draw()

    # Keep the window open until the user hits the 'close' button

