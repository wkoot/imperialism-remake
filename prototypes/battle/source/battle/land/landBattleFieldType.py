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

from PyQt5.QtGui import QPixmap, QColor


class LandBattleFieldType:
    """Class LandBattleFieldType
    """

    def __init__(self, name, color, texture):
        if not isinstance(name, str) or name == '':
            raise ValueError('name must be a non empty string')
        if texture is not None and (not isinstance(texture, str) or texture == ''):
            raise ValueError('texture must be a non empty string')
        if color is not None and (not isinstance(color, str) or color == ''):
            raise ValueError('color must be a non empty string')
        self.color = QColor(color)
        self.color_str = color
        self.texture_str = texture
        self.texture = QPixmap(texture)
        if not self.color.isValid() and self.texture.isNull():
            raise ValueError('texture or color must be specified')
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'name=\'%s\' color=\'%s\' texture=\'%s\'' % (self.name, self.color_str, self.texture_str)
