# Merry Christmas from the BRCS Team!🎅🎄
# Running this code and changing 'Change this' will result in a Christmas card displayed in ASCII art from terminal 🎅🎄

class ChristmasCard:
    """
    Class to generate personalized digital Christmas cards.

    Attributes:
    - design: str
        The design of the Christmas card.
    - message: str
        The message to be displayed on the Christmas card.
    """

    def __init__(self, design: str, message: str):
        """
        Constructor to instantiate the ChristmasCard class.

        Parameters:
        - design: str
            The design of the Christmas card.
        - message: str
            The message to be displayed on the Christmas card.
        """

        self.design = design
        self.message = message

    def generate_card(self, custom_text: str = ""):
        """
        Generates the personalized digital Christmas card.

        Parameters:
        - custom_text: str, optional
            Custom text to be included in the Christmas card. Default is an empty string.

        Returns:
        - str:
            The generated Christmas card as a string.
        """

        # Creating the header of the Christmas card
        card = f"{'*' * 20}\n"
        card += f"{'Merry Christmas!':^20}\n"
        card += f"{'*' * 20}\n\n"

        # Adding the design to the card
        card += f"Design: {self.design}\n\n"

        # Adding the message to the card
        card += f"Message: {self.message}\n\n"

        # Adding the custom text (if provided) to the card
        if custom_text:
            card += f"Custom Text: {custom_text}\n\n"

        # Adding the footer of the Christmas card
        card += f"{'*' * 20}\n"

        return card


# Change this

# XMAS Card with Design and Message
card1 = ChristmasCard("Snowflakes", "Wishing you a joyful holiday season!")
generated_card1 = card1.generate_card()
print(generated_card1)

# XMAS Card with Design and Message and Custom Text
card2 = ChristmasCard("Santa Claus", "May your days be merry and bright!")
custom_text2 = "From: John Doe"
generated_card2 = card2.generate_card(custom_text2)
print(generated_card2)
