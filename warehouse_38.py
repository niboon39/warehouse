import codecs
import os
from collections import OrderedDict

file_input = 'input.txt'

class World: # BaseClass

    def __init__(self):

        self.named_harbor = []
        self.named_airport = []
        self.named_train_Station = []

        self.named_warehouse = []
        self.Station_start = []
        self.Station_end = []
        self.Station_dist = []
        self.orders = []
        self.slots = []

        self.named_truck = []
        self.items_1 = []
        self.items_2 = []

        self.named_item_name = []
        self.min_temp = []
        self.max_temp = []
        self.weight = []

        # List of countries
        # Airport
        self.First_airport = ['USA', 'UK', 'Italy']
        self.Second_airport = ['Wakanda', 'Germany', 'USSR']
        self.Third_airport = ['Brazil', 'Argentina', 'Ireland']

        # Harbor
        self.First_harbor = ['India', 'Indonesia', 'Hong Kong']
        self.Second_harbor = ['Philipine', 'Singapore', 'Sri Lanka']
        self.Third_harbor = ['Egypt', 'Congo', 'Madagasgar']

        # Train station
        self.First_train_station = ['Vietnam', 'China', 'Laos']
        self.Second_train_station = ['Hungary', 'Austria', 'Myanmar']
        self.Third_train_station = ['Bulgaria', 'Poland', 'Latvia']


class Harbor(World):

    def Add_harbor(self, name = ""):
        self.named_harbor.append(name[1:-1])

    def Show_harbor(self):
        print("----- Information Harbor -----")
        for i in range(len(self.named_harbor)):
            print("Harbor : {}".format(self.named_harbor[i]))

    def __del__(self):
        self.named_harbor.clear()

class Warehouse(World): # DerivedClass inherit World

    def Add_warehouse(self, name = "", order = 0, slot = 0):
        self.named_warehouse.append(name[1:-1])
        self.orders.append(order)
        self.slots.append(slot)

    def Set_distance(self, start_station = "", end_station = "", dist = 0):
        self.Station_start.append(start_station)
        self.Station_end.append(end_station)
        self.Station_dist.append(dist)

    def Show_infomation(self):
        print("----- Information Warehouse -----")
        for i in range(len(self.named_warehouse)):
            print("named : {} , orders : {} , slots = {}".format(self.named_warehouse[i], self.orders[i], self.slots[i]))

    def Show_distance(self):
        print("----- Distance Warehouse -----")
        for i in range(len(self.Station_start)):
            print("{} - {} , Distance = {}".format(self.Station_start[i], self.Station_end[i], self.Station_dist[i]))

    def __del__(self):
        self.named_warehouse.clear()
        self.orders.clear()
        self.slots.clear()

class Truck(World):

    def Add_truck(self, name = "", item_1 = 0, item_2 = 0):
        self.named_truck.append(name[1:-1])
        self.items_1.append(item_1)
        self.items_2.append(item_2)

    def Show_truck(self):
        print("----- Information Truck -----")
        for i in range(len(self.named_truck)):
            print("Truck : {} , Item 1 : {} , Item 2 : {}".format(self.named_truck[i], self.items_1[i], self.items_2[i]))

    def __del__(self):
        self.named_truck.clear()
        self.items_1.clear()
        self.items_2.clear()

class Airport(World):

    def Add_airport(self, name = ""):
        self.named_airport.append(name[1:-1])

    def Show_airport(self):
        print("----- Information Airport -----")
        for i in range(len(self.named_airport)):
            print("Airport : {}".format(self.named_airport[i]))

    def __del__(self):
        self.named_airport.clear()

class Train_Station(World):

    def Add_train_station(self, name = ""):
        self.named_train_Station.append(name[1:-1])

    def Show_train_station(self):
        print("----- Information Train_Station -----")
        for i in range(len(self.named_train_Station)):
            print("Train_Station : {}".format(self.named_train_Station[i]))

    def __del__(self):
        self.named_train_Station.clear()

class Create_item(World):

    def Add_create_item(self, name = "", stored_1 = 0, stored_2 = 0, weight = 0):
        self.named_item_name.append(name[1:-1])
        self.min_temp.append(stored_1)
        self.max_temp.append(stored_2)
        self.weight.append(weight)

    def Show_create_item(self):
        print("----- Information Item -----")
        for i in range(len(self.named_item_name)):
            print("Item name : {} , min temp : {} , max temp : {} , weight : {}".format(self.named_item_name[i], self.min_temp[i], self.max_temp[i], self.weight[i]))

    def __del__(self):
        self.named_item_name.clear()
        self.min_temp.clear()
        self.max_temp.clear()

def check_create_item(item):
    R = False
    f = codecs.open(file_input, 'r', encoding='utf-8')
    for line in f:
        if (line.find('Create_item') != -1 and item in line):
            R = True
            break
        else:
            R = False
            '''
            A = line.split(' ')
            create_item = A[1]
            item = item.strip()
            if(item in create_item):
                R = True
                break
            else:
                R = False
            '''
    return R

def check_existing_harbor_ariport_train(T):
    R = False
    w = World()
    for i in w.First_airport:
        if(T == i):
            R = True
            break
    for i in w.Second_airport:
        if(T == i):
            R = True
            break
    for i in w.Third_airport:
        if(T == i):
            R = True
            break

    for i in w.First_harbor:
        if(T == i):
            R = True
            break
    for i in w.Second_harbor:
        if(T == i):
            R = True
            break
    for i in w.Third_harbor:
        if(T == i):
            R = True
            break

    for i in w.First_train_station:
        if(T == i):
            R = True
            break
    for i in w.Second_train_station:
        if(T == i):
            R = True
            break
    for i in w.Third_train_station:
        if(T == i):
            R = True
            break
    return R

