import tkinter as tk

class CreditCardVerifier(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Credit Card Verifier")
        self.geometry("400x250")

        self.card_number_label = tk.Label(self, text="Enter Credit Card Number:")
        self.card_number_label.pack()

        self.card_number_entry = tk.Entry(self)
        self.card_number_entry.pack()

        self.verify_button = tk.Button(self, text="Verify", command=self.verify_card)
        self.verify_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        self.card_issuer_label = tk.Label(self, text="")
        self.card_issuer_label.pack()

        self.instructions_label = tk.Label(self, text="Instructions:\n"
                                                     "1. Enter the credit card number without spaces.\n"
                                                     "2. Click the 'Verify' button to check its validity.")
        self.instructions_label.pack()

        self.author_label = tk.Label(self, text="Developed by: Your Name")
        self.author_label.pack()

    def verify_card(self):
        card_number = self.card_number_entry.get().replace(" ", "")
        if self.is_valid_card(card_number):
            self.result_label.config(text="Valid Credit Card", fg="green")
        else:
            self.result_label.config(text="Invalid Credit Card", fg="red")

    def is_valid_card(self, card_number):
        # Remove any non-digit characters
        card_number = ''.join(filter(str.isdigit, card_number))

        if not 13 <= len(card_number) <= 19:
            return False

        # Check for Visa (starts with 4 and has 16 digits)
        if card_number[0] == '4' and len(card_number) == 16:
            self.card_issuer_label.config(text="Issuer: Visa")
            return self.luhn_algorithm(card_number)

        # Check for Amex (starts with 34 or 37 and has 15 digits)
        if card_number[:2] in ['34', '37'] and len(card_number) == 15:
            self.card_issuer_label.config(text="Issuer: American Express")
            return self.luhn_algorithm(card_number)

        # Check for American Express (starts with 3 and has 15 digits)
        if card_number[0] == '3' and len(card_number) == 15:
            self.card_issuer_label.config(text="Issuer: Amex")
            return self.luhn_algorithm(card_number)

        self.card_issuer_label.config(text="Issuer: Unknown")
        return False

    def luhn_algorithm(self, card_number):
        total = 0
        reverse_digits = card_number[::-1]
        for i, digit in enumerate(reverse_digits):
            num = int(digit)
            if i % 2 == 1:
                num *= 2
                if num > 9:
                    num -= 9
            total += num

        return total % 10 == 0

if __name__ == "__main__":
    app = CreditCardVerifier()
    app.mainloop()
