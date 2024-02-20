# Copyright (c) 2024 TouchNetix
# 
# This file is part of [Project Name] and is released under the MIT License: 
# See the LICENSE file in the root directory of this project or http://opensource.org/licenses/MIT.

from axiom_tc.USB_Comms import USB_Comms

import rpyc
from rpyc.utils.server import ThreadedServer

class AxiomRPCService(rpyc.Service):
    def __init__(self):
        self.comms = USB_Comms()

    def exposed_comms_init(self, axiom):
        self.__axiom = axiom

    def exposed_read_page(self, target_address, length):
        #print(f"Read: {target_address:04X}, length: {length}")
        return self.comms.read_page(target_address, length)

    def exposed_write_page(self, target_address, length, payload):
        #print(f"Write: {target_address:04X}, length: {length}")
        self.comms.write_page(target_address, length, list(payload))
    
    def exposed_close(self):
        pass


if __name__ == '__main__': 
    server = ThreadedServer(AxiomRPCService, port=29466)
    print("Axiom RPC Server started on port 29466")
    server.start()