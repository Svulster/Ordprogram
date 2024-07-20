
def replace_letters(input_file, output_file, old_letter, new_letter):
    try:
        with open(input_file, 'r', encoding="latin") as file:
            content = file.read()

        new_content = content.replace(old_letter,new_letter)

        with open(output_file, 'w', encoding="latin") as file:
            file.write(new_content)
        
        print(f"{old_letter}(s) have been replaced with {new_letter}(s) in {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_file = "ordlista_4bok.txt"
output_file = "ordlista_4bok.txt"

replace_letters(input_file, output_file, " ", "")
