import time

class Channel:
    """
    Implements a simple binary channel.

    Parameters
    ----------
    latency : int
        how many seconds between each bit sent.
    """    
    
    def __init__(self, latency=2):
        self.decoder = None
        self.buffer = []
        self.working = False
        self.latency = latency
        
        
    def attach_decoder(self,decoder):
        """
        add a decoder.

        Parameters
        ----------
        decoder : int
            decoder to be used.
        """
        self.decoder = decoder
        
        
    def send_bits(self,bit):
        """
        Send one bit over the channel
        
        Parameters
        ----------
        bit : str
            bit ('0' or '1') to send.
        """
        self.buffer.append(bit)
        
        
    def transmit_bits(self, bit):
        """
        Transmit bit to the decoder
        
        Parameters
        ----------
        bit : str
            bit ('0' or '1') to send.
        """
        self.decoder.send(bit)
        
        
    def open_channel(self):
        ''' Start transmitting real-time; works until closed. '''
        self.working = True
        while self.working:
            if len(self.buffer)>0:
                self.transmit_bits(self.buffer[0])
                self.buffer = self.buffer[1:]
                time.sleep(self.latency)
                
                
    def close_channel(self):
        """
        Close the channel.
        
        Returns
        -------
        bool
            True when channel closed.
        """
        if len(self.buffer) != 0:
            return False
        self.working = False
        return True