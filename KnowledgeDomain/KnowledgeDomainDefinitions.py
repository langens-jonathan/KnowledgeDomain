__author__ = 'Jonathan Langens'
"""
Copyright (C) 2015  Langens Jonathan

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""
"""
@author Jonathan Langens
@description this class presents all constants the knowledge domain uses
"""
class KnowledgeDomainDefinitions:
    # types
    TEXT = "text" # all textual data, also serves as the 'base' type
    NUMERIC = "numeric" # all numbers etc
    TIME = "time" # a time is a point in time, this is the 'default' time related type
    DATE = "date" # a date
    LOCATION = "location" # a location in the world