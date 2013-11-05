from jpype import *
import random
import math

jarLocation = "assets/infodynamics.jar"
# Start the JVM (add the "-Xmx" option with say 1024M if you get
# crashes due to not enough memory space)
jpath = "-Djava.class.path=" + jarLocation
startJVM(getDefaultJVMPath(), "-ea", jpath)

def transferEntropy(source_array, dest_array):
    # Create a TE calculator and run it:
    jp = JPackage("infodynamics.measures.continuous.kernel")
    teCalcClass = jp.TransferEntropyCalculatorKernel
    teCalc = teCalcClass();
    # Normalise the individual variables
    teCalc.setProperty("NORMALISE", "true"); 
    # Use history length 1 (Schreiber k=1), kernel width of 0.5
    # normalised units
    teCalc.initialise(1, 0.5); 
    teCalc.setObservations(JArray(JDouble, 1)(source_array), JArray(JDouble, 1)(dest_array));
    # For copied source, should give something close to 1 bit:
    result = teCalc.computeAverageLocalOfObservations();
    return result



