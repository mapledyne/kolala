import kolala.framework.aiml

import aiml

k = aiml.Kernel()
k.verbose()

k.learn("aiml/aiml/*.aiml")
