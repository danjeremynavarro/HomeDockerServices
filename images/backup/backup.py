import tarfile
import datetime
import os

backup_vol = "/backups"
current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
backup_location = ("{}/archive{}.tar.gz".format(backup_vol, current_time))
dirs = ("/data")
print("started at {}".format(current_time))
with tarfile.open(backup_location, "w:gz") as tar:
    tar.add(dirs, arcname=os.path.basename(dirs))

end_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
print("finished at {}".format(end_time))