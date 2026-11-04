import graphviz

dot = graphviz.Digraph('cinematic_arthuriana_influences', comment="Influences on Cinematic Athuriana")

'''
Key

media formats:
 - Film = green
 - Medieval Text = red
 - Book = blue
 - Stage Production = yellow
 - Other = orange

relationship types:
 - Adaptation = purple
 - Inspiration = cyan
 - Continuation (i.e. same series) = black


'''

# Nodes
## template: dot.node("", color='')
    # Valiant
dot.node("Prince Valiant (1954)", color='green')
dot.node("Prince Valiant (1997)", color='green')
dot.node("Hal Foster's Prince Valiant", color='orange')
    # Perceval/Parsival/Parzival/Percival/etc.
dot.node("Parsival (1904)", color='green')
dot.node("The Evil Forest", color='green')
dot.node("Parsival (1982)", color='green')
dot.node("Richard Wagner's Parsival", color='yellow')
dot.node("Parzival by Wolfram von Eschenbach", color='red')
dot.node("Perceval, the Story of the Grail by Chrétien de Troyes", color='red')
    # Connecticut Yankee

    # The Sword in the Stone / The Once and Future King

    # 

# Edges
## template: dot.edge("", "", color='')
dot.edge("Hal Foster's Prince Valiant", "Prince Valiant (1954)", color='purple')
dot.edge("Hal Foster's Prince Valiant", "Prince Valiant (1997)", color='purple')

dot.edge("Perceval, the Story of the Grail by Chrétien de Troyes", "Prince Valiant (1954)", color='cyan')

dot.edge("Richard Wagner's Parsival", "Parsival (1904)", color='purple')
dot.edge("Richard Wagner's Parsival", "The Evil Forest", color='purple')
dot.edge("Richard Wagner's Parsival", "Parsival (1982)", color='purple')
dot.edge("Parzival by Wolfram von Eschenbach", "Richard Wagner's Parsival", color='cyan')
dot.edge("Perceval, the Story of the Grail by Chrétien de Troyes", "Richard Wagner's Parsival", color='cyan')

# Render
dot.render(view=True)