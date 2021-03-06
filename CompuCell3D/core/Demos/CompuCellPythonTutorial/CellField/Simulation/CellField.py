import sys
from os import environ
from os import getcwd
import string

sys.path.append(environ["PYTHON_MODULE_PATH"])

import CompuCellSetup

sim,simthread = CompuCellSetup.getCoreSimulationObjects()
            
CompuCellSetup.initializeSimulationObjects(sim,simthread)
        
#Add Python steppables here
steppableRegistry=CompuCellSetup.getSteppableRegistry()

from CellFieldSteppables import UniformInitializer
instanceOfUniformInitializer=UniformInitializer(_simulator=sim,_frequency=1)
steppableRegistry.registerSteppable(instanceOfUniformInitializer)

CompuCellSetup.mainLoop(sim,simthread,steppableRegistry)
        
        