import whois
import time

def check_tld_availability(base_name, tld_file="tlds.txt"):
    """Checks availability of a given base name across TLDs from a file."""

    available_tlds = []
    checked = 0

    with open(tld_file, "r") as file:
        for tld in file:
            tld = tld.strip()  # Remove any leading/trailing whitespace (e.g., newlines)
            domain = base_name + tld
            try:
                whois.whois(domain)
            except whois.parser.PywhoisError:
                available_tlds.append(domain)

            checked += 1
            if checked % 10 == 0:
                time.sleep(1)

    return available_tlds

if __name__ == "__main__":
    base_name = input("Enter base domain name: ")
    tld_file = input("Enter TLD file name (or press Enter to use tlds.txt): ")
    if not tld_file:
        tld_file = "tlds.txt"

    available_domains = check_tld_availability(base_name, tld_file)

    if available_domains:
        print("Available domains:")
        for domain in available_domains:
            print(domain)
    else:
        print("No available domains found for the given base name.")
