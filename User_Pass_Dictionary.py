Username = "Sourabh@2411"
Password = "admin123"
User_pass = ""
User_user = ""
input_count = 4
out_of_tries = False
while (User_user != Username or User_pass != Password) and not(out_of_tries):
    if input_count > 0:
        User_user = input("Enter Username: ")
        User_pass = input ("Enter Password: ")
        input_count -= 1
        if (User_user == "" and User_pass != ""):
            input_count +=1
            print("                     Please Enter Username also")
        elif (User_user != "" and User_pass == ""):
            input_count +=1
            print("                     Please Enter Password also")
        elif (User_user == "" and User_pass == ""):
            input_count +=1
            print("                     Please Enter credentials")
        elif (User_user != Username or User_pass != Password) and input_count > 1:
            print("                     Incorrect Username or Password!")
            print("                     You have " + str(input_count) + " more tries left to login")
        elif (User_user != Username or User_pass != Password) and input_count == 1:
            print("                     Incorrect Username or Password!")
            print("                     It is your last attempt to login")
    else:
        out_of_tries = True
if out_of_tries:
    print("                             Too many attempts, Try again later")
else:
    print("                             You have successfully logged in\n"
          "                             Now, you can access the dictionary")
    i = input("Enter the short form to get the full form: ")
    j = 500
    k = ""
    m = False
    # There are key value pairs in dictionaries in which some keys are assigned values
    # which we can get by getting the key value
    # The keys should always be unique.
    Full_forms = {
        'LAN': 'Local Area Network',
        'WAN': 'Wide Area Network',
        'AES': 'Advanced Encryption Standard',
        'VPN': 'Virtual Private Network',
        'DHCP': 'Dynamic Host Configuration Protocol',
        'XSS': 'Cross-Site Scripting',
        'HIPS': 'Host-based Intrusion Prevention System',
        'HIDS': 'Host-based Intrusion Detection System',
        'NIDS': 'Network-based Intrusion Detection System',
        'NIPS': 'Network-based Intrusion Prevention System',
        'ACL': 'Access Control Lists',
        'VLAN': 'Virtual Local Area Network',
        'CAM Table': 'Content Addressable Memory Table',
        'QOS': 'Quality Of Service',
        'WEP': 'Wired Equivalent Privacy',
        'IV': 'Initialisation Vector',
        'TKIP': 'Temporal Key Integrity Protocol',
        'SSID': 'Service Set Identifier',
        'RADIUS': 'Remote Authentication Dial-In User Service',
        'PEAP': 'Protected Extensible Authentication Protocol',
        'WPA': 'Wireless Protected Access',
        'SSL': 'Secured Socket Layer',
        'TLS': 'Transport Layer Security',
        'CCMP': 'Counter Mode with Cipher Block Chaining Message Authentication Code Protocol',
        'DLP': 'Data Loss Prevention',
        'RAID': 'Redundant Array of Independent Disks',
        'PKI': 'Public Key Infrastructure',
        'POST': 'Power On Self Test',
        'MITM': 'Man In The Middle Attack',
        'ARP': 'Address Resolution Protocol',
        'ICMP': 'Internet Control Message Protocol',
        'NFC': 'Near Field Communication',
        'WPS': 'Wireless Fidelity Protected Setup or Wi-Fi Protected Setup',
        'LDAP': 'Lightweight Directory Access Protocol',
        'AAA': 'Authentication Authorisation Accounting',
        'URL': 'Uniform Resource Locator',
        'XML': 'Extensible Markup Language',
        'SSH': 'Secured Shell',
        'EAL': 'Evaluation Assurance Level',
        'FDE': 'Full Disk Encryption',
        'TPM': 'Trusted Platform Module',
        'HSM': 'Hardware Security Module',
        'RAS': 'Remote Authentication Server',
        'TACACS': 'Terminal Access Controller Access Control System',
        'SAML': 'Security Assertion Markup Language',
        'TOTP': 'Time-based One-Time Password',
        'HOTP': 'Hash-based One-Time Password',
        'PAP': 'Password Authentication Protocol',
        'CHAP': 'Challenge Handshake Authentication Protocol',
        'RBAC': 'Role-Based Access Control or it can also be Rule-Based Access Control',
        'MAC': 'Mandatory Access Control',
        'DAC': 'Discretionary Access Control',
        'IKE': 'Internet Key Exchange',
        'DH': 'Diffie-Hellman Algorithm',
        'SHA': 'Secure Hashing Algorithm',
        'PFS': 'Perfect Forward Secrecy'
    }

    while (j != 0):
            if Full_forms.get(i) != None:
                if j == 500:
                    print(Full_forms.get(i))
                    j -= 1
                else:
                    if m:
                        print(Full_forms.get(i))
                        k = input("          Do You want to continue ?")
                        if k == "yes":
                            i = input("Enter the short form to get the full form: ")
                            if Full_forms.get(i) != None:
                                print(Full_forms.get(i))
                        elif k == "no":
                            print("                           Thank You")
                            j = 0
                        else:
                            print("          Please say yes or no")
                        m = False
                    else:
                        k = input("          Do You want to continue ?")
                        if k == "yes":
                            i = input("Enter the short form to get the full form: ")
                            if Full_forms.get(i) != None:
                                print(Full_forms.get(i))
                        elif k == "no":
                            print("                           Thank You")
                            j = 0
                        else:
                            print("          Please say yes or no")

            else:
                print("The Entered value is not in the dictionary, Please Try Again")
                i = input("Enter the short form to get the full form: ")
                m  = True
                j -= 1














































