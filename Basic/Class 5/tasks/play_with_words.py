original_text = "Macaroon macaroon tootsie roll jelly-o cotton candy candy brownie pie jelly beans"
final_string = ""

#"text_list = original_text.split()


for index, char in enumerate(original_text):
    if (index+1) % 3 == 0:
        final_string += char.upper()
    elif (index+1) % 4  == 0:
        final_string += f"{char}!"
    else:
        final_string += char

print(final_string)





