#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Copyright (C) 2009 Gianni Valdambrini, Develer S.r.l (http://www.develer.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Gianni Valdambrini gvaldambrini@develer.com

"""
:copyright: 2009 Gianni Valdambrini, Develer_ S.r.l.
:author: Gianni Valdambrini
:contact: gvaldambrini@develer.com

.. _Develer: http://www.develer.com/

The directory servers contains the servers definitions used to customize the 
DevClient. Every time that the DevClient establish a connection with a server 
the list of the servers definitions (loaded at startup with the content of the 
directory) is searched in order to find a server with the proper (hostname, port).
A default server is loaded if the search failed.

Every server is a python class that can have various attributes, in order to
customize some of the processing/viewing.

The attributes list is the following:
- host, the hostname used to connect.
- port, the port used to connect.
- right_widget, the widget used to fill the right area of the client.
- cmd_password, the number of the command arrived from the server that represent
  the password.
- cmd_new_player, the command entered to create a new player.
- prompt_reg, the regular expression that identify the prompt. 
- prompt_sep, the character used to separate the max value from the current.
- wild_chars, the list of characters (used as part of a regular expression) that
  can be in a map of a wild.
- wild_end_text, the text that mark the end of a wild room (or a room, if 
  room_end_text is not defined).
- room_end_text, the text that mark the end of a room.
- room_map, the list of characters that can be in a map of a room.
- map_width, the width of the wild, in numbers of characters.
- map_height, the height of the wild, in numbers of characters.
- gui_width, the total width of the client.
"""