def check_index_harbor_ariport_train(T):
    txt = ''
    ind = 0
    w = World()
    for i in w.First_airport:
        if(T == i):
            ind = 0
            txt = 'Airport'
            break
    for i in w.Second_airport:
        if(T == i):
            ind = 1
            txt = 'Airport'
            break
    for i in w.Third_airport:
        if(T == i):
            ind = 2
            txt = 'Airport'
            break

    for i in w.First_harbor:
        if(T == i):
            ind = 0
            txt = 'Harbor'
            break
    for i in w.Second_harbor:
        if(T == i):
            ind = 1
            txt = 'Harbor'
            break
    for i in w.Third_harbor:
        if(T == i):
            ind = 2
            txt = 'Harbor'
            break

    for i in w.First_train_station:
        if(T == i):
            ind = 0
            txt = 'Train_Station'
            break
    for i in w.Second_train_station:
        if(T == i):
            ind = 1
            txt = 'Train_Station'
            break
    for i in w.Third_train_station:
        if(T == i):
            ind = 2
            txt = 'Train_Station'
            break
    return ind, txt

def check_warehouse(warehouse):
    R = False
    f = codecs.open(file_input, 'r', encoding='utf-8')
    for line in f:
        if (line.find('Create Warehouse') != -1):
            A = line.split(' ')
            Create_Warehouse = A[2]
            warehouse = warehouse.strip()
            if(warehouse in Create_Warehouse):
                R = True
                break
            else:
                R = False
    return R

def check_warehouse_temp(To, Item, Amount):
    R = False
    Temp_warehouse = 0
    Slot_warehouse = 0
    product = 0
    f = codecs.open(file_input, 'r', encoding='utf-8')
    for line in f:
        if (line.find('Create Warehouse') != -1):
            A = line.split(' ')
            Create_Warehouse = A[2]
            if(To in Create_Warehouse):
                Temp_warehouse = A[3].replace('(', '').strip()
                Temp_warehouse = float(Temp_warehouse.replace(',', '').strip())
                Slot_warehouse = A[4].replace(')', '').strip()
                Slot_warehouse = int(Slot_warehouse.replace(',', '').strip())
                break

    f2 = codecs.open(file_input, 'r', encoding='utf-8')
    for line2 in f2:
        if (line2.find('Create_item') != -1 and Item in line2):
            A = line2.split('(')
            B = A[1].split(',')
            min_temp = float(B[0])
            max_temp = float(B[1])
            if (Temp_warehouse >= min_temp and Temp_warehouse <= max_temp and Slot_warehouse >= int(Amount)):
                R = True
                break
            else:
                R = False
                break
            '''
            A = line2.split(' ')
            create_item = A[1]
            if(Item in create_item):
                A = line2.split('(')
                B = A[1].split(',')
                min_temp = float(B[0])
                max_temp = float(B[1])
                if(Temp_warehouse >= min_temp and Temp_warehouse <= max_temp and Slot_warehouse >= int(Amount)):
                    R = True
                    break
                else:
                    R = False
                    break
            '''
    return R

def check_truck(Item, Amount):
    R = False
    load_item = 0
    f = codecs.open(file_input, 'r', encoding='utf-8')
    for line in f:
        if (line.find('Create_item') != -1):
            A = line.split(' ')
            create_item = A[1].strip()
            Item = Item.strip()
            if(Item in create_item):
                S = float(A[4].replace(')', '').replace(',', '').strip())
                Amount = int(Amount)
                load_item = S * Amount
                break

    ITEM1 = 0
    ITEM2 = 0
    W = ''
    f2 = codecs.open(file_input, 'r', encoding='utf-8')
    for line2 in f2:
        if (line2.find('Create Truck') != -1):
            SPLIT_1 = line2.rstrip().split('(')
            SPLIT_2 = SPLIT_1[0].split(' ')
            if (len(SPLIT_2) >= 4):
                W = SPLIT_2[2] + " " + SPLIT_2[3]
            else:
                W = SPLIT_2[2]

            SPLIT_3 = SPLIT_1[1].split(',')
            ITEM1 = SPLIT_3[0].strip()
            ITEM2 = SPLIT_3[1].replace(')','').strip()

        if(load_item >= int(ITEM1) and load_item <= int(ITEM2)):
            R = True
            break
        else:
            W = 'Reject'

    return R, W

# Depth-First Search Path
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

