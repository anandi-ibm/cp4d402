# Get environment variables
import os
ENV1 = os.getenv('ENV1')
ENV2 = os.getenv('ENV2')
 
#script with arg

import sys
print ("The script has the name %s" % (sys.argv[0]))
arguments = len(sys.argv) - 1
print ("The script is called with %i arguments" % (arguments))
