import networkx as nx

# 待ち合わせ場所の候補（リスト型）
meet_place = []

# ファイルの読み込み
G = nx.read_weighted_edgelist('network.txt')

path = nx.dijkstra_path(G, "izumi", "loft")
length = nx.dijkstra_path_length(G, "izumi", "loft")

path2 = nx.dijkstra_path(G, "arai", "loft")
length2 = nx.dijkstra_path_length(G, "arai", "loft")

path3 = nx.dijkstra_path(G, "izumi", "paruko_two")
length3 = nx.dijkstra_path_length(G, "izumi", "paruko_two")

path4 = nx.dijkstra_path(G, "arai", "paruko_two")
length4 = nx.dijkstra_path_length(G, "arai", "paruko_two")

path_int = len(path)
# print(path_int)
count = 0
# print(path)
for i in path:
    if count <= int(path_int - 2):
        print(str(i), end=" ")
        count += 1
        print("→", end=" ")
    if count == int(path_int - 1):
        print(str(path[-1]))
        count += 1
print(str(length) + "分")

path_int2 = len(path2)
# print(path_int)
count2 = 0
# print(path)
for j in path2:
    if count2 <= int(path_int2 - 2):
        print(str(j), end=" ")
        count2 += 1
        print("→", end=" ")
    if count2 == int(path_int2 - 1):
        print(str(path2[-1]))
        count2 += 1
print(str(length2) + "分")

loft = length + length2
print("合計：" + str(loft) + "分")

# パルコ2
path_int3 = len(path3)
# print(path_int)
count3 = 0
# print(path)
for k in path3:
    if count3 <= int(path_int3 - 2):
        print(str(k), end=" ")
        count3 += 1
        print("→", end=" ")
    if count3 == int(path_int3 - 1):
        print(str(path3[-1]))
        count3 += 1
print(str(length3) + "分")

path_int4 = len(path4)
# print(path_int)
count4 = 0
# print(path)
for m in path4:
    if count4 <= int(path_int4 - 2):
        print(str(m), end=" ")
        count4 += 1
        print("→", end=" ")
    if count4 == int(path_int4 - 1):
        print(str(path4[-1]))
        count4 += 1
print(str(length4) + "分")

paruko_two = length3 + length4
print("合計：" + str(paruko_two) + "分")

if loft < paruko_two:
    print("最短で待ち合わせできる場所はロフトです！")

if loft > paruko_two:
    print("最短で待ち合わせできる場所はパルコ2です！")

