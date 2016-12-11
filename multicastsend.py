#!/usr/bin/env python3.5

import vlc
import sys
import time

if __name__ == "__main__":
    # streaming 
    fileurl = 'file://[full path to file]'

    instance = vlc.Instance()
    player = instance.media_player_new()

    cmd = [videourl]

    stream = 'sout=#rtp{access=udp,mux=ts,dst=239.255.12.42,port=5004,sap,group="Video",name=SlowTV"}' 
    cmd.append(stream)

    cmd.append(':sout-all')

    media = instance.media_new(*cmd)
    media.get_mrl()
    player.set_media(media)

    player.play()

    while True:
        time.sleep(10)

        state = player.get_state()
        pos = player.get_position()
        print(" state: {} position: {}".format(state, pos))
