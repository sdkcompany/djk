"""
 Copyright (c) 2023. Vili and contributors.

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
 """

import json
import time
import requests
import random
import socket
from helper import printer, timer
from work import randomuser


class Lookup:
    """
    Gets information about a given ip address using https://ipinfo.io/

    :param ip: The ip address to search for.
    """
    @timer.timer
    def __init__(self, ip):
        try:
            ip = socket.gethostbyname(ip)
            url = f"https://ipinfo.io/{ip}/json"
            headers = {'User-Agent': random.choice(randomuser.users)}
            url = requests.get(url, headers=headers)
            # printer.info(url.text)
            values = json.loads(url.text)

            print(f"Trying to find information for '{ip}'...")
            time.sleep(1)

            for value in values:
                # If value contains readme, skip it.
                if value == "readme":
                    continue
                elif value == "" or value is None:
                    value = "Not Found"

                print(f"{value.capitalize()} - ", values[value])

            print(f"Maps URL - ", f"https://www.google.com/maps/search/{values['loc']}")

        except Exception as e:
            print(f"Error : {e}")
            pass
