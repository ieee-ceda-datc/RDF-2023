from liberty.parser import parse_liberty
import numpy as np
import bisect
import sys


def GetScaleLine_1idx(lx, ux, x):
  # -.1 to +.1
  if x <= ux:
    return float(sys.argv[1])
  else:
    return float(sys.argv[1])

def GetScaleLine_2idx(lx, ux, x):
  # -.1 to +.1
  if x <= ux:
    return float(sys.argv[2])
  else:
    return float(sys.argv[2])

def GetUpdatedTables_1idx( tbl ):
  transArr = tbl.get_array('index_1')[0]
  valueArr = tbl.get_array('values')

  newArr = np.copy(valueArr)
  
  if len(transArr) > 1:
    for tranIdx in range( len(transArr) ):
      maxTran = transArr[len(transArr)-1]
      scaleDownFact = GetScaleLine_1idx( transArr[0], maxTran, transArr[tranIdx] ) 

      # Negative delay should have opposite effects
      value = valueArr[0][tranIdx]
      if value < 0:
        scaleDownFact = 0
  
      newArr[0][tranIdx] = value * (1.0 + scaleDownFact)
  
    tbl['values'].clear()
    tbl.attributes.pop(1)
    tbl.set_array('values', newArr) 

def GetUpdatedTables_2idx( tbl, maxCap ):
  transArr = tbl.get_array('index_1')[0]
  capArr = tbl.get_array('index_2')[0]
  valueArr = tbl.get_array('values')

  closeIdx = bisect.bisect_left(capArr, maxCap)

  newArr = np.copy(valueArr)

  for tranIdx in range( len(transArr) ):
    for capIdx in range( len(capArr) ):
      scaleDownFact = GetScaleLine_2idx( capArr[0], maxCap, capArr[capIdx] ) 

      # Negative delay should have opposite effects
      value = valueArr[tranIdx][capIdx]
      if value < 0:
        scaleDownFact = 0

      newArr[tranIdx][capIdx] = value * (1.0 + scaleDownFact)

  tbl['values'].clear()
  tbl.attributes.pop(2)
  tbl.set_array('values', newArr) 

### Configuration ###

liberty_file = sys.argv[3]

library = parse_liberty(open(liberty_file).read())

cells = library.get_groups('cell')
for cell in cells:
  for pin in cell.get_groups('pin'):
      pinPowers = pin.get_groups('internal_power')
      if pinPowers != []:
            
        if 'max_capacitance' not in pin:
          for power in pinPowers:
            riseTbls = power.get_groups('rise_power')
            fallTbls = power.get_groups('fall_power')
        
            for riseTbl in riseTbls:
              firstValue = riseTbl.get_array('values')[0][0]
              if firstValue > 0:
                GetUpdatedTables_1idx( riseTbl )
              elif firstValue < 0:
                GetUpdatedTables_1idx( riseTbl )
              else:
                continue
            for fallTbl in fallTbls:
              firstValue = fallTbl.get_array('values')[0][0]
              if firstValue > 0:
                GetUpdatedTables_1idx( fallTbl )
              elif firstValue < 0:
                GetUpdatedTables_1idx( fallTbl )
              else:
                continue
    
        else:
          for power in pinPowers:
            riseTbls = power.get_groups('rise_power')
            fallTbls = power.get_groups('fall_power')
      
            for riseTbl in riseTbls:
              if 'index_2' not in riseTbl: 
                continue
              GetUpdatedTables_2idx( riseTbl, pin['max_capacitance'] )
            for fallTbl in fallTbls:
              if 'index_2' not in fallTbl: 
                continue
              GetUpdatedTables_2idx( fallTbl, pin['max_capacitance'] )

print( str( library ) )

