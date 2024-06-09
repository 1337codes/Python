Domain Availability Checker README

**Description:**

This Python script is a domain name availability checker. Given a base domain name (e.g., "yourcompany"), it scans through a comprehensive list of top-level domains (TLDs) and reports which ones are available for registration.

**Features:**

- **Extensive TLD List:** Checks a vast number of TLDs for availability.
- **Rate Limiting:** Includes pauses to avoid being blocked by WHOIS servers.
- **Verbose Output:** Provides real-time feedback on the checking process, highlighting available domains in green.
- **Results File:** Saves the list of available domains to a "results.txt" file.

**Requirements:**

- **Python:** The script requires Python 3.x.
- **python-whois:**  Install this library using `pip3 install python-whois`.

**Usage:**

1. **Create `tlds.txt`:** Prepare a text file named `tlds.txt` (or specify a different filename) containing the TLDs you want to check, one per line (e.g., `.com`, `.net`, `.org`).
2. **Run the Script:** Execute the script from your terminal using `python3 check_tld_availability.py`.
3. **Enter Base Name:** Enter the base domain name you want to check (e.g., "mynewwebsite").
4. **(Optional) Enter TLD File:** If your TLD file has a different name, you can provide it when prompted.
5. **View Results:** The script will print available domains in green to the console, and save the results to "results.txt".

**Example:**

```
python3 check_tld_availability.py
Enter base domain name: mynewwebsite
Enter TLD file name (or press Enter to use tlds.txt): 
Checking: mynewwebsite.com
Checking: mynewwebsite.net
...
Available: mynewwebsite.online 
...
Results also saved to results.txt
```

**Created By:** 1337 Company
