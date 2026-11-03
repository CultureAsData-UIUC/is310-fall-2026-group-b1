import graphviz

dot = graphviz.Digraph('cinematic_arthuriana_influences', comment="Influences on Cinematic Athuriana")

'''
Key

media formats:
 - Film = green
 - Medieval Text = red
 - Novel = blue
 - Other = yellow

relationship types:
 - Adaptation = purple
 - Inspiration = cyan
 - Continuation (i.e. same series) = black


'''

dot.node("Prince Valiant (1954)", color='green')
dot.node("Hal Foster's Prince Valiant", color='yellow')
dot.edge("Hal Foster's Prince Valiant", "Prince Valiant (1954)", color='purple')




dot.render()