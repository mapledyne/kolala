import kolala.framework.aiml

import aiml

k = aiml.Kernel()
k.verbose()

k.learn("aiml/aiml/*.aiml")

while True:
    print(k.respond(raw_input("> ")))
