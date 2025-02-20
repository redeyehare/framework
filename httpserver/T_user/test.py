import datetime
from pathlib import Path
import sys

Root_path = Path(__file__).resolve().parent.parent
sys.path.append(str(Root_path))
import T_structure.database_table_structre as dbts

print(dbts.user)



current_datetime = datetime.datetime.now()
print(current_datetime)