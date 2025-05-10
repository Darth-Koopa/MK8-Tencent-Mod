import wupclient

if __name__ == '__main__':
    print("Connecting to wupserver")
    w = wupclient.wupclient()
    if(w.s == None):
        print("Failed to connect to wupserver!")
        exit()
    print("Connected!")
    wupclient.w = w
    print("Mounting SD")
    ret = wupclient.mount_sd()
    if(ret == 0):
        print("Failed to mount SD!")
    else:
        print("Mounted! Copying content file from SD")
        ret = w.cpdir("/vol/storage_sdcard/haxchi/mariokart8gfyzhhbd", "/vol/storage_usb01/usr/title/0005000e/1010eb00")
    import os 
    os.system('pause')
    if(w.fsa_handle != None):
        w.close(w.fsa_handle)
        w.fsa_handle = None
    if(w.s != None):
        w.s.close()
        w.s = None
