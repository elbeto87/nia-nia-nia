def convertor(input_data):

    input_data_lower = input_data.lower()
    exit_data = []
    vocals = ['a', 'e', 'i', 'o', 'u']


    for i, j in enumerate(input_data_lower):
        if input_data_lower[i] in vocals:
            if input_data_lower[i - 1] != 'q' and input_data_lower[i - 1] != 'i':
                exit_data.append("i")
            else:
                if input_data_lower[i - 1] == 'q':
                    exit_data.append("u")
        elif input_data_lower[i] == "y" and (input_data_lower[i - 1] == " " and input_data_lower[i + 1] == " "):
            exit_data.append("i")
        elif input_data_lower[i] == "c" and (input_data_lower[i + 1] == "a" or input_data_lower[i + 1] == "o"):
            exit_data.extend(["q", "u"])
        else:
            exit_data.append(input_data_lower[i])

    result = ''.join(exit_data)

    if input_data.isupper():
        return result.upper()
    else:
        return result.lower()

frase = input("Ingrese una frase a traducir:\n")
print(convertor(frase))