text = "Macaroon macaroon tootsie roll jelly-o cotton candy candy brownie pie jelly beans. Fruitcake candy liquorice oat cake croissant halvah. Icing tiramisu pastry ice cream sesame snaps."

def modify(original):
    return  original.replace(" ", "_").lower

print(modify(text))
