<<<<<<< HEAD
import itertools
from tqdm import tqdm

def calculate_checksum(pin_first_7):
    """
    Calculate the checksum for the last digit of a WPS PIN.
    The checksum is the last digit of the sum of all digits multiplied by 3 plus the sum of alternating digits.
    """
    # Convert the first 7 digits into integers
    digits = [int(d) for d in pin_first_7]
    
    # Calculate the checksum
    total = sum(digits[::2]) * 3 + sum(digits[1::2])
    checksum = (10 - (total % 10)) % 10
    return checksum

def generate_wps_wordlist(output_file="wps_wordlist.txt"):
    """
    Generates all valid WPS PIN combinations and writes them to a file.
    Shows progress using a loading bar.
    """
    # Define the range of digits (0-9) and the length of the first 7 digits of the PIN
    digits = "0123456789"
    pin_length = 7  # First 7 digits; the 8th digit is the checksum

    # Open the output file in write mode
    with open(output_file, "w") as file:
        print(f"Generating valid WPS PIN combinations and saving to '{output_file}'...")
        
        # Calculate the total number of combinations (10^7 = 10,000,000)
        total_combinations = 10**pin_length

        # Use itertools.product to generate all possible combinations for the first 7 digits
        for first_7_digits in tqdm(itertools.product(digits, repeat=pin_length), total=total_combinations, unit="PIN"):
            # Join the tuple into a string (e.g., ('1', '2', '3') -> '123')
            first_7_str = "".join(first_7_digits)
            
            # Calculate the checksum for the last digit
            checksum = calculate_checksum(first_7_str)
            
            # Combine the first 7 digits with the checksum to form the full 8-digit PIN
            wps_pin = first_7_str + str(checksum)
            
            # Write the valid WPS PIN to the file, followed by a newline
            file.write(wps_pin + "\n")

    print(f"WPS PIN wordlist generation complete! Saved to '{output_file}'.")

# Run the program
if __name__ == "__main__":
=======
import itertools
from tqdm import tqdm

def calculate_checksum(pin_first_7):
    """
    Calculate the checksum for the last digit of a WPS PIN.
    The checksum is the last digit of the sum of all digits multiplied by 3 plus the sum of alternating digits.
    """
    # Convert the first 7 digits into integers
    digits = [int(d) for d in pin_first_7]
    
    # Calculate the checksum
    total = sum(digits[::2]) * 3 + sum(digits[1::2])
    checksum = (10 - (total % 10)) % 10
    return checksum

def generate_wps_wordlist(output_file="wps_wordlist.txt"):
    """
    Generates all valid WPS PIN combinations and writes them to a file.
    Shows progress using a loading bar.
    """
    # Define the range of digits (0-9) and the length of the first 7 digits of the PIN
    digits = "0123456789"
    pin_length = 7  # First 7 digits; the 8th digit is the checksum

    # Open the output file in write mode
    with open(output_file, "w") as file:
        print(f"Generating valid WPS PIN combinations and saving to '{output_file}'...")
        
        # Calculate the total number of combinations (10^7 = 10,000,000)
        total_combinations = 10**pin_length

        # Use itertools.product to generate all possible combinations for the first 7 digits
        for first_7_digits in tqdm(itertools.product(digits, repeat=pin_length), total=total_combinations, unit="PIN"):
            # Join the tuple into a string (e.g., ('1', '2', '3') -> '123')
            first_7_str = "".join(first_7_digits)
            
            # Calculate the checksum for the last digit
            checksum = calculate_checksum(first_7_str)
            
            # Combine the first 7 digits with the checksum to form the full 8-digit PIN
            wps_pin = first_7_str + str(checksum)
            
            # Write the valid WPS PIN to the file, followed by a newline
            file.write(wps_pin + "\n")

    print(f"WPS PIN wordlist generation complete! Saved to '{output_file}'.")

# Run the program
if __name__ == "__main__":
>>>>>>> f291145 (updated)
    generate_wps_wordlist()