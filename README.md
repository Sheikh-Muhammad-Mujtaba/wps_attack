<<<<<<< HEAD

# WPS Attack Tools

This project contains tools for performing WPS attacks on wireless networks. It includes scripts for listing wireless interfaces, scanning for WiFi networks, attempting WPS PIN connections, and generating WPS PIN wordlists.

## Tools and Scripts

- `wps.py`: A script for listing interfaces, scanning WiFi networks, and attempting WPS PIN connections.
- `wps-advance.py`: An advanced script for detecting the OS, installing necessary tools, and cracking WPS PINs.
- `gen_scripts/wps_pin-comb_gen.py`: A script for generating valid WPS PIN combinations.
- `gen_scripts/eight-digit-list-gen.py`: A script for generating all possible 8-digit PIN combinations.

## Setup

### Prerequisites

- Python 3.x
- `uv` (Universal Virtualenv) for managing virtual environments

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Sheikh-Muhammad-Mujtaba/wps_attack.git
    cd wps_attack
    ```

2. Create a virtual environment using `uv`:
    ```sh
    uv new env
    ```

3. Activate the virtual environment:
    ```sh
    uv activate env
    ```

4. Install the required Python packages:
    ```sh
    uv pip install -r requirements.txt
    ```

## Usage

### Running `wps.py`

1. Ensure you have the necessary permissions to run network commands.
2. Run the script:
    ```sh
    uv python wps.py
    ```

### Running `wps-advance.py`

1. Ensure you have the necessary permissions to run network commands.
2. Run the script:
    ```sh
    uv python wps-advance.py
    ```

### Generating WPS PIN Wordlist

1. Navigate to the `gen_scripts` directory:
    ```sh
    cd gen_scripts
    ```

2. Run the WPS PIN combination generator:
    ```sh
    uv python wps_pin-comb_gen.py
    ```

3. Run the 8-digit PIN list generator:
    ```sh
    uv python eight-digit-list-gen.py
    ```

## Notes

- The `wps.py` script is designed for Windows environments and uses `netsh` commands.
- The `wps-advance.py` script supports Linux and Termux environments and uses tools like `aircrack-ng` and `reaver`.
- Ensure you have the necessary permissions and tools installed on your system before running the scripts.

## Disclaimer

These tools are for educational purposes only. Unauthorized access to networks is illegal. Use these tools responsibly and only on networks you own or have explicit permission to test.
=======

# WPS Attack Tools

This project contains tools for performing WPS attacks on wireless networks. It includes scripts for listing wireless interfaces, scanning for WiFi networks, attempting WPS PIN connections, and generating WPS PIN wordlists.

## Tools and Scripts

- `wps.py`: A script for listing interfaces, scanning WiFi networks, and attempting WPS PIN connections.
- `wps-advance.py`: An advanced script for detecting the OS, installing necessary tools, and cracking WPS PINs.
- `gen_scripts/wps_pin-comb_gen.py`: A script for generating valid WPS PIN combinations.
- `gen_scripts/eight-digit-list-gen.py`: A script for generating all possible 8-digit PIN combinations.

## Setup

### Prerequisites

- Python 3.x
- `uv` (Universal Virtualenv) for managing virtual environments

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Sheikh-Muhammad-Mujtaba/wps_attack.git
    cd wps_attack
    ```

2. Create a virtual environment using `uv`:
    ```sh
    uv new env
    ```

3. Activate the virtual environment:
    ```sh
    uv activate env
    ```

4. Install the required Python packages:
    ```sh
    uv pip install -r requirements.txt
    ```

## Usage

### Running `wps.py`

1. Ensure you have the necessary permissions to run network commands.
2. Run the script:
    ```sh
    uv python wps.py
    ```

### Running `wps-advance.py`

1. Ensure you have the necessary permissions to run network commands.
2. Run the script:
    ```sh
    uv python wps-advance.py
    ```

### Generating WPS PIN Wordlist

1. Navigate to the `gen_scripts` directory:
    ```sh
    cd gen_scripts
    ```

2. Run the WPS PIN combination generator:
    ```sh
    uv python wps_pin-comb_gen.py
    ```

3. Run the 8-digit PIN list generator:
    ```sh
    uv python eight-digit-list-gen.py
    ```
[**Note :**  you can use google colab for genrating list](#)
## Notes

- The `wps.py` script is designed for Windows environments and uses `netsh` commands.
- The `wps-advance.py` script supports Linux and Termux environments and uses tools like `aircrack-ng` and `reaver`.
- Ensure you have the necessary permissions and tools installed on your system before running the scripts.

## Disclaimer

These tools are for educational purposes only. Unauthorized access to networks is illegal. Use these tools responsibly and only on networks you own or have explicit permission to test.
>>>>>>> f291145 (updated)
