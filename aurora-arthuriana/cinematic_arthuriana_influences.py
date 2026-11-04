import graphviz

dot = graphviz.Digraph('cinematic_arthuriana_influences', comment="Influences on Cinematic Athuriana")
dot.attr(compound='true')

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

    # T.H. White
dot.node("Disney's The Sword in the Stone", color='green')
dot.node("Camelot (1967)", color='green')
dot.node("Camelot (musical)", color='yellow')
dot.node("The Sword in the Stone", color='blue')
dot.node("The Queen of Air and Darkness", color='blue')
dot.node("The Ill-Made Knight", color='blue')
dot.node("The Candle in the Wind", color='blue')
dot.node("The Book of Merlyn", color='blue')
dot.node("Le Morte D'Arthur", color='red')
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

    # Once and Future King subgraph
with dot.subgraph(name='cluster The Once and Future King by T.H. White') as c:
    c.attr(color='blue')
    c.edge("The Sword in the Stone", "The Queen of Air and Darkness")
    c.edge("The Queen of Air and Darkness", "The Ill-Made Knight")
    c.edge("The Ill-Made Knight", "The Candle in the Wind")
    c.edge("The Candle in the Wind", "The Book of Merlyn")
    c.attr(label='The Once and Future King by T.H. White')

dot.edge("The Sword in the Stone", "Disney's The Sword in the Stone", color='purple')
dot.edge("Camelot (musical)", "Camelot (1967)", color='purple')
dot.edge("The Ill-Made Knight", "Camelot (musical)", color='purple')
dot.edge("The Candle in the Wind", "Camelot (musical)", color='purple')
dot.edge("Le Morte D'Arthur", "The Sword in the Stone", lhead="cluster The Once and Future King by T.H. White", color='purple')

# Render
dot.render(view=True)