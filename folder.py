from pathlib import Path
import arrow

filesPath = r"D:\Plan"

criticalTime = arrow.now().shift(hours=+5).shift(days=-7)

for item in Path(filesPath).glob('*'):
    if item.is_file():
        print (str(item.absolute()))
        itemTime = arrow.get(item.stat().st_mtime)
        if itemTime < criticalTime:
            #remove it
            pass
