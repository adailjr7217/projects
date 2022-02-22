#!/usr/bin/env python
# coding: utf-8

# In[20]:


import datetime as dt

packet = input("Insert data packet:\n")
packet_list = list(packet)
lenght = "".join(packet_list[0:4])
print("Lenght:" , int(lenght, 16))
packet_id = "".join(packet_list[4:8])
print("Packet id:" , int(packet_id, 16))
none_bit = "".join(packet_list[8:10])
print("Non used bit:" , none_bit)
avl_id = "".join(packet_list[10:12])
print("AVL packet ID:" , int(avl_id,16))
imei_lenght = "".join(packet_list[12:16])
print("Imei Lenght:" , int(imei_lenght, 16))
imei_tmp = packet[16:46]
imei = []
for i in range(len(imei_tmp)):
    if i%2!=0:
        imei.append(imei_tmp[i])
    i+=1
imei = "".join(imei)
print("Imei:", imei)
codec = "".join(packet_list[46:48])
print("Codec type hex" , codec)
data_num = "".join(packet_list[48:50])
print("Number of Data records:" , int(data_num,16))
count_avl_data = 50

#Convert hex to coordinate function
def decode_hex_coord(coord):
    val = int(coord,16)
    if val  >= 2**32 / 2:
        return( (val - 2**32)/1e6)
    else :
        return(val/1e6)
    
