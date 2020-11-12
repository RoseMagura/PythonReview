# Write your code here
# HINT: create a dictionary from flowers.txt
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

# HINT: create a function to ask for user's first and last name
def main():
    flower_d = create_flowerdict('flowers.txt')
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    try:
        first_letter = first_name[0].lower()
        flower = flower_dict[first_letter]
        # print the desired output
        print("Unique flower name with the same first letter: {}".format(flower))
    except KeyError:
        print('A Key Error exception occured')

main()