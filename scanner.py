import nmap

def scan_target(target):
    scanner = nmap.PortScanner()

    print(f"\n[+] Iniciando varredura no alvo: {target}\n")

    try:
        scanner.scan(hosts=target, arguments='-sV')
    except Exception as e:
        print(f"[ERRO] Falha ao executar o scan: {e}")
        return

    for host in scanner.all_hosts():
        print(f"Host: {host}")
        print(f"Estado: {scanner[host].state()}")

        for protocol in scanner[host].all_protocols():
            print(f"\nProtocolo: {protocol}")

            ports = scanner[host][protocol].keys()
            for port in sorted(ports):
                service = scanner[host][protocol][port].get('name', 'desconhecido')
                state = scanner[host][protocol][port].get('state', 'desconhecido')
                print(f"Porta: {port} | Estado: {state} | Serviço: {service}")

if __name__ == "__main__":
    target = input("Digite o IP ou rede para varredura: ")
    scan_target(target)

