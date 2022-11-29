def main():
    print('Hello, starting script for a modified Parsec installation...')
    import requests, getpass, time, os
        
    #variable to retrieve local username account the script is run on
    usrname = getpass.getuser()

    #variable to save Parsec installer and Parsec Virtual Drive application on specified directory
    destination = f'C:\\Users\\{usrname}\\Downloads\\'

    #filepath location of the Parsec config.txt
    #filepath where Parsec will be installed for only-one user Client-side
    client_wacom = f'C:\\Users\\{usrname}\\AppData\\Roaming\\Parsec\\config.txt'
    config_path = f'C:\\Users\\{usrname}\\AppData\\Roaming\\Parsec\\'
    #filepath where Parsec will be installed as a shared software for Host side
    shared_cw_path = 'C:\\ProgramData\\Parsec\\config.txt'
    shared_config_path = 'C:\\ProgramData\\Parsec\\'

    #list of client path combined
    one_clnt_path = [client_wacom, shared_cw_path]

    #variable to run kill command for the parsec service once it installs
    shutdown = 'C:\\Program Files\\Parsec\\wscripts\\service-kill-parsec.vbs'
    #variable to start up parsec
    boot_up = 'C:\\Program Files\\Parsec\\parsecd.exe'
    print('Parsec installer and Parsec VUD installer are downloading...')

    parsecURL = 'https://builds.parsecgaming.com/package/parsec-windows.exe'
    vudURL = 'https://builds.parsec.app/vud/parsec-vud-0.1.1.0.exe'

    #using requests function to make sure official URL with installers is active
    parsec = requests.get(parsecURL,allow_redirects=True)
    vud = requests.get(vudURL,allow_redirects=True)

    #saving the filename instead of the whole filepath under the variable
    filename = parsec.url[parsecURL.rfind('/')+1:]
    filename_2 = vud.url[vudURL.rfind('/')+1:]
    files = filename, filename_2

    #installing Parsec and the Virtual Drive
    open(destination + filename, 'wb').write(parsec.content)
    open(destination + filename_2, 'wb').write(vud.content)

    #path variables for the mic_check function
    parsec_path = destination + filename
    vud_path = destination + filename_2

    #function to check that the parsec installers have been downloaded
    def mic_check(the_golden_path):
        if os.path.exists(the_golden_path):
            print(f'{the_golden_path} has been downloaded.')
        else:
            print(f"{the_golden_path} doesn't exist.")

    mic_check(parsec_path)
    mic_check(vud_path)

    print('Starting Parsec executables...')

    time.sleep(4) #Pause for 4 second for applications to download
    print('Install 1: parsec-windows.exe....')
    os.startfile(destination + filename)
    time.sleep (8) #Pause for 10 seconds so that the first application can be installed
    print('Install 2: parsec-VUD-0.1.1.0.exe...')
    os.startfile(destination + filename_2)

    #function to pause the script and wait for the user to install the executables
    def thats_alright_i_can_wait(usr_path, shared):
        while (usr_path, shared):
            if not os.path.exists(usr_path) != os.path.exists(shared):
                time.sleep(2.5) #can be modified
                print('Path not found, waiting for Parsec to be installed...')
            else:
                print(f'{files[0]} and {files[1]} confirmed, advancing with script...')
                break

    thats_alright_i_can_wait(config_path, shared_config_path)

    time.sleep(2.5)
    print('Restarting parsec application...')
    os.startfile(shutdown)

    #function to check which filepath is true based on the path variables created on lines 20 and 21
    #if True it will return the filepath where the file we are looking for is located
    def path_is_true(paths):
        for path in paths:
            if os.path.exists(path):
                true_path = "{}".format(path)
                return(true_path)

    time.sleep(2.5)
    one_and_only = path_is_true(one_clnt_path)

    #removing default config.txt from Parsec
    try:
        os.remove(one_and_only)  # type: ignore
    except FileNotFoundError(): # type: ignore
        print('The file was not found.')
    except PermissionError(): # type: ignore
        print('You do not have permission to delete the file or folder.')
    except TypeError(): # type: ignore
        print('The file was not found.')
    else:
        print('Default config was deleted...')

    print('Updating config with the custom lines...')

    time.sleep(1.5)
    #another function to check if the config file we are looking for located on path_1 or path_2
    def one_or_the_other(path_1, path_2):
        if os.path.exists(path_1):
    #replacing new config.txt with updated app_channel line to client_wacom
            with open (path_1 + 'config.txt', 'w') as file:
                file.write('''# All configuration settings must appear on a new line.
    # All whitespace, besides the newline character '\\n', is ignored.
    # All settings passed via the command line take precedence.
    # The configuration file will be overwritten by Parsec when changing settings,
    #   so if you edit this file while Parsec is running, make sure to save this file
    #   and restart Parsec immediately so your changes are preserved.

    # Example:
    # encoder_bitrate = 10

    app_channel = client_wacom
    app_flags = 1
    app_run_level = 1
    app_changelog_ver = 6
    client_pen_type = 2
    client_windowed = 1
    host_virtual_monitors = 1
    host_virtual_tablet = 1
    ''')
        else:
            with open (path_2+ 'config.txt', 'w') as file:
                file.write('''# All configuration settings must appear on a new line.
    # All whitespace, besides the newline character '\\n', is ignored.
    # All settings passed via the command line take precedence.
    # The configuration file will be overwritten by Parsec when changing settings,
    #   so if you edit this file while Parsec is running, make sure to save this file
    #   and restart Parsec immediately so your changes are preserved.

    # Example:
    # encoder_bitrate = 10

    app_channel = client_wacom
    app_flags = 1
    app_run_level = 1
    app_changelog_ver = 6
    client_pen_type = 2
    client_windowed = 1
    host_virtual_monitors = 1
    host_virtual_tablet = 1
    ''')
    print ('Settings have been updated.')

    one_or_the_other(config_path, shared_config_path)

    os.startfile(boot_up)
    print('Script has been completed.')
    time.sleep(6)

if __name__ == '__main__':
    main()