#AVL data
#Separate id and value Io elements
def bytes_elements(id_elem):
    dict_bytes = {"Ignition":[239,1],"Movement":[240,1],"Data Mode":[80,1],"GSM Signal":[21,1],"Sleep Mode":[200,1],"GNSS Status":[69,1],"GNSS PDOP":[181,2],"GNSS HDOP":[182,2],"External Voltage":[66,2],"Speed":[24,2],"GSM Cell ID":[205,2],"GSM Area Code":[206,2],"Battery Voltage ":[67,2],"Battery Current":[68,2],"Active GSM Operator":[241,4],"Trip Odometer":[199,4],"Total Odometer":[16,4],"Digital Input 1":[1,1],"Analog Input 1":[9,2],"Digital Output 1":[179,1],"Fuel Used GPS":[12,4],"Fuel Rate GPS":[13,2],"Axis X":[17,2],"Axis Y":[18,2],"Axis Z":[19,2],"ICCID1":[11,8],"SD Status":[10,1],"Digital Input 2":[2,1],"Digital Input 3":[3,1],"Analog Input 2":[6,2],"Digital Output 2":[180,1],"Dallas Temperature 1":[72,4],"Dallas Temperature 2":[73,4],"Dallas Temperature 3":[74,4],"Dallas Temperature 4":[75,4],"Dallas Temperature ID 1":[76,8],"Dallas Temperature ID 2":[77,8],"Dallas Temperature ID 3":[79,8],"Dallas Temperature ID 4":[71,8],"iButton":[78,8],"Eco Score":[15,2],"Battery Level ":[113,1],"User ID":[238,8],"Pulse Counter Din1":[4,4],"Pulse Counter Din2":[5,4],"BT Status":[263,1],"Instant Movement":[303,1],"UL202-02 Sensor Fuel level":[327,2],"UL202-02 Sensor Status":[483,1],"Digital output 3":[380,1],"Ground Sense":[381,1],"ISO6709 Coordinates":[387,34],"UMTS/LTE Cell ID":[636,4],"Driver Name":[403,35],"Driver card license type":[404,1],"Driver Gender":[405,1],"Driver Card ID":[406,4],"Driver Card Issue Year":[407,1],"Driver Card Issue Year":[408,4],"Driver Status Event":[409,1],"Geofence zone 01":[155,1],"Geofence zone 02":[156,1],"Geofence zone 03":[157,1],"Geofence zone 04":[158,1],"Geofence zone 05":[159,1],"Geofence zone 06":[61,1],"Geofence zone 07":[62,1],"Geofence zone 08":[63,1],"Geofence zone 09":[64,1],"Geofence zone 10":[65,1],"Geofence zone 11":[70,1],"Geofence zone 12":[88,1],"Geofence zone 13":[91,1],"Geofence zone 14":[92,1],"Geofence zone 15":[93,1],"Geofence zone 16":[94,1],"Geofence zone 17":[95,1],"Geofence zone 18":[96,1],"Geofence zone 19":[97,1],"Geofence zone 20":[98,1],"Geofence zone 21":[99,1],"Geofence zone 22":[153,1],"Geofence zone 23":[154,1],"Geofence zone 24":[190,1],"Geofence zone 25":[191,1],"Geofence zone 26":[192,1],"Geofence zone 27":[193,1],"Geofence zone 28":[194,1],"Geofence zone 29":[195,1],"Geofence zone 30":[196,1],"Geofence zone 31":[197,1],"Geofence zone 32":[198,1],"Geofence zone 33":[208,1],"Geofence zone 34":[209,1],"Geofence zone 35":[216,1],"Geofence zone 36":[217,1],"Geofence zone 37":[218,1],"Geofence zone 38":[219,1],"Geofence zone 39":[220,1],"Geofence zone 40":[221,1],"Geofence zone 41":[222,1],"Geofence zone 42":[223,1],"Geofence zone 43":[224,1],"Geofence zone 44":[225,1],"Geofence zone 45":[226,1],"Geofence zone 46":[227,1],"Geofence zone 47":[228,1],"Geofence zone 48":[229,1],"Geofence zone 49":[230,1],"Geofence zone 50":[231,1],"Auto Geofence":[175,1],"Trip":[250,1],"Over Speeding":[255,1],"Idling":[251,1],"Green driving type":[253,1],"Towing":[246,1],"Unplug":[252,1],"Crash detection":[247,1],"Immobilizer":[248,1],"Green Driving Value":[254,1],"Jamming":[249,1],"ICCID2":[14,8],"Green driving event duration":[243,2],"Alarm":[236,1],"Private mode":[391,1],"Crash event counter":[317,1],"Ignition On Counter":[449,4],"VIN":[256,17],"Number of DTC":[30,1],"Engine Load":[31,1],"Coolant Temperature":[32,1],"Short Fuel Trim":[33,1],"Fuel pressure":[34,2],"Intake MAP":[35,1],"Engine RPM":[36,2],"Vehicle Speed":[37,1],"Timing Advance":[38,1],"Intake Air Temperature":[39,1],"MAF":[40,2],"Throttle Position":[41,1],"Runtime since engine start":[42,2],"Distance Traveled MIL On":[43,2],"Relative Fuel Rail Pressure":[44,2],"Direct Fuel Rail Pressure":[45,2],"Commanded EGR":[46,1],"EGR Error":[47,1],"Fuel Level":[48,1],"Distance Since Codes Clear":[49,2],"Barometic Pressure":[50,1],"Control Module Voltage":[51,2],"Absolute Load Value":[52,2],"Ambient Air Temperature":[53,1],"Time Run With MIL On":[54,2],"Time Since Codes Cleared":[55,2],"Absolute Fuel Rail Pressure":[56,2],"Hybrid battery pack life":[57,1],"Engine Oil Temperature":[58,1],"Fuel injection timing":[59,2],"Fuel Rate":[60,2],"Vehicle Speed":[81,1],"Accelerator Pedal Position":[82,1],"Fuel Consumed":[83,4],"Fuel level":[84,2],"Engine RPM":[85,2],"Total Mileage":[87,4],"Fuel level":[89,1],"Door Status":[90,2],"Program Number":[100,4],"Module ID 8B":[101,8],"Module ID 17B":[388,17],"Engine Worktime":[102,4],"Engine Worktime (counted)":[103,4],"Total Mileage (counted)":[105,4],"Fuel Consumed(counted)":[107,4],"Fuel Rate":[110,2],"AdBlue Level":[111,1],"AdBlue Level":[112,2],"Engine Load":[114,1],"Engine Temperature":[115,2],"Axle 1 Load":[118,2],"Axle 2 Load":[119,2],"Axle 3 Load":[120,2],"Axle 4 Load":[121,2],"Axle 5 Load":[122,2],"Control State Flags":[123,4],"Agricultural Machinery Flags":[124,8],"Harvesting Time":[125,4],"Area of Harvest":[126,4],"LVC of Harvest":[127,4],"Grain Mow Volume":[128,4],"Grain Moisture":[129,2],"Harvesting Drum RPM":[130,2],"Gap Under Harvesting Drum":[131,1],"Security State Flags":[132,8],"Tacho Total Distance":[133,4],"Trip Distance":[134,4],"Tacho Vehicle Speed":[135,2],"Tacho Driver Card Presence":[136,1],"Driver 1 States":[137,1],"Driver 2 States":[138,1],"Driver 1 Driving Time":[139,2],"Driver 2 Driving Time":[140,2],"Driver 1 Break Time":[141,2],"Driver 2 Break Time":[142,2],"Driver 1 Activity Duration":[143,2],"Driver 2 Activity Duration":[144,2],"Driver 1 Driving Time":[145,2],"Driver 2 Driving Time":[146,2],"Driver 1 ID High":[147,8],"Driver 1 ID Low":[148,8],"Driver 2 ID High":[149,8],"Driver 2 ID Low":[150,8],"Battery Temperature":[151,2],"Battery Level":[152,1],"DTC Faults Count":[160,1],"Slope of Arm":[161,2],"Rotation of Arm":[162,2],"Eject of Arm":[163,2],"Horizontal Distance Arm":[164,2],"Horizontal Distance Arm":[164,2],"Horizontal Distance Arm":[164,2],"Height Arm Above Ground":[165,2],"Drill RPM":[166,2],"Spread Salt":[167,2],"Battery Voltage":[168,2],"Spread Fine Grained Salt":[169,4],"Coarse Grained Salt":[170,4],"Spread DiMix":[171,4],"Spread Coarse Grained Calcium":[172,4],"Spread Calcium Chloride":[173,4],"Spread Sodium Chloride":[174,4],"Spread Magnesium Chloride":[176,4],"Amount Of Spread Gravel":[177,4],"Amount Of Spread Sand":[178,4],"Width Pouring Left":[183,2],"Width Pouring Right":[184,2],"Salt Spreader Working Hours":[185,4],"Distance During Salting":[186,4],"Load Weight":[187,4],"Retarder Load":[188,1],"Cruise Time":[189,4],"CNG status":[232,1],"CNG used":[233,4],"CNG level":[234,1],"Engine Oil Level":[235,1],"Vehicle Range on Battery":[304,4],"Vehicle Range On Additional Fuel":[305,4],"VIN":[325,17],"SecurityStateFlags_P4":[517,8],"ControlStateFlags_P4":[518,8],"IndicatorStateFlags_P4":[519,8],"AgriculturalStateFlags_P4":[520,8],"UtilityStateFlags_P4":[521,8],"CisternStateFlags_P4":[522,8],"Total LNG Used":[855,4],"Total LNG Used Counted":[856,4],"LNG Level Proc":[857,2],"LNG Level kg":[858,2],"BLE Temperature #1":[25,2],"BLE Temperature #2":[26,2],"BLE Temperature #3":[27,2],"BLE Temperature #4":[28,2],"BLE Battery #1":[29,1],"BLE Battery #2":[20,1],"BLE Battery #3":[22,1],"BLE Battery #4":[23,1],"BLE Humidity #1":[86,2],"BLE Humidity #2":[104,2],"BLE Humidity #3":[106,2],"BLE Humidity #4":[108,2],"BLE Fuel Level #1":[270,2],"BLE Fuel Level #2":[273,2],"BLE Fuel Level #3":[276,2],"BLE Fuel Level #4":[279,2],"BLE Fuel Frequency #1":[306,4],"BLE Fuel Frequency #2":[307,4],"BLE Fuel Frequency #3":[308,4],"BLE Fuel Frequency #4":[309,4],"BLE Luminosity #1":[335,2],"BLE Luminosity #2":[336,2],"BLE Luminosity #3":[337,2],"BLE Luminosity #4":[338,2],"BLE 1 Custom #2":[463,8],"BLE 1 Custom #3":[464,8],"BLE 1 Custom #4":[465,8],"BLE 1 Custom #5":[466,8],"BLE 2 Custom #2":[467,8],"BLE 2 Custom #3":[468,8],"BLE 2 Custom #4":[469,8],"BLE 2 Custom #5":[470,8],"BLE 3 Custom #2":[471,8],"BLE 3 Custom #3":[472,8],"BLE 3 Custom #4":[473,8],"BLE 3 Custom #5":[474,8],"BLE 4 Custom #2":[475,8],"BLE 4 Custom #3":[476,8],"BLE 4 Custom #4":[477,8],"BLE 4 Custom #5":[478,8]}
    dictionary_items = dict_bytes.items()
    for i, (key, value) in enumerate(dictionary_items):
            if int(id_elem,16) == value[0]:
                return value[0], key
    return "unknow"

