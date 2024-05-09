import pikepdf
from tqdm import tqdm
from tkinter import filedialog
from tkinter import Tk

#Figlet Content(cyber arun)
from colorama import Fore, Style, init;import pyfiglet;init(autoreset=True);print(Fore.CYAN + pyfiglet.figlet_format('Cyber Arun') + Style.RESET_ALL);print(f"{Fore.GREEN}Author   : Arun Sanjeev M S\nGithub   : github.com/arunsanjeevms\n{Fore.GREEN}Disclaimer: This tool is for educational purposes only. Misuse for unauthorized access is prohibited.\n")
###
#  Tkinter
root = Tk()
root.withdraw()  # Hide main window

# Choose the password text file
password_text_file = filedialog.askopenfilename(title="Choose Password Text File ( txt format )")

# Choose the protected PDF file
protected_pdf_file = filedialog.askopenfilename(title="Choose Protected PDF File")

# Empty password list
passwords = []

# each line in txt
with open(password_text_file) as f:
    passwords = [line.strip() for line in f]

for password in tqdm(passwords, "Cracking PDF File"):
    try:
        with pikepdf.open(protected_pdf_file, password=password) as p:
            print(" Password Found :", password)
            break
    except pikepdf._core.PdfError as e:
        print("Error:", e)
        print("PDF file is damaged or Corrupted. Please try another PDF file.")
        break
    except pikepdf.PasswordError as e:
        continue