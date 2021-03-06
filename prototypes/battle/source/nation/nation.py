#!/usr/bin/python3
# Imperialism remake
# Copyright (C) 2015 Spitaels <spitaelsantoine@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from PyQt5.QtGui import QPixmap

FLAG_WIDTH = 600
FLAG_HEIGHT = 400
COAT_OF_ARMS_WIDTH = 600
COAT_OF_ARMS_HEIGHT = 800


class Nation:
    def __init__(self, name, computer, coat_of_arms, flag):
        """function __init__
        :param name: str (not empty)
        :param computer: bool
        :param coat_of_arms: QPixmap (not null)
        :param flag: QPixmap (not null)
        """
        if not isinstance(name, str) or name == '':
            raise ValueError('name must be a non empty string')
        if not isinstance(computer, bool):
            raise ValueError('computer must be a boolean')
        if not isinstance(coat_of_arms, QPixmap) or coat_of_arms is None or coat_of_arms.isNull():
            raise ValueError('coatOfArms must be a not null pixmap ' + name)
        if not isinstance(flag, QPixmap) or flag is None or flag.isNull():
            raise ValueError('flag must be a not null pixmap')
        if coat_of_arms.width() != COAT_OF_ARMS_WIDTH or coat_of_arms.height() != COAT_OF_ARMS_HEIGHT:
            raise ValueError('coat_of_arms must have the dimension ' + str(COAT_OF_ARMS_WIDTH) + 'x' + str(
                    COAT_OF_ARMS_HEIGHT) + ' ' + name)
        if flag.width() != FLAG_WIDTH or flag.height() != FLAG_HEIGHT:
            raise ValueError('flag must have the dimension ' + str(FLAG_WIDTH) + 'x' + str(FLAG_HEIGHT))
        self.name = name
        self.computer = computer
        self.coatOfArms = coat_of_arms
        self.flag = flag

    # Operations
    def draw_flag(self, scene, size):
        """function draw_flag

        :param scene: QGraphicsScene
        :param size: QSize

        no return
        """
        raise NotImplementedError()

    def draw_coat_of_arms(self, scene, size):
        """function draw_coat_of_arms

        :param scene: QGraphicsScene
        :param size: QSize

        no return
        """
        pixmap = self.coatOfArms.scaled(size)
        scene.addPixmap(pixmap)

    def __str__(self):
        return self.name.title()  # capitalize all words

    def __repr__(self):
        return '\n\tName: %s\n\tComputer: %r\n' % (self.name, self.computer)