def values_elements(id_elem, val_elem):
    dict_bytes = {"Ignition Off":[239,0],"Ignition On":[239,1],"Movement Off":[240,0],"Movement On":[240,1],"Home On Stop":[80,0],"Home On Moving":[80,1],"Roaming On Stop":[80,2],"Roaming On Moving":[80,3],"Unknown On Stop":[80,4],"Unknown On Moving":[80,5],"No Sleep":[200,0],"GPS Sleep":[200,1],"Deep Sleep":[200,2],"Online Sleep":[200,3],"Ultra Sleep":[200,4],"GNSS OFF":[69,0],"GNSS ON with fix":[69,1],"GNSS ON without fix":[69,2],"GNSS sleep":[69,3],"Trip stop":[250,0],"Trip start":[250,1],"Business Status":[250,2],"Private Status":[250,3],"Custom Statuses 1":[250,4],"Custom Statuses 2":[250,5],"Custom Statuses 3":[250,6],"Custom Statuses 4":[250,7],"Custom Statuses 5":[250,8],"Sensor 1 not ready":[75,850],"Harsh acceleration":[253,1],"Harsh braking":[253,2],"Harsh cornering":[253,3],"Jamming stop":[249,0],"Jamming start":[249,1],"Moving":[251,0],"Idling":[251,1],"Reserved":[236,0]
,"Alarm event occured":[236,1],"Battery present":[252,0],"Battery unplugged":[252,1]}
    dictionary_items = dict_bytes.items()
    for i, (key, value) in enumerate(dictionary_items):
            if int(id_elem,16) == value[0] and int(val_elem,16) == value[1] or val_elem == value[1]:
                return key
    else:
        return " "


