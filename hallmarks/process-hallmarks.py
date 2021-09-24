# Process Hallmarks of cancer texts and labels to give a single file csv dataset
# of one sentence per line
# main labels, not sub-labels, are output
# if a line has two labels, both are output

# import os for dir listing, re for string processing
import os, re

# where are our files?
textDir = './text'
labelsDir = './labels'

# label file delimeters and stings
labelDelimeter = '<'
sublabelDelimeter = '--'
multilabelDelimeter = 'AND'
noLabel = ''

# output variables
noneLabel = "NONE"
csvItemDelim = ','
csvTextDelim = '\''
 
# iterate over labels files directory
for labelsFileName in os.listdir(labelsDir):
    labelsPath = os.path.join(labelsDir, labelsFileName)
    if os.path.isfile(labelsPath):
        
        # for each file get the associated text
        textPath = os.path.join(textDir, labelsFileName)
        if os.path.isfile(textPath):
            with open(textPath ) as textFile:
                lines = textFile.readlines()

                # now get the labels themselves
                with open(labelsPath ) as labelsFile:
                    labelsStr = labelsFile.readline()
                    labels = re.split(labelDelimeter, labelsStr)

                    # trim off the first item, which is prior to the first marker
                    labels.pop(0)

                    # we should have the same number of lines and labels...
                    if len(lines) == len(labels):
                        for i, (lineLabels, line) in enumerate(zip(labels, lines)):

                            # deal with multiple labels for the same line
                            for label in re.split(multilabelDelimeter, lineLabels):
                                mainLabel = re.split(sublabelDelimeter, label)[0].strip()
                                if mainLabel == noLabel: mainLabel = noneLabel

                                # Output it all
                                fileId = os.path.splitext(labelsFileName)[0]                            
                                print(fileId, csvItemDelim, i, csvItemDelim, csvTextDelim, mainLabel, csvTextDelim, csvItemDelim, csvTextDelim, line.strip(), csvTextDelim, sep='')
                                
                            
       
  
            
