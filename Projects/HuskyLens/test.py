#!/usr/bin/env python3

import time
import huskylib
import json

test = huskylib.HuskyLensLibrary("SERIAL", "/dev/ttyUSB0", 3000000)
# test = huskylib.HuskyLensLibrary("I2C","",address=0x32)

try:
    print("First request a knock: {}".format(test.knock()))
except:
    print("Failed to find HuskyLens at I2C address 0x32")
    exit(1)


# testcmd = "55AA11002C"
# testcksum = test.calculateChecksum(testcmd)
# print("cksum for {} is {}".format(testcmd,testcksum))

def print_menu():
    print("""
        Menu options:
        0) algorithm() ***format 0 ALG_VAL***
           0 = ALGORITHM_FACE_RECOGNITION
           1 = ALGORITHM_OBJECT_TRACKING
           2 = ALGORITHM_OBJECT_RECOGNITION
           3 = ALGORITHM_LINE_TRACKING
           4 = ALGORITHM_COLOR_RECOGNITION
           5 = ALGORITHM_TAG_RECOGNITION
           6 = ALGORITHM_OBJECT_CLASSIFICATION
           7 = ALGORITHM_QR_CODE_RECOGNITION (not in 0.5.1norm)
           8 = ALGORITHM_BARCODE_RECOGNITION (not in 0.5.1norm)

        1) requestAll()
        2) blocks() (cntrl-c to stop loop)
        3) arrows()
        4) learned()
        5) blocks_learned()
        6) arrows_learned()
        7) by_id() ***format 7 ID_VAL***
        8) blocks_by_id() ***format 8 ID_VAL***
        9) arrows_by_id() ***format 9 ID_VAL***
        10) Exit (or Cntrl-C)


        47) learn()   ***format 47 ID_VAL***
        48) forget()  
        """)

def printObjectNicely(obj):
    count=1

    print("printObjectNicely({}):".format(type(obj)))
    if(type(obj)==list):
        print("len(obj):",len(obj))
        for i in obj:
            print("\t "+ ("BLOCK_" if i.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(i.__dict__))
            count+=1
    else:
        print("\t "+ ("BLOCK_" if obj.type=="BLOCK" else "ARROW_")+str(count)+" : "+ json.dumps(obj.__dict__))

def print_blocks(blks):
    for blk in blks:
        print("center (x,y): ({:>3},{:>3}) width: {:>3} height: {:>3} ID: {:>2}".format(blk[0],blk[1],blk[2],blk[3],blk[4]))
    print("\n")

def print_arrows(arrows):
    for arrows in arrows:
        print("origin (x,y): ({:>3},{:>3}) target (x,y): ({:>3},{:>3}) ID: {:>2}".format(arrow[0],arrow[1],arrow[2],arrow[3],arrow[4
]))
    print("\n")

# reverse the ID_by_algorithm dictionary to allow algorithm lookup by ID
algorithmsByValue = {v: k for k, v in huskylib.algorithmsByteID.items()}
ex=1

try:
    while(ex==1):
        print_menu()
        v=input("Enter cmd number:")
        numEnter=v
        if(numEnter=="10"):
            ex=0
        vsplit = v.split()
        # print("vsplit:",vsplit)
        v=int(vsplit[0])
        if(v==0):
            try:
                f_alg = "{:04x}".format(int(numEnter[2:]))
                f_alg = f_alg[2:]+f_alg[0:2]
                if f_alg in algorithmsByValue:
                    alg_str = algorithmsByValue[f_alg]
                    print("Requesting {} mode".format(alg_str))
                    print(test.algorithm(alg_str))
                else:
                    print("{} not valid algorithm".format(numEnter[2:]))
            except Exception as e:
                print("Exception {}".format(str(e)))

        elif(v==1):
            print("requestAll():")
            req = test.requestAll()
            printObjectNicely(req)

        elif(v==2):
            print("blocks(): press cntrl-c to stop")
            while True:
                try:
                    blks = test.blocks()
                    # print_blocks(blks)
                    printObjectNicely(blks)
                    time.sleep(1)
                except KeyboardInterrupt:
                    print(" Exiting blocks()\n")
                    break
        elif(v==3):
            print("arrows(): press cntrl-c to stop")
            # print(test.arrows())
            while True:
                try:
                    arrows = test.arrows()
                    # print_arrows(arrows)
                    printObjectNicely(arrows)
                    time.sleep(1)
                except KeyboardInterrupt:
                    print(" Exiting arrows()\n")
                    break
        elif(v==4):
            print("learned():")
            lrnd = test.learned()
            # for id in lrnd:
            #     print(id)
            printObjectNicely(lrnd)

        elif(v==5):
            print("learnedBlocks():")
            blks = test.learnedBlocks()
            # print_blocks(blks)
            printObjectNicely(blks)

        elif(v==6):
            print("arrows_learned():")
            arrows = test.arrows_learned()
            print_arrows(arrows)
        elif(v==7):
            print("by_id({})".format(int(vsplit[1])))
            ids = test.by_id(int(numEnter[2:]))
            for id in ids:
                print(id)
        elif(v==8):
            print("blocks_by_id({})".format(int(vsplit[1])))
            blks = test.blocks_by_id(int(numEnter[2:]))
            print_blocks(blks)
        elif(v==9):
            print("arrows_by_id({})".format(int(vsplit[1])))
            arrows = test.arrows_by_id(int(numEnter[2:]))
            print_arrows(arrows)
        elif(v==47):
            print("requesting learn id={}".format(int(vsplit[1])))
            print(test.learn(int(numEnter[3:])))
        elif(v==48):
            print("requesting forget")
            print(test.forget())

except KeyboardInterrupt:
    print("\nCtrl-C Detected: Exiting")
except Exception as e:
    print("Exception: {}".format(str(e)))

