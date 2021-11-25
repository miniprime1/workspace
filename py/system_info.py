import platform, socket, psutil, time, getpass, math

systeminfo = {
    'System': str(platform.system() + ' ' + platform.release() + ' ' + platform.machine()),
    'Hostname': socket.gethostname(),
    "Uptime": str(str(math.floor((time.time()-psutil.boot_time())/(24*60*60))) + " days, " + time.strftime("%H hours, %M mins", time.gmtime((time.time()-psutil.boot_time())%(24*60*60)))),
    "Kernel": platform.release(),
    'Version': platform.version(),
    'Machine': platform.machine(),
    'CPU': platform.processor(),
    'Memory': str(round(psutil.virtual_memory().total / (2**20)))+"MB"
}

print(f"{getpass.getuser()}@{socket.gethostname()}")
print("-" * len(f"{getpass.getuser()}@{socket.gethostname()}"))
for i in systeminfo: print(f"{i}: {systeminfo[i]}")
