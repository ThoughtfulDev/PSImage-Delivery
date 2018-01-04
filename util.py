VER = "0.1.1"

def banner():
    logo = """
    ║ K I R A
    ╔════════ ╗
    ║████████ ║
    ║Ð£A†нηΘ†E║
    ║████████ ║
    ║████████ ║
    ║████████ ║
    ║████████ ║
    ╚════════ Version {0}
    """
    print(logo.format(VER))

def success(msg):
    print('[*] ' +  msg)
def warning(msg):
    print('[!] ' + msg)
def error(msg):
    print('[-] '+ msg)
def info(msg):
    print('[-] '+ msg)
