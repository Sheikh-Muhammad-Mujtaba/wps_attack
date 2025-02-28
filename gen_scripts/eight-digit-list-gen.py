import itertools
from tqdm import tqdm

def generate_wordlist(output_file="numlist.txt"):
    """
    Generates all possible 8-digit PIN combinations and writes them to a file.
    Shows progress using a loading bar.
    """
    # Define the range of digits (0-9) and the length of the PIN (8 digits)
    digits = "0123456789"
    pin_length = 8

    # Open the output file in write mode
    with open(output_file, "w") as file:
        print(f"Generating 8-digit PIN combinations and saving to '{output_file}'...")
        
        # Calculate the total number of combinations (10^8 = 100,000,000)
        total_combinations = 10**pin_length

        # Use itertools.product to generate all possible combinations
        for pin in tqdm(itertools.product(digits, repeat=pin_length), total=total_combinations, unit="PIN"):
            # Join the tuple into a string (e.g., ('1', '2', '3') -> '123')
            pin_str = "".join(pin)
            
            # Write the PIN to the file, followed by a newline
            file.write(pin_str + "\n")

    print(f"Wordlist generation complete! Saved to '{output_file}'.")

# Run the program
if __name__ == "__main__":
    generate_wordlist()