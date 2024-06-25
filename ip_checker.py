import ipaddress
import subprocess
import platform


def is_valid_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        return True, ip_obj
    except ValueError:
        return False, None


def is_private_ip(ip_obj):
    return ip_obj.is_private


def ping_ip(ip):
    if platform.system().lower() == 'windows':
        ping_cmd = ['ping', '-n', '1', '-w', '1000', str(ip)]
    else:
        ping_cmd = ['ping', '-c', '1', '-W', '1', str(ip)]

    try:
        result = subprocess.run(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5,
                                universal_newlines=True)
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False


def main():
    ip = input("Enter an IP address: ").strip()

    valid, ip_obj = is_valid_ip(ip)
    if not valid:
        print("IP does not exist or is not valid.")
        return

    if is_private_ip(ip_obj):
        print("IP is a Private address.")
        return

    if ping_ip(ip):
        print("Ping successful. The IP is active and pingable.")
    else:
        print("Ping unsuccessful. The IP is not active or not pingable.")


if __name__ == "__main__":
    main()
