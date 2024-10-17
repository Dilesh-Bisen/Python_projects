questions = [
    ("'OS' computer abbreviation usually means?", [
     "1. Order of Significance", "2. Open Software", "3. Operating System", "4. Optical Sensor"], 3, 1000),
    ("'.MOV' extension refers usually to what kind of file?", [
     "1. Image file", "2. Animation/movie file", "3. Audio file", "4. MS Office document"], 2, 2000),
    ("What is part of a database that holds only one type of information?", [
     "1. Report", "2. Field", "3. Record", "4. File"], 2, 5000),
    ("What is the capital of France?", [
     "1. Paris", "2. London", "3. Berlin", "4. Madrid"], 1, 10000),
    ("Which gas do plants use for photosynthesis?", [
     "1. Oxygen", "2. Carbon Dioxide", "3. Nitrogen", "4. Hydrogen"], 2, 20000),
    ("Which planet is known as the Red Planet?", [
     "1. Venus", "2. Mars", "3. Jupiter", "4. Saturn"], 2, 10000),
    ("Who wrote the play 'Romeo and Juliet'?", [
     "1. William Shakespeare", "2. Charles Dickens", "3. Jane Austen", "4. Leo Tolstoy"], 1, 50000),
    ("What is the largest mammal?", [
     "1. Elephant", "2. Giraffe", "3. Whale", "4. Hippopotamus"], 3, 100000),
    ("The Grand Central Terminal, Park Avenue, New York is the world's ?", [
     "1. largest railway station", "2. highest railway station", "3. longest railway station", "4. None of the above"], 1, 1000000),
]

total_amount = 0
print("\n")
for question, options, correct_option, prize_amount in questions:
    print(question)
    for option in options:
        print(option)

    user_input = int(input("Select your answer (1-4) : "))

    if user_input == correct_option:
        total_amount += prize_amount
        print("Correct!\n")
    else:
        print("Incorrect!\n")
        break

print("Congratulations! You are taking home Rs.", total_amount)
