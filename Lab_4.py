# Make a function to remove duplicates
def rem_dups(list):
    dedup_list = []
    for number in list:
        if number not in dedup_list:
            dedup_list.append(number)
    return dedup_list

# Initialize the list
int_list = []

# Ask for whole numbers in a loop until ''
while True:
    print('Enter a whole number, or enter nothing to quit')
    int_input = input()
    if int_input == '':
        break
    int_list = int_list + [int_input]

# Remove duplicates and sort
int_list = rem_dups(int_list)
int_list.sort()

# Loop through list contents and print
print('The numbers entered were: ')
for int_input in int_list:
    print(int_input)
