
import os
import psutil

def close_chrome():
    for process in psutil.process_iter():
        try:
            process_info = process.as_dict(attrs=['pid', 'name'])
            process_name = process_info['name']
            if process_name == 'chrome.exe':
                process.terminate()
                print(f"Terminated Chrome process (PID: {process_info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

close_chrome()
print('All Existing chrome  processes closed.')
import subprocess
p=False
if os.path.exists('C:\Program Files\Google\Chrome\Application\chrome.exe'):
    p='C:\Program Files\Google\Chrome\Application\chrome.exe'
elif os.path.exists('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'):
    p='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
elif os.path.exists('C:\LocalAppData\Google\Chrome\Application\chrome.exe'):
    p='C:\LocalAppData\Google\Chrome\Application\chrome.exe.'
if p:
    # print(os.system('"'+p+'" --remote-debugging-port=9222'))
    subprocess.Popen('"'+p+'" --remote-debugging-port=9222')

else:
    subprocess.Popen('chrome --remote-debugging-port=9222')
    # os.system('chrome --remote-debugging-port=9222')

