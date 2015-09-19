__author__ = 'Jonathan Langens'

from KnowledgeDomain import KnowledgeDomain
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
@description The knowledge domain manager initializes a singleton knowledge domain
@version 0.01
"""
class KnowledgeDomainManager:

    DOMAIN = None
    """
    @post the only domain gets initialised if it did not exist before
    """
    def __init__(self):
        if KnowledgeDomainManager.DOMAIN  is None:
            KnowledgeDomainManager.DOMAIN = KnowledgeDomain("172.0.0.1")

    """
    @return the singleton domain
    """
    @classmethod
    def getDomain(self):
        return KnowledgeDomainManager.DOMAIN