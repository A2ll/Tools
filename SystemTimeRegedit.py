import win32api
import win32con
'''
在任务栏时间中显示“秒数”
'''
key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,
                          'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced',
                          0,
                          win32con.KEY_ALL_ACCESS)
win32api.RegSetValueEx(key, 'ShowSecondsInSystemClock', 0, win32con.REG_DWORD, 0x1)