if __name__ == "__main__":

    # Create Instance class
    wh = Warehouse()
    hb = Harbor()
    ap = Airport()
    tc = Truck()
    tr = Train_Station()
    ci = Create_item()
    All_station = []
    All_warehouse = []
    All_truck = []

    # Read input text file
    file_name = file_input
    f = codecs.open(file_name, 'r', encoding='utf-8')
    for line in f:

        if(line.find('Create Harbor') != -1): # Create Harbor

            SPLIT_1 = line.rstrip().split(' ')
            if(len(SPLIT_1) >= 4):
                NAME = SPLIT_1[2] + " " + SPLIT_1[3]
                hb.Add_harbor(NAME)
            else:
                NAME = SPLIT_1[2]
                hb.Add_harbor(NAME)
            All_station.append(NAME)

        elif(line.find('Create Airport') != -1): # Create Airport

            SPLIT_1 = line.rstrip().split(' ')
            if(len(SPLIT_1) >= 4):
                NAME = SPLIT_1[2] + " " + SPLIT_1[3]
                ap.Add_airport(NAME)
            else:
                NAME = SPLIT_1[2]
                ap.Add_airport(NAME)
            All_station.append(NAME)

        elif(line.find('Create Warehouse') != -1): # Create Warehouse

            SPLIT_1 = line.rstrip().split('(')
            SPLIT_2 = SPLIT_1[0].split(' ')
            if(len(SPLIT_2) >= 4):
                W = SPLIT_2[2] + " " + SPLIT_2[3]
            else:
                W = SPLIT_2[2]

            SPLIT_3 = SPLIT_1[1].split(',')
            ORDER = SPLIT_3[0].strip()
            SLOT = SPLIT_3[1].strip()

            wh.Add_warehouse(W, ORDER, SLOT.replace(')', '').strip())
            All_warehouse.append(W)

        elif(line.find('Create Truck') != -1): # Create Truck

            SPLIT_1 = line.rstrip().split('(')
            SPLIT_2 = SPLIT_1[0].split(' ')
            if(len(SPLIT_2) >= 4):
                W = SPLIT_2[2] + " " + SPLIT_2[3]
            else:
                W = SPLIT_2[2]

            SPLIT_3 = SPLIT_1[1].split(',')
            ITEM1 = SPLIT_3[0].strip()
            ITEM2 = SPLIT_3[1].replace(')','').strip()

            tc.Add_truck(W, ITEM1, ITEM2.replace(')', '').strip())
            All_truck.append(W)

        elif(line.find('Create Train_Station') != -1): # Create Train_Station

            SPLIT_1 = line.rstrip().split(' ')
            if(len(SPLIT_1) >= 4):
                NAME = SPLIT_1[2] + " " + SPLIT_1[3]
                tr.Add_train_station(NAME)
            else:
                NAME = SPLIT_1[2]
                tr.Add_train_station(NAME)
            All_station.append(NAME)

        elif(line.find('Set_path') != -1): # Set_path

            SPLIT_1 = line.rstrip().split(' ')
            if(len(SPLIT_1) == 5):
                A = SPLIT_1[1]
                B = SPLIT_1[2] + ' ' + SPLIT_1[3]
                C = SPLIT_1[4]
                wh.Set_distance(A, B, C)
            else:
                A = SPLIT_1[1]
                B = SPLIT_1[2]
                C = SPLIT_1[3]
                wh.Set_distance(A, B, C)

        elif (line.find('Create_item') != -1): # Create_item

            SPLIT_1 = line.rstrip().split('(')
            SPLIT_2 = SPLIT_1[0].split(' ')
            if(len(SPLIT_2) >= 4):
                W = SPLIT_2[1] + " " + SPLIT_2[2]
            else:
                W = SPLIT_2[1]

            SPLIT_3 = SPLIT_1[1].split(',')
            MIN_TEMP = SPLIT_3[0].strip()
            MAX_TEMP = SPLIT_3[1].strip()
            WEIGHT = SPLIT_3[2].strip()

            ci.Add_create_item(W, MIN_TEMP, MAX_TEMP, WEIGHT.replace(')', '').strip())

    hb.Show_harbor()
    ap.Show_airport()
    wh.Show_infomation()
    wh.Show_distance()
    tc.Show_truck()
    tr.Show_train_station()
    ci.Show_create_item()

    # ------- Transection -------

    Warehouse_temp = False
    Loaded = False
    location = ''
    T_truck = {}
    T_warehouse_slot = {}
    Each_slot_warehouse = {}
    Each_warehouse_name = {}
    Each_truck_dist = {}
    Have_import = {}
    Have_export = {}

    LOG = ''

    # Clear old files
    for r, d, f in os.walk('order//'):
        for file in f:
            os.remove('order//' + file)

    # Find capacity of slot each warehouse
    cs = 0
    with codecs.open(file_input, 'r', encoding='utf-8') as f_find_slot:
        for line_find_slot in f_find_slot:
            if (line_find_slot.find('Create Warehouse') != -1):

                SPLIT_1 = line_find_slot.rstrip().split('(')
                SPLIT_2 = SPLIT_1[0].split(' ')
                W = SPLIT_2[2][1:-1]

                SPLIT_3 = SPLIT_1[1].split(',')
                ORDER = SPLIT_3[0].strip()
                SLOT = SPLIT_3[1].strip()

                Each_slot_warehouse[W] = SLOT.replace(')','')
                Each_warehouse_name[cs] = W
                cs += 1


    # Seperate order
    ind = 0
    num_order = 0
    DO = False
    file_name = file_input
    f = codecs.open(file_name, 'r', encoding='utf-8')
    for line in f:

        if(line.find('Order') != -1):

            DO = True
            num_order = line.rstrip()

        elif(DO == True):

            ind += 1
            file = 'order//' + str(ind) + '_' + num_order.replace(':', '').strip().replace(' ', '_')  + '.txt'
            with open(file, 'a+') as fs:

                DO = False
                file_name = file_input
                f3 = codecs.open(file_name, 'r', encoding='utf-8')
                for line3 in f3:

                    if (line3.find(num_order) != -1):

                        DO = True

                    elif (DO == True):

                        if (line3.find(':') != -1):
                            DO = False
                            break

                        fs.write(line3)

            DO = False

    f.close()

    # Process
    print('\n')
    for r, d, f in os.walk('order//'):
        for file in f:

            Process_count = 0
            Success_count = 0
            Fail_count = 0
            tmp_log = ''

            ST = file.split('_')
            ST2 = ST[2].split('.')
            LOG += ST[1] + ' ' + ST2[0] + ':' + '\r\n'

            with codecs.open('order//' + file, 'r', encoding='utf-8') as f2:
                for line2 in f2:

                    dist = 0

                    if (line2.find('Export') != -1): # Export

                        Process_count += 1
                        START = 0
                        END = 0

                        A = line2.strip().split(' ')
                        if(len(A) > 7):
                            Amount = A[1]
                            Item = A[2]
                            From = A[4] + ' ' + A[5]
                            To = A[7]
                        else:
                            Amount = A[1]
                            Item = A[2]
                            From = A[4]
                            To = A[6]

                        Existing_item = False
                        Ad = check_create_item(Item)
                        Bd = check_warehouse(From)
                        [Ind, txt] = check_index_harbor_ariport_train(To)
                        if (Ad and Bd and txt != ''):
                            Existing_item = True
                        else:
                            Existing_item = False

                        [Loaded, Truck] = check_truck(Item, Amount)

                        Pick_up_product = ''
                        if(txt == 'Harbor'):
                            Pick_up_product = hb.named_harbor[Ind]
                        elif(txt == 'Airport'):
                            Pick_up_product = ap.named_airport[Ind]
                        elif(txt == 'Train_Station'):
                            Pick_up_product = tr.named_train_Station[Ind]

                        # check product (such as lightsaber)
                        RU = False
                        for key, val in T_warehouse_slot.items():
                            if(key == From):
                                for t in val:
                                    if(t == Item):
                                        RU = True
                                        break

                        if(RU == False):

                            Fail_count += 1

                            # Add slot
                            T_warehouse_slot[To] = []

                            print(file)
                            tmp_log = A[0] + ' ' + A[1] + ' - Failed'
                            print(location + ' -> ' + To)
                            print('Truck name : {}'.format(Truck))
                            print(tmp_log)
                            print('Total distance : {}'.format(dist))
                            print('Location : {}'.format(location))
                            T_truck[Truck] = location
                            print('------')

                        else:

                            # log import
                            strw = []
                            for i in range(int(Amount)):
                                strw.append(Item)
                            if ((To in Have_export) == False):
                                Have_export[Pick_up_product] = []
                            Have_export[Pick_up_product] += strw

                            cm = 0
                            for ty in range(len(All_station)):
                                if Pick_up_product in All_station[ty]:
                                    All_station.pop(ty)
                                    break
                                else:
                                    Have_import[All_station[ty][1:-1]] = []
                                cm += 1

                            # Update slot
                            for i in range(int(Amount)):
                                T_warehouse_slot[From].pop()

                            # Find start airport & harbor location
                            S = False
                            txt = []
                            Concerned_path = []

                            # Depth-First Search Path
                            num = [x for x in range(1, 1000)]
                            c = 1
                            Dict_dfs = {}
                            RE = []
                            MS = []
                            with codecs.open(file_input, 'r', encoding='utf-8') as f_dfs:
                                for line_dfs in f_dfs:
                                    if(line_dfs.find('Set_path') != -1):
                                        SPLIT_1 = line_dfs.rstrip().split(' ')
                                        if (len(SPLIT_1) == 5):
                                            A = SPLIT_1[1]
                                            B = SPLIT_1[2] + ' ' + SPLIT_1[3]
                                            C = SPLIT_1[4]
                                            RE.append(A)
                                            RE.append(B)
                                            MS += [[A, B]]
                                        else:
                                            A = SPLIT_1[1]
                                            B = SPLIT_1[2]
                                            C = SPLIT_1[3]
                                            RE.append(A)
                                            RE.append(B)
                                            MS += [[A, B]]
                                    c += 1

                            RE = list(OrderedDict.fromkeys(RE))
                            RE2 = num[:len(RE)]

                            cm = 0
                            for o in range(len(MS)):
                                SE = MS[o]
                                for o2 in range(len(SE)):
                                    for o3 in range(len(RE)):
                                        if(SE[o2] == RE[o3]):
                                            SE[o2] = o3 + 1
                                MS[o] = SE

                            Tx = {}
                            for i in range(len(RE2)):
                                d = RE2[i]
                                Tx[d] = []
                                for j in range(len(MS)):
                                    e = MS[j]
                                    if (d in e):
                                        if (e[0] != d):
                                            Tx[d] += str(e[0])
                                        elif (e[1] != d):
                                            Tx[d] += str(e[1])

                            XP = {}
                            for ko in range(len(RE)):
                                if((str(ko + 1) in XP) == False):
                                    XP[str(ko + 1)] = []
                                XP[str(ko + 1)] = set(Tx[ko + 1])

                            graph = XP

                            # A = Naboo , B = Coruscant , C = Tatooine , D = Galactic City , E = Gungan , F = Tomas
                            Weight = []

                            for mm in range(len(RE)):
                                if(RE[mm] == From):
                                    START = mm + 1

                            for mm in range(len(RE)):
                                if (RE[mm] == Pick_up_product):
                                    END = mm + 1

                            # Path From - To
                            R_path = list(dfs_paths(graph, str(START), str(END)))
                            X = ''
                            Y = ''

                            DICT = {}
                            for jk in range(len(RE)):
                                DICT[jk + 1] = RE[jk]

                            #DICT = {'A':'Naboo' , 'B':'Coruscant' , 'C':'Tatooine' , 'D':'Galactic City' , 'E':'Gungan' , 'F':'Tomas'}
                            S = R_path[0]
                            Map = []
                            for u in range(len(S) - 1):
                                for key, val in DICT.items():
                                    if(key == int(S[u])):
                                        X = val
                                    if(key == int(S[u + 1])):
                                        Y = val
                                Map.append(X + ' ' + Y)

                            # Weight
                            for u in range(len(Map)):
                                with codecs.open(file_input, 'r', encoding='utf-8') as f_map:
                                    for line_map in f_map:
                                        if (line_map.find('Set_path') != -1):
                                            Q = Map[u].split(' ')
                                            R = 0
                                            for j in range(len(Q)):
                                                if(Q[j] in line_map):
                                                    R += 1
                                            if(R == len(Q)):
                                                Weight.append(line_map.split(' ')[-1].strip())


                            for mm in range(len(RE)):
                                if(RE[mm] == Start_truck):
                                    Truck_location = mm + 1

                            R_path_truck = list(dfs_paths(graph, str(Truck_location), str(START)))
                            X_truck = ''
                            Y_truck = ''
                            DICT_truck = DICT
                            S_truck = R_path_truck[0]
                            Map_truck = []
                            for u in range(len(S_truck) - 1):
                                for key, val in DICT_truck.items():
                                    if(key == int(S_truck[u])):
                                        X_truck = val
                                    if(key == int(S_truck[u + 1])):
                                        Y_truck = val
                                Map_truck.append(X_truck + ' ' + Y_truck)

                            # Weight
                            for u in range(len(Map_truck)):
                                with codecs.open(file_input, 'r', encoding='utf-8') as f_map:
                                    for line_map in f_map:
                                        if (line_map.find('Set_path') != -1):
                                            Q = Map_truck[u].split(' ')
                                            R = 0
                                            for j in range(len(Q)):
                                                if(Q[j] in line_map):
                                                    R += 1
                                            if(R == len(Q)):
                                                Weight.append(line_map.split(' ')[-1].strip())

                            #Map = Map + Map_truck
                            Map = Map_truck

                            tmp_log += A[0] + ' ' + A[1] + ' - Success' + '\r\n'
                            for f in range(len(Map)):
                                if(f < len(Map)):
                                    tmp_log += Map[f] + ' , '
                                    dist += float(Weight[f])
                                else:
                                    tmp_log += Map[f]
                                    dist += Weight

                            location = To
                            T_truck[Truck] = location

                            if((Truck in Each_truck_dist) == False):
                                Each_truck_dist[Truck] = 0
                            Each_truck_dist[Truck] += dist

                            if (line2.find('Export 2 yolo') != -1):
                                a = 1

                            '''
                            # Add slot
                            strw = []
                            for i in range(int(Amount)):
                                strw.append(Item)
                            if(To in T_warehouse_slot):
                                T_warehouse_slot[Pick_up_product] += strw
                            else:
                                T_warehouse_slot[Pick_up_product] = strw

                            # log import
                            if ((Pick_up_product in Have_import) == False):
                                Have_import[Pick_up_product] = []
                            Have_import[Pick_up_product] += strw
                            '''


                            Success_count += 1

                            print(file)
                            tmp_log = A[0] + ' ' + A[1] + ' - Success'
                            print(location + ' -> ' + To)
                            print('Truck name : {}'.format(Truck))
                            print(tmp_log)
                            print('Total distance : {}'.format(dist))
                            print('Location : {}'.format(location))
                            T_truck[Truck] = location

                            if (line2.find('Export 2 yolo') != -1):
                                a = 1

                            for key, val in T_warehouse_slot.items():
                                print(key, '->', val)

                            for key, val in T_truck.items():
                                print('Update truck : ', key, '->', val)

                            print('------')

                    elif (line2.find('Transfer') != -1): # Transfer

                        if (line2.find('Transfer 1 KFC chicken') != -1):
                            a = 1

                        Process_count += 1

                        FT = line2.strip().split('from')
                        FT2 = FT[0].strip().split(' ')

                        FP = line2.strip().split('to')
                        FP2 = FP[1].strip().split(' ')

                        A = line2.strip().split(' ')
                        if(len(A) > 7 and len(FT2) < 4 and len(FP2) == 1):
                            Amount = A[1]
                            Item = A[2]
                            From = A[4] + ' ' + A[5]
                            To = A[7]
                        elif(len(A) > 7 and len(FT2) >= 4 and len(FP2) == 1):
                            Amount = A[1]
                            Item = A[2] + ' ' + A[3]
                            From = A[5]
                            To = A[7]
                        elif(len(A) > 7 and len(FT2) >= 4 and len(FP2) > 1):
                            Amount = A[1]
                            Item = A[2] + ' ' + A[3]
                            From = A[5]
                            To = A[7] + ' ' + A[8]
                        else:
                            Amount = A[1]
                            Item = A[2]
                            From = A[4]
                            To = A[6]

                        # STEP 1 - check existing (item, harbor, warehouse)
                        Existing_item = False
                        Ad = check_create_item(Item)
                        Cd = check_warehouse(To)
                        if (Ad and Cd):
                            Existing_item = True
                        else:
                            Existing_item = False

                        Existing_item = False
                        for key, val in T_warehouse_slot.items():
                            if(key == From):
                                for t in val:
                                    if(t == Item):
                                        Existing_item = True

                        if (line2.find('Transfer 1 KFC chicken') != -1):
                            a = 1

                        # STEP 2 - select truck
                        [Loaded, Truck] = check_truck(Item, Amount)

                        # STEP 3 - warehouse temp
                        Warehouse_temp = check_warehouse_temp(To, Item, Amount)


                        if (Existing_item and Loaded and Warehouse_temp and Truck != 'Reject' ):

                            Success_count += 1

                            with codecs.open(file_input, 'r', encoding='utf-8') as f3:
                                for line3 in f3:
                                    if (line3.find('Set_path') != -1):

                                        AY = line3.strip().split(' ')
                                        if ((AY[1] == location and AY[2] == To) or (AY[1] == To and AY[2] == location)):
                                            tmp_log = A[0] + ' ' + A[1] + ' - Success' + '\r\n'
                                            tmp_log += location + ' -> ' + To
                                            dist += int(AY[3])
                                            print(file)
                                            print('Truck name : {}'.format(Truck))
                                            print(tmp_log)
                                            print('Total distance : {}'.format(dist))
                                            print('Location : {}'.format(location))
                                            location = To
                                            T_truck[Truck] = location

                                            for key, val in T_truck.items():
                                                print('Update truck : ', key, '->', val)

                                            print('------')

                                            T_truck[Truck] = location

                                            # Add slot
                                            strw = []
                                            for i in range(int(Amount)):
                                                strw.append(Item)
                                            T_warehouse_slot[To] = strw

                                            # Find start airport & harbor location
                                            S = False
                                            txt = []
                                            Concerned_path = []

                                            # Depth-First Search Path
                                            num = [x for x in range(1, 1000)]
                                            c = 1
                                            Dict_dfs = {}
                                            RE = []
                                            MS = []
                                            with codecs.open(file_input, 'r', encoding='utf-8') as f_dfs:
                                                for line_dfs in f_dfs:
                                                    if (line_dfs.find('Set_path') != -1):
                                                        SPLIT_1 = line_dfs.rstrip().split(' ')
                                                        if (len(SPLIT_1) == 5):
                                                            A = SPLIT_1[1]
                                                            B = SPLIT_1[2] + ' ' + SPLIT_1[3]
                                                            C = SPLIT_1[4]
                                                            RE.append(A)
                                                            RE.append(B)
                                                            MS += [[A, B]]
                                                        else:
                                                            A = SPLIT_1[1]
                                                            B = SPLIT_1[2]
                                                            C = SPLIT_1[3]
                                                            RE.append(A)
                                                            RE.append(B)
                                                            MS += [[A, B]]
                                                    c += 1

                                            RE = list(OrderedDict.fromkeys(RE))
                                            RE2 = num[:len(RE)]

                                            cm = 0
                                            for o in range(len(MS)):
                                                SE = MS[o]
                                                for o2 in range(len(SE)):
                                                    for o3 in range(len(RE)):
                                                        if (SE[o2] == RE[o3]):
                                                            SE[o2] = o3 + 1
                                                MS[o] = SE

                                            Tx = {}
                                            for i in range(len(RE2)):
                                                d = RE2[i]
                                                Tx[d] = []
                                                for j in range(len(MS)):
                                                    e = MS[j]
                                                    if (d in e):
                                                        if (e[0] != d):
                                                            Tx[d] += str(e[0])
                                                        elif (e[1] != d):
                                                            Tx[d] += str(e[1])

                                            XP = {}
                                            for ko in range(len(RE)):
                                                if ((str(ko + 1) in XP) == False):
                                                    XP[str(ko + 1)] = []
                                                XP[str(ko + 1)] = set(Tx[ko + 1])

                                            graph = XP

                                            # A = Naboo , B = Coruscant , C = Tatooine , D = Galactic City , E = Gungan , F = Tomas
                                            Weight = []

                                            for mm in range(len(RE)):
                                                if (RE[mm] == From):
                                                    START = mm + 1

                                            for mm in range(len(RE)):
                                                if (RE[mm] == Pick_up_product):
                                                    END = mm + 1

                                            # Path From - To
                                            R_path = list(dfs_paths(graph, str(START), str(END)))
                                            X = ''
                                            Y = ''

                                            DICT = {}
                                            for jk in range(len(RE)):
                                                DICT[jk + 1] = RE[jk]

                                            if (line2.find('Transfer 1 KFC chicken') != -1):
                                                a = 1

                                            # DICT = {'A':'Naboo' , 'B':'Coruscant' , 'C':'Tatooine' , 'D':'Galactic City' , 'E':'Gungan' , 'F':'Tomas'}
                                            S = R_path[0]
                                            Map = []
                                            for u in range(len(S) - 1):
                                                for key, val in DICT.items():
                                                    if (key == int(S[u])):
                                                        X = val
                                                    if (key == int(S[u + 1])):
                                                        Y = val
                                                Map.append(X + ' ' + Y)

                                            # Weight
                                            for u in range(len(Map)):
                                                with codecs.open(file_input, 'r', encoding='utf-8') as f_map:
                                                    for line_map in f_map:
                                                        if (line_map.find('Set_path') != -1):
                                                            Q = Map[u].split(' ')
                                                            R = 0
                                                            for j in range(len(Q)):
                                                                if (Q[j] in line_map):
                                                                    R += 1
                                                            if (R == len(Q)):
                                                                Weight.append(line_map.split(' ')[-1].strip())

                                            for mm in range(len(RE)):
                                                if (RE[mm] == Start_truck):
                                                    Truck_location = mm + 1

                                            R_path_truck = list(dfs_paths(graph, str(Truck_location), str(START)))
                                            X_truck = ''
                                            Y_truck = ''
                                            DICT_truck = DICT
                                            S_truck = R_path_truck[0]
                                            Map_truck = []
                                            for u in range(len(S_truck) - 1):
                                                for key, val in DICT_truck.items():
                                                    if (key == int(S_truck[u])):
                                                        X_truck = val
                                                    if (key == int(S_truck[u + 1])):
                                                        Y_truck = val
                                                Map_truck.append(X_truck + ' ' + Y_truck)

                                            # Weight
                                            for u in range(len(Map_truck)):
                                                with codecs.open(file_input, 'r', encoding='utf-8') as f_map:
                                                    for line_map in f_map:
                                                        if (line_map.find('Set_path') != -1):
                                                            Q = Map_truck[u].split(' ')
                                                            R = 0
                                                            for j in range(len(Q)):
                                                                if (Q[j] in line_map):
                                                                    R += 1
                                                            if (R == len(Q)):
                                                                Weight.append(line_map.split(' ')[-1].strip())

                                            # Map = Map + Map_truck
                                            Map = Map_truck

                                            tmp_log += A[0] + ' ' + A[1] + ' - Success' + '\r\n'
                                            for f in range(len(Map)):
                                                if (f < len(Map)):
                                                    tmp_log += Map[f] + ' , '
                                                    dist += float(Weight[f])
                                                else:
                                                    tmp_log += Map[f]
                                                    dist += Weight

                                            location = To
                                            T_truck[Truck] = location

                                            if ((Truck in Each_truck_dist) == False):
                                                Each_truck_dist[Truck] = 0
                                            Each_truck_dist[Truck] += dist

                                            # Update slot
                                            for i in range(int(Amount)):
                                                T_warehouse_slot[From].pop()

                                            if (line2.find('Transfer 1 KFC chicken') != -1):
                                                a = 1

                                            # Add slot
                                            Amount = 0
                                            strw = []
                                            for i in range(int(Amount)):
                                                strw.append(Item)
                                            if (To in T_warehouse_slot):
                                                T_warehouse_slot[To] += strw
                                            else:
                                                T_warehouse_slot[To] = strw

                        else:

                            Fail_count += 1

                            # Add slot
                            #T_warehouse_slot[To] = []

                            tmp_log = A[0] + ' ' + A[1] + ' - Failed' + '\r\n'
                            tmp_log += location + ' -> ' + To
                            dist = 0
                            print(file)
                            print('Truck name : {}'.format(Truck))
                            print(tmp_log)
                            print('Total distance : {}'.format(dist))
                            print('Location : {}'.format(location))
                            T_truck[Truck] = location

                            for key, val in T_truck.items():
                                print('Update truck : ', key, '->', val)

                            print('------')

                    elif(line2.find('Import') != -1): # Import

                        Process_count += 1

                        if (line2.find('Import 150 KFC chicken') != -1):
                            a = 1

                        FT = line2.strip().split('from')
                        FT2 = FT[0].strip().split(' ')

                        FP = line2.strip().split('to')
                        FP2 = FP[1].strip().split(' ')

                        A = line2.strip().split(' ')
                        if(len(A) > 7 and len(FT2) < 4 and len(FP2) == 1):
                            Amount = A[1]
                            Item = A[2]
                            From = A[4] + ' ' + A[5]
                            To = A[7]
                        elif(len(A) > 7 and len(FT2) >= 4 and len(FP2) == 1):
                            Amount = A[1]
                            Item = A[2] + ' ' + A[3]
                            From = A[5]
                            To = A[7]
                        elif(len(A) > 7 and len(FT2) >= 4 and len(FP2) > 1):
                            Amount = A[1]
                            Item = A[2] + ' ' + A[3]
                            From = A[5]
                            To = A[7] + ' ' + A[8]
                        else:
                            Amount = A[1]
                            Item = A[2]
                            From = A[4]
                            To = A[6]

                        if (line2.find('Import 150 KFC chicken') != -1):
                            a = 1

                        # STEP 1 - check existing (item, harbor, warehouse)
                        Existing_item = False
                        Ad = check_create_item(Item)
                        Bd = check_existing_harbor_ariport_train(From)
                        Cd = check_warehouse(To)
                        if (Ad and Bd and Cd):
                            Existing_item = True
                        else:
                            Existing_item = False

                        if (line2.find('Import 100 KFC chicken') != -1):
                            a = 1

                        # STEP 2 - select truck
                        [Loaded, Truck] = check_truck(Item, Amount)

                        # Last location
                        '''
                        if (len(T_truck) != 0):
                            for key, val in T_truck.items():
                                if(key == Truck):
                                    From = val
                        '''

                        if (line2.find('Import 100 KFC chicken') != -1):
                            a = 1

                        # STEP 3 - warehouse temp
                        Warehouse_temp = check_warehouse_temp(To, Item, Amount)


                        # STEP 4 - Check index harbor , ariport, train station
                        Pick_up_product = ''
                        [Ind, txt] = check_index_harbor_ariport_train(From)
                        if(txt == 'Harbor'):
                            Pick_up_product = hb.named_harbor[Ind]
                        elif(txt == 'Airport'):
                            Pick_up_product = ap.named_airport[Ind]
                        elif(txt == 'Train_Station'):
                            Pick_up_product = tr.named_train_Station[Ind]

                        if(Existing_item and Loaded and Warehouse_temp and Truck != 'Reject'):

                            Success_count += 1

                            # Truck working
                            Start_truck = ap.named_airport[0]

                            for key, val in T_truck.items():
                                if (key == Truck):
                                    Start_truck = val

                            Start_truck.replace('"', '')


                            # Find start airport & harbor location
                            S = False
                            txt = []
                            Concerned_path = []

                            # Depth-First Search Path
                            num = [x for x in range(1, 1000)]
                            c = 1
                            Dict_dfs = {}
                            RE = []
                            MS = []
                            with codecs.open(file_input, 'r', encoding='utf-8') as f_dfs:
                                for line_dfs in f_dfs:
                                    if(line_dfs.find('Set_path') != -1):
                                        SPLIT_1 = line_dfs.rstrip().split(' ')
                                        if (len(SPLIT_1) == 5):
                                            A = SPLIT_1[1]
                                            B = SPLIT_1[2] + ' ' + SPLIT_1[3]
                                            C = SPLIT_1[4]
                                            RE.append(A)
                                            RE.append(B)
                                            MS += [[A, B]]
                                        else:
                                            A = SPLIT_1[1]
                                            B = SPLIT_1[2]
                                            C = SPLIT_1[3]
                                            RE.append(A)
                                            RE.append(B)
                                            MS += [[A, B]]
                                    c += 1

                            RE = list(OrderedDict.fromkeys(RE))
                            RE2 = num[:len(RE)]

                            cm = 0
                            for o in range(len(MS)):
                                SE = MS[o]
                                for o2 in range(len(SE)):
                                    for o3 in range(len(RE)):
                                        if(SE[o2] == RE[o3]):
                                            SE[o2] = o3 + 1
                                MS[o] = SE

                            Tx = {}
                            for i in range(len(RE2)):
                                d = RE2[i]
                                Tx[d] = []
                                for j in range(len(MS)):
                                    e = MS[j]
                                    if (d in e):
                                        if (e[0] != d):
                                            Tx[d] += str(e[0])
                                        elif (e[1] != d):
                                            Tx[d] += str(e[1])

                            XP = {}
                            for ko in range(len(RE)):
                                if((str(ko + 1) in XP) == False):
                                    XP[str(ko + 1)] = []
                                XP[str(ko + 1)] = set(Tx[ko + 1])

                            graph = XP

                            # A = Naboo , B = Coruscant , C = Tatooine , D = Galactic City , E = Gungan , F = Tomas
                            Weight = []

                            for mm in range(len(RE)):
                                if(RE[mm] == Pick_up_product):
                                    START = mm + 1

                            for mm in range(len(RE)):
                                if (RE[mm] == To):
                                    END = mm + 1

                            # Path From - To
                            R_path = list(dfs_paths(graph, str(START), str(END)))
                            X = ''
                            Y = ''

                            DICT = {}
                            for jk in range(len(RE)):
                                DICT[jk + 1] = RE[jk]

                            #DICT = {'A':'Naboo' , 'B':'Coruscant' , 'C':'Tatooine' , 'D':'Galactic City' , 'E':'Gungan' , 'F':'Tomas'}
                            S = R_path[0]
                            Map = []
                            for u in range(len(S) - 1):
                                for key, val in DICT.items():
                                    if(key == int(S[u])):
                                        X = val
                                    if(key == int(S[u + 1])):
                                        Y = val
                                Map.append(X + ' ' + Y)

                            # Weight
                            for u in range(len(Map)):
                                with codecs.open(file_input, 'r', encoding='utf-8') as f_map:
                                    for line_map in f_map:
                                        if (line_map.find('Set_path') != -1):
                                            Q = Map[u].split(' ')
                                            R = 0
                                            for j in range(len(Q)):
                                                if(Q[j] in line_map):
                                                    R += 1
                                            if(R == len(Q)):
                                                Weight.append(line_map.split(' ')[-1].strip())


                            for mm in range(len(RE)):
                                if(RE[mm] == Start_truck):
                                    Truck_location = mm + 1

                            R_path_truck = list(dfs_paths(graph, str(Truck_location), str(START)))
                            X_truck = ''
                            Y_truck = ''
                            DICT_truck = DICT
                            S_truck = R_path_truck[0]
                            Map_truck = []
                            for u in range(len(S_truck) - 1):
                                for key, val in DICT_truck.items():
                                    if(key == int(S_truck[u])):
                                        X_truck = val
                                    if(key == int(S_truck[u + 1])):
                                        Y_truck = val
                                Map_truck.append(X_truck + ' ' + Y_truck)

                            # Weight
                            for u in range(len(Map_truck)):
                                with codecs.open(file_input, 'r', encoding='utf-8') as f_map:
                                    for line_map in f_map:
                                        if (line_map.find('Set_path') != -1):
                                            Q = Map_truck[u].split(' ')
                                            R = 0
                                            for j in range(len(Q)):
                                                if(Q[j] in line_map):
                                                    R += 1
                                            if(R == len(Q)):
                                                Weight.append(line_map.split(' ')[-1].strip())

                            Map = Map + Map_truck

                            tmp_log += A[0] + ' ' + A[1] + ' - Success' + '\r\n'
                            for f in range(len(Map)):
                                if(f < len(Map)):
                                    tmp_log += Map[f] + ' , '
                                    dist += float(Weight[f])
                                else:
                                    tmp_log += Map[f]
                                    dist += Weight

                            location = To
                            T_truck[Truck] = location

                            if((Truck in Each_truck_dist) == False):
                                Each_truck_dist[Truck] = 0
                            Each_truck_dist[Truck] += dist

                            if (line2.find('Import 30 KFC chicken') != -1):
                                a = 1

                            # Add slot
                            strw = []
                            for i in range(int(Amount)):
                                strw.append(Item)
                            if(To in T_warehouse_slot):
                                T_warehouse_slot[To] += strw
                            else:
                                T_warehouse_slot[To] = strw

                            if (line2.find('Import 30 KFC chicken') != -1):
                                a = 1

                            # log import
                            if ((Pick_up_product in Have_import) == False):
                                Have_import[Pick_up_product] = []
                            Have_import[Pick_up_product] += strw

                            cm = 0
                            for ty in range(len(All_station)):
                                if Pick_up_product in All_station[ty]:
                                    All_station.pop(ty)
                                    break
                                else:
                                    Have_import[All_station[ty][1:-1]] = []
                                cm += 1

                            # Create temp warehousr
                            for pm in range(len(Each_warehouse_name)):
                                ZX = Each_warehouse_name[pm]
                                if ((ZX in T_warehouse_slot) == False):
                                    T_warehouse_slot[Each_warehouse_name[pm]] = []

                            for key, val in T_warehouse_slot.items():
                                print(key, '->', val)

                            for key, val in T_truck.items():
                                print('Update truck : ', key, '->', val)

                        else:

                            if((Truck in Each_truck_dist) == False):
                                Each_truck_dist[Truck] = 0
                            Each_truck_dist[Truck] += dist

                            # Add slot
                            Amount = 0
                            strw = []
                            for i in range(int(Amount)):
                                strw.append(Item)
                            if(To in T_warehouse_slot):
                                T_warehouse_slot[To] += strw
                            else:
                                T_warehouse_slot[To] = strw

                            # log import
                            if ((Pick_up_product in Have_import) == False):
                                Have_import[Pick_up_product] = []
                            Have_import[Pick_up_product] += strw

                            cm = 0
                            for ty in range(len(All_station)):
                                if Pick_up_product in All_station[ty]:
                                    All_station.pop(ty)
                                    break
                                else:
                                    Have_import[All_station[ty][1:-1]] = []
                                cm += 1

                            Fail_count += 1

                            if(Warehouse_temp == False):
                                Truck = ''

                            if(Truck == 'Reject'):
                                #Truck = ''
                                tmp_log = A[0] + ' ' + A[1] + ' - Reject'
                            else:
                                tmp_log = A[0] + ' ' + A[1] + ' - Failed'

                        print(file)
                        print('Truck name : {}'.format(Truck))
                        print(tmp_log)
                        print('Total distance : {}'.format(dist))
                        print('Location : {}'.format(location))

                        print('------')

            print('########################')



            if(Truck == 'Reject'):
                LOG += 'Reject' + '\r\n\r\n'
            else:
                LOG += 'Process: ' + str(Process_count) + '\r\n'
                LOG += 'Success: ' + str(Success_count) + '\r\n'
                LOG += 'Fail: ' + str(Fail_count) + '\r\n'

                # Order log
                TE = ''
                for key, val in T_warehouse_slot.items():
                    if(len(val) > 0 and key in Each_slot_warehouse):
                        Name_warehouse = key
                        Have_product = val
                        Have_product_count = len(val)
                        LM = '['
                        for ps in range(len(val)):
                            if(ps < len(val) - 1):
                                LM += str(val[ps]) + ', '
                            else:
                                LM += str(val[ps])
                        LM += ']'
                        TE += Name_warehouse + ' (' + str(Have_product_count) + '/' + Each_slot_warehouse[key] + '): ' + LM + '\r\n'
                    elif(key in Each_slot_warehouse):
                        Name_warehouse = key
                        Have_product = val
                        Have_product_count = len(val)
                        LM = '['
                        for ps in range(len(val)):
                            if(ps < len(val) - 1):
                                LM += str(val[ps]) + ', '
                            else:
                                LM += str(val[ps])
                        LM += ']'
                        TE += Name_warehouse + ' (' + str(Have_product_count) + '/' + Each_slot_warehouse[key] + '): ' + LM + '\r\n'

                TE += '\r\n'
                LOG += TE + '\r\n'

    # Sumary log
    Summary = ''
    for key, val in T_warehouse_slot.items():
        if (len(val) >= 0 and key in Each_slot_warehouse):
            Name_warehouse = key
            Have_product = val
            Have_product_count = len(val)
            LM2 = '['
            for ps in range(len(val)):
                if (ps < len(val) - 1):
                    LM2 += str(val[ps]) + ', '
                else:
                    LM2 += str(val[ps])
            LM2 += ']'
            Summary += Name_warehouse + ' (' + str(Have_product_count) + '/' + Each_slot_warehouse[key] + '): ' + LM2 + '\r\n'
    LOG += 'Summary:' + '\r\n'
    LOG += Summary

    # Truck dist
    Truck_log = ''
    for key, val in Each_truck_dist.items():
        Truck_log += key.strip() + ' has traveled ' + str(val) + ' km.' + '\r\n'
    LOG += Truck_log

    # Import log
    Import_log = ''
    for key, val in Have_import.items():

        mp = ''
        for kl in range(len(val)):
            if(kl < len(val) - 1):
                mp += val[kl] + ', '
            else:
                mp += val[kl]
        Import_log += key + ' has imported ' + str(len(val)) + ' items:' + ' [' + mp + ']' + '\r\n'

        if(key in Have_export and len(Have_export[key]) > 0):
            for key, val in Have_export.items():
                mp2 = ''
                for kl in range(len(val)):
                    if (kl < len(val) - 1):
                        mp2 += val[kl] + ', '
                    else:
                        mp2 += val[kl]
                Import_log += key + ' has exported ' + str(len(val)) + ' items:' + ' [' + mp2 + ']' + '\r\n'
        else:
            Import_log += key + ' has exported ' + str(0) + ' items:' + ' []' + '\r\n'

    LOG += Import_log


    # Save log
    with open('log.txt', 'w') as fs:
        fs.write(LOG)
