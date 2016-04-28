import aiml
import time

def initiate():
    # The Kernel object is the public interface to
    # the AIML interpreter.
    k = aiml.Kernel()

    # Use the 'learn' method to load the contents
    # of an AIML file into the Kernel.
    # k.learn("std-startup.xml")
    import glob
    filenames = glob.glob('alice/*.aiml')
    for x in filenames:
        k.learn(x)

    return k

# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
# k.respond("load aiml b")

# Loop forever, reading user input from the command
# line and printing responses.
# first = k.respond("hai")
# while True:
    # second = k.respond(first)
    # first = k.respond(second)
    # if first == "":
        # first = "hai again"
    # if len(first) > 300:
        # first = "stop it"
    # print "\n :: " + second
    # time.sleep(2)
    # print "\n ** " + first
k = initiate()
while True:
    print k.respond(raw_input(">"))
