import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# make it dark theme
plt.style.use('dark_background')

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def create_collatz_tree(starting_numbers):
    G = nx.Graph()
    for start in starting_numbers:
        sequence = collatz_sequence(start)
        for i in range(len(sequence) - 1):
            G.add_edge(sequence[i], sequence[i+1])
    return G

def visualize_collatz_tree(G: nx.Graph):
    pos = nx.spring_layout(G)
    # make figure size square
    plt.figure(figsize=(6,6))
    plt.title('Collatz tree', size=20)
    nx.draw_networkx(G, 
                     pos,
                     with_labels=False,
                     node_size=10,
                     node_color='r',
                     edge_color=range(2, G.number_of_edges() + 2),
                     edge_cmap=cm.get_cmap('viridis')
                     )
    # save figure
    plt.savefig('collatz.png', dpi=1000)
    plt.show()

# Example usage
starting_numbers = [6, 9, 27, 10, 24, 3, 7, 15, 96, 9663]
collatz_tree = create_collatz_tree(starting_numbers)
visualize_collatz_tree(collatz_tree)
