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

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from prototypes.battle.source.battle.battleView import MainBattleWindow
from prototypes.battle.source.battle.land.landArmy import LandArmy
from prototypes.battle.source.battle.land.landBattleView import LandBattleView
from prototypes.battle.source.battle.land.landUnitInBattle import LandUnitInBattle
from prototypes.battle.source.config.config import Config
from prototypes.battle.source.base.constants import version


CONFIG_FILE = 'config.ini'

if __name__ == '__main__':
    v = version()
    print('Battle prototype version: %f' % version())
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.png'))

    # load config files
    window_config = Config(CONFIG_FILE, v)

    # Set up a land battle
    nation_uk = window_config.get_nation("uk")
    nation_uk.computer = True
    nation_fr = window_config.get_nation("france")

    unit_militia_default = window_config.get_unit_type('Militia I')
    current_unit = LandUnitInBattle(False, 'Charge', False, 50, 25, 1, unit_militia_default, nation_fr)
    targetted_unit = LandUnitInBattle(False, 'Shoot', False, 75, 50, 1, unit_militia_default, nation_uk)

    defender = LandArmy(False, None, nation_uk)
    attacker = LandArmy(False, None, nation_fr)

    initial_battle_state = dict(auto_combat=False, turn=0,
                                current_unit=current_unit, targetted_unit=targetted_unit,
                                defender=defender, attacker=attacker)

    # start the battle view
    mainWindow = MainBattleWindow(window_config)
    mainWindow.ui = LandBattleView(mainWindow, initial_battle_state, None)
    mainWindow.ui.setup_ui()
    mainWindow.show()

    sys.exit(app.exec_())
