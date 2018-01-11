"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
from ..flash.flash import Flash
from ..core.coresight_target import CoreSightTarget
from ..core.memory_map import (RomRegion, FlashRegion, RamRegion, MemoryMap)
import logging
from time import sleep

class Flash_rtl8195am(Flash):

    def __init__(self, target):
        return

class RTL8195AM(CoreSightTarget):

    memoryMap = MemoryMap(
        RomRegion(      start=0x00000000,  length=0x100000),
        RamRegion(      start=0x10000000,  length=0x70000),
        RamRegion(      start=0x1FFF0000,  length=0x10000),
        RamRegion(      start=0x30000000,  length=0x200000),
        RamRegion(      start=0x40000000,  length=0x400000)
        )

    def __init__(self, link):
        logging.debug('rtl8195am __init__')
        super(RTL8195AM, self).__init__(link, self.memoryMap)

    def init(self):
        logging.debug('rtl8195am init')
        super(RTL8195AM, self).init()

    def resetStopOnReset(self, software_reset=None, map_to_user=True):
        logging.debug('rtl8195am resetStopOnReset')
        super(RTL8195AM, self).resetStopOnReset()
        
        # Init system
        sleep(0.02)
        self.writeMemory(0x40000014, 0x00000021)
        sleep(0.01)
        self.writeMemory(0x40000304, 0x1fc00002)
        sleep(0.01)
        self.writeMemory(0x40000250, 0x00000400)
        sleep(0.01)
        self.writeMemory(0x40000340, 0x00000000)
        sleep(0.01)
        self.writeMemory(0x40000230, 0x0000dcc4)
        sleep(0.01)
        self.writeMemory(0x40000210, 0x00011117)
        sleep(0.01)
        self.writeMemory(0x40000210, 0x00011157)
        sleep(0.01)
        self.writeMemory(0x400002c0, 0x00110011)
        sleep(0.01)
        self.writeMemory(0x40000320, 0xffffffff)
        sleep(0.01)
        # Init DRAM
        self.writeMemory(0x40000040, 0x00fcc702)
        logging.debug('rtl8195am 0x%08x=0x%08x', 0x40000040, self.readMemory(0x40000040))
        self.writeMemory(0x40005224, 0x00000001)
        sleep(0.01)
        self.writeMemory(0x40005004, 0x00000208)
        sleep(0.01)
        self.writeMemory(0x40005008, 0xffffd000)
        sleep(0.013)
        self.writeMemory(0x40005020, 0x00000022)
        sleep(0.013)
        self.writeMemory(0x40005010, 0x09006201)
        sleep(0.013)
        self.writeMemory(0x40005014, 0x00002611)
        sleep(0.013)
        self.writeMemory(0x40005018, 0x00068413)
        sleep(0.013)
        self.writeMemory(0x4000501c, 0x00000042)
        sleep(0.013)
        self.writeMemory(0x4000500c, 0x700)
        sleep(0.02)
        self.writeMemory(0x40005000, 0x1)
        sleep(0.3)
        logging.debug('rtl8195am 0x%08x=0x%08x', 0x40005000, self.readMemory(0x40005000))
        self.writeMemory(0x4000500c, 0x600)
        sleep(0.3)
        self.writeMemory(0x40005008, 0x00000000)
        sleep(0.01)
        self.writeMemory(0x40000300, 0x0006005e)
        sleep(0.01)
        self.writeMemory(0x40000210, 0x8011157)
        logging.debug('rtl8195am 0x%08x=0x%08x', 0x40000210, self.readMemory(0x40000210))
        