def avl_data(packet_lst, count_avl):
    len_packet = len(packet_lst)-4
    while count_avl<len_packet:
        timestamp = "".join(packet_lst[count_avl:count_avl+16])
        timestamp = int(timestamp,16)/1000
        date_time_1 = dt.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        print("Timestamp:" , date_time_1)
        count_avl+=16
        prior = int("".join(packet_lst[count_avl:count_avl+2]))
        print("Priority:" , prior)
        count_avl+=2
        lat_hex = "".join(packet_lst[count_avl:count_avl+8])
        print("Latitude:" , decode_hex_coord(lat_hex))
        count_avl+=8
        long_hex = "".join(packet_lst[count_avl:count_avl+8])
        print("Longitude:" , decode_hex_coord(long_hex))
        count_avl+=8
        alt = int("".join(packet_lst[count_avl:count_avl+4]),16)
        print("Altitude:" , alt)
        count_avl+=4
        angle = int("".join(packet_lst[count_avl:count_avl+4]),16)
        print("Angle:" , angle)
        count_avl+=4
        sat = int("".join(packet_lst[count_avl:count_avl+2]),16)
        print("Satellites:" , sat)
        count_avl+=2
        speed = "".join(packet_lst[count_avl:count_avl+4])
        print("Speed:" , int(speed,16))
        count_avl+=4
        if codec == "8e" and len(packet_lst) > 182:
            io_id = int("".join(packet_lst[count_avl:count_avl+4]),16)
            print("Event IO Id:" , io_id)
            count_avl+=4
            total_id = int("".join(packet_lst[count_avl:count_avl+4]), 16)
            print("Element count:", total_id)
            count_avl+=4
            count_min = count_avl
            for i in [1,2,4,8]:
                count = count_min+4
                byte_num = int("".join(packet_lst[count_min:count_min+4]),16)
                byte_len = (4 + (2*i)) * byte_num
                print("Count of ", i, "bytes:", byte_num)
                count_min+=4
                count_min +=byte_len
                for j in range(byte_num):
                    elem_id = "".join(packet_lst[count:count+4])
                    elem_val = "".join(packet_lst[count+4:count+4+(2*i)])
                    count+=(2*i)+4
                    print("Parameter: {}, Value: {}".format(bytes_elements(elem_id),int(elem_val,16)), "-", values_elements(elem_id,elem_val))
            count_avl = count_min+4
            print("Xb element count:", int("".join(packet_lst[count:count+4])))

        elif codec == "08" and len(packet_lst) > 182:
            io_id = int("".join(packet_lst[count_avl:count_avl+2]),16)
            print("Event IO Id:" , io_id)
            total_id = int("".join(packet_lst[count_avl:count_avl+2]), 16)
            print("Element count:", total_id)
            count_avl+=2
            count_min = count_avl
            for i in [1,2,4,8]:
                count = count_min+2
                byte_num = int("".join(packet_lst[count_min:count_min+2]),16)
                byte_len = (2 + (2*i)) * byte_num
                print("Count of ", i, "byte(s):", byte_num)
                count_min+=2
                count_min +=byte_len
                for j in range(byte_num):
                    elem_id = "".join(packet_lst[count:count+2])
                    elem_val = "".join(packet_lst[count+2:count+2+(2*i)])
                    count+=(2*i)+2
                    print("Parameter: {}, Value: {}".format(bytes_elements(elem_id),int(elem_val,16)), "-", values_elements(elem_id,elem_val))
            count_avl = count_min+4
            print("Xb element count:", int("".join(packet_lst[count:count+4])))
        else:
            io_id = int("".join(packet_lst[98:102]),16)
            print("Event IO Id:" , io_id)
            total_id = int("".join(packet_lst[102:106]), 16)
            print("Element count:", total_id)
            return "Beacon detected"
            
            
            
