
from controller import Controller
from utils import Utils

import pygame as pg

class HumanController(Controller):

    def __init__(self, controlled_object, control_scheme):
        Controller.__init__(self, controlled_object)
        self.control_scheme = control_scheme

    def handle(self, event, env):
        
        keys = pg.key.get_pressed()

        sign = 0

        if keys[self.control_scheme["FORWARD"]]:
            sign = 1
        if keys[self.control_scheme["BACKWARD"]]:
            sign = -1
            
        mpos = pg.mouse.get_pos()
        angle = Utils.get_look_angle(self.controlled_object.position, mpos)
        self.controlled_object.turn(angle % 360)

        if event.type == pg.MOUSEBUTTONDOWN:
            # bullet = self.controlled_object.shoot()
            # if bullet:
            #     env[1].append(bullet)
            self.controlled_object.shoot(env[2])

        if sign:
            angle = self.controlled_object.rotation
            self.controlled_object.move(sign)        