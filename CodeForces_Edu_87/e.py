v,e = map(int,input().split())

n1,n2,n3 = map(int,input().split())


colors = ['1','2','3']
states = []
neighbors = defaultdict(list)

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color


while e != 0:
    u,v = map(int,input().split())
    neighbors[u].extend(v)
    if u not in states:
        states.append(u)
    e -= 1

print(neighbors)
print(states)

colors_of_states = {}

for state in states:
    colors_of_states[state] = get_color_for_state(state)





# colors_of_states = {}

#     print colors_of_states