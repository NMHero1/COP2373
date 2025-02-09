# The program is designed to scan an email and determine the likelihood that the email is a spam message.

# Function to calculate the spam score using a list of keywords
def calculate_spam_score(emailText):

    # Define keywords to identify spam messages
    spamKeywords = [
        "free", "win", "winner", "prize", "congratulations", "click here", "act now",
        "limited time", "urgent", "offer", "money", "guaranteed", "no risk", "buy now",
        "credit card", "discount", "cash", "investment", "miracle", "lottery", "earn",
        "extra income", "best price", "work from home", "cheap", "increase sales", "bonus",
        "order now", "call now", "important information"
    ]

    # Define variables to calculate spam score
    emailTextLower = emailText.lower()
    spamScore = 0
    foundWords = []

    # Iterate through each word in the spam keywords list
    for word in spamKeywords:

        # Check if the current word is contained in the email text
        if word in emailTextLower:

            # Increase the spam score
            spamScore += 1
            foundWords.append(word)

    # Return the spam score and the flagged words
    return spamScore, foundWords

# Function to evaluate the spam likelihood given a spam score
def evaluate_spam_score(score):

    # Compare score
    if score == 0:
        likelihood = "Not Spam"
    elif 1 <= score <= 2:
        likelihood = "Unlikely Spam"
    elif 3 <= score <= 6:
        likelihood = "Possibly Spam"
    elif 7 <= score <= 12:
        likelihood = "Likely Spam"
    else:
        likelihood = "Highly Likely Spam"

    # Return likelihood
    return likelihood

# Main function
def main():

    # Prompt user for the email message
    emailText = input("Enter the email message to analyze: ")

    # Determine the likelihood of a spam message
    spamScore, foundWords = calculate_spam_score(emailText)
    likelihood = evaluate_spam_score(spamScore)

    # Print results
    print("\n--- Spam Analysis Result ---")
    print(f"Spam Score: {spamScore}")
    print(f"Likelihood: {likelihood}")

    # Check if the message had any spam words
    if foundWords:

        # Print the words that were flagged as spam
        print(f"Spam Trigger Words: {','.join(foundWords)}")
    else:
        print("No spam words detected.")

# Call main function
if __name__ == "__main__":
    main()