avl_data(packet_list,count_avl_data)
    


# In[1]:


var = '0059cafe016e000f3335323632353639343536323530338e010000017f1dd86fb100e903402bfdbd37a4000000000000000181000100000000000000000001018100171121a877d2915b3d32cebb84e600e2b4962484b59c40c001'
print(len(var))


# In[ ]:


packet = '019acafe019a000f3335343031383131323237303536308e020000017f1304d47000e8fff96ffdba27eb0035013914001b00fd0024000f00ef0100f00100500100150500c80000450100010100b30000715201070100fb0000fd0200fc0000fe4300f900000e00b5000b00b60005004233e70018001b00cd30ea00ce36a100430f5500440000000900da000d0048001100b60012ffa100130175000f0018000400f100011ad500c700002a28001000492ed3000c00005fb40003000b000000d08046eb0400ee0000000000000000000e0000000001a83bfb00000000017f1304d85800e8fff7dffdba298c0035013c13001200fd0024000f00ef0100f00100500100150500c80000450100010100b30000715201070100fb0000fd0200fc0000fe3c00f900000e00b5000c00b60006004233a60018001200cd30ea00ce36a100430f5500440000000900da000d0048001100780012ff070013010a000f0018000400f100011ad500c700002a2f001000492eda000c00005fb40003000b000000d08046eb0400ee0000000000000000000e0000000001a83bfb000002'


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




