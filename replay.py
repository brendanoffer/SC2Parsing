#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, re

# import termios
# import fcntl

import sc2reader
from sc2reader.events import *
from sc2reader.plugins.replay import APMTracker, SelectionTracker
sc2reader.register_plugin('Replay',APMTracker())
sc2reader.register_plugin('Replay',SelectionTracker())

def myGetch():
    sys.stdin.read(1)

def get_args():
    import argparse

    parser = argparse.ArgumentParser(
        description="""Step by step replay of game events; shows only the
        Initialization, Ability, and Selection events by default. Press any
        key to advance through the events in sequential order.""",
        epilog="And that's all folks")

    parser.add_argument('paths', metavar='filename', type=str, nargs='+',
        help="Paths to one or more SC2Replay files or directories")
    parser.add_argument('--player',default=0, type=int,
        help="The number of the player you would like to watch. Defaults to 0 (All).")
    parser.add_argument('--bytes',default=False,action="store_true",
        help="Displays the byte code of the event in hex after each event.")
    parser.add_argument('--hotkeys',default=False,action="store_true",
        help="Shows the hotkey events in the event stream.")
    parser.add_argument('--cameras',default=False,action="store_true",
        help="Shows the camera events in the event stream.")

    return parser.parse_args()

def main(): 
    args = get_args()
    
    for path in args.paths:
        counter = int(0)
        depth = -1
        for filepath in sc2reader.utils.get_files(path, depth=depth):
            sys.stdout = sys.__stdout__
            counter+=1
            print "Processing file #: {0}".format(counter)
            name, ext = os.path.splitext(filepath)
            replay = sc2reader.load_replay(filepath,debug=True)
            filenamesave = str(name) + ".txt"
            sys.stdout = open(filenamesave, 'w')
            print replay.release_string
            print replay.map_name
            for player in replay.players:
                 print player.name
                 print player.result
                 print player.pick_race[0]
                 print int(round(player.avg_apm))
                 print str(replay.length).replace('.',':')
            print "\n--------------------------\n\n"

        # Allow picking of the player to 'watch'
            if args.player:
                events = replay.player[args.player].events
            else:
                events = replay.events

        # Loop through the events
        #data = sc2reader.config.build_data[replay.build]
            for event in events:
                 try:
                     pass
                    #event.apply(data)
                 except ValueError as e:
                     if str(e) == "Using invalid abilitiy matchup.":
                         myGetch()
                     else:
                         raise e

            # Use their options to filter the event stream

                 if isinstance(event,AbilityEvent) or\
                            isinstance(event,SelectionEvent) or\
                            isinstance(event,PlayerJoinEvent) or\
                            isinstance(event, PlayerLeaveEvent) or\
                            isinstance(event,GameStartEvent) or\
                            (args.hotkeys and isinstance(event,HotkeyEvent)) or\
                            (args.cameras and isinstance(event,CameraEvent)):
                     '''
                     if isinstance(event, SelectionEvent) or isinstance(event, HotkeyEvent):
                     '''
                     eventcheck = str(event)
                     if ('Build' in eventcheck) or ('MorphOverlord' in eventcheck):
                        if ('BuildCreepTumor' not in eventcheck) and ('Cancel' not in eventcheck) and ('Halt' not in eventcheck) and ('BuildNuke' not in eventcheck) and ('BuildThor' not in eventcheck) and ('BuildBattleHellion' not in eventcheck) and ('BuildSiegeTank' not in eventcheck) and ('BuildWidowMine' not in eventcheck) and ('BuildInterceptor' not in eventcheck) and ('BuildHellion' not in eventcheck):
                            print str(event)
                        # print event
                        #myGetch()
                     if args.bytes:
                        print "\t"+event.bytes.encode('hex')
                     if re.search('UNKNOWN|ERROR', str(event)):
                         myGetch()



if __name__ == '__main__':
    main()
