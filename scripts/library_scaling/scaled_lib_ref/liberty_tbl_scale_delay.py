from liberty.parser import parse_liberty
import numpy as np
import bisect
import sys


def GetScaleLine(lx, ux, x):
  # -.1 to +.1
  if x <= ux:
    return float(sys.argv[1])
  else:
    return float(sys.argv[1])

def GetUpdatedTables( tbl, maxCap ):
  transArr = tbl.get_array('index_1')[0]
  capArr = tbl.get_array('index_2')[0]
  valueArr = tbl.get_array('values')

  closeIdx = bisect.bisect_left(capArr, maxCap)

  newArr = np.copy(valueArr)

  for tranIdx in range( len(transArr) ):
    for capIdx in range( len(capArr) ):
      scaleDownFact = GetScaleLine( capArr[0], maxCap, capArr[capIdx] )  
      # Negative delay should have opposite effects
      value = valueArr[tranIdx][capIdx]
      if value < 0:
        scaleDownFact *= -1.0

      newArr[tranIdx][capIdx] = value * (1.0 + scaleDownFact)

  tbl['values'].clear()
  tbl.attributes.pop(2)
  tbl.set_array('values', newArr) 

### Configuration ###
liberty_file = sys.argv[2]

library = parse_liberty(open(liberty_file).read())

# print("parse is done")

cells = library.get_groups('cell')
for cell in cells:
  for pin in cell.get_groups('pin'):
    pinTimings = pin.get_groups('timing')

    if 'max_capacitance' not in pin:
      continue

    for timing in pinTimings:
      riseTbls = timing.get_groups('cell_rise')
      fallTbls = timing.get_groups('cell_fall')

      for riseTbl in riseTbls:
        if 'index_2' not in riseTbl: 
          continue
        GetUpdatedTables( riseTbl, pin['max_capacitance'] )
      for fallTbl in fallTbls:
        if 'index_2' not in riseTbl: 
          continue
        GetUpdatedTables( fallTbl, pin['max_capacitance'] )

print( str( library ) )

