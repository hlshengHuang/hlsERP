#coding=utf-8
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     09/12/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import  sys, configparser, os,webbrowser, ctypes, winreg #  wmi, win32api, win32con,

#def main():
#    pass

#if __name__ == '__main__':
#    main()


def kill_ie():

  c = wmi.WMI()

  kernel32 = ctypes.windll.kernel32

  for process in c.Win32_Process():

    if process.Name=='iexplore.exe':

      kernel32.TerminateProcess(kernel32.OpenProcess(1, 0, process.ProcessId), 0)

def changeIEProxy(keyName, keyValue):

  pathInReg = 'Software\Microsoft\Windows\CurrentVersion\Internet Settings'

  key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER,pathInReg, 0, win32con.KEY_ALL_ACCESS)

  win32api.RegSetValueEx(key, keyName, 0, win32con.REG_SZ, keyValue)

  win32api.RegCloseKey(key)

def check_config():

  if not os.path.isfile('config.ini'):

    cfg = ConfigParser.ConfigParser()

    #开发环境

    cfg.add_section('dev')

    cfg.set('dev', 'ProxyServer', '192.168.0.6:3128')

    cfg.set('dev', 'ProxyOverride', 'localhost;127.0.0.1')

    #预上线

    cfg.add_section('prepare')

    cfg.set('prepare', 'ProxyServer', '192.168.0.6:3128')

    cfg.set('prepare', 'ProxyOverride', 'localhost;127.0.0.1;')

    #线上

    cfg.add_section('online')

    cfg.set('online', 'ProxyServer', '192.168.0.6:3128')

    cfg.set('online', 'ProxyOverride', 'localhost;127.0.0.1')

    #QA

    cfg.add_section('qa')

    cfg.set('qa', 'ProxyServer', '192.168.2.16:3128')

    cfg.set('qa', 'ProxyOverride', 'localhost;127.0.0.1')

    cfg.write(open('config.ini', 'a'))

    return False

  return True

if __name__ == "__main__":

  _section = sys.argv[1] if len(sys.argv) > 1 else 'dev'

  if check_config():

    kill_ie()

    config = ConfigParser.ConfigParser()

    config.read('config.ini')

    if config.has_section(_section):

      _ProxyServer = config.get(_section, 'ProxyServer')

      _ProxyOverride = config.get(_section, 'ProxyOverride')

      changeIEProxy('ProxyServer', _ProxyServer)

      changeIEProxy('ProxyOverride', _ProxyOverride)

    print( 'done, open ie')

  else:

    print( 'config.ini is created, modify config.ini and try again')
