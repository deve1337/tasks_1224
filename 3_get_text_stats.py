def get_text_stats(x):
    symbol_count = 0
    sentence_count = 0
    maybe_ellipsis = False

    for c in x:
        if c.isalnum():
            symbol_count += 1

        # Если сейчас точка и до этого была точка - пропускаем итерацию
        if c == "." and maybe_ellipsis:
            continue

        # если до сюда дошли - сейчас либо не точка либо это первая точка
        maybe_ellipsis = False

        if c == ".":
            sentence_count += 1
            maybe_ellipsis = True

    return symbol_count, sentence_count


text = "Взаимно простыми числами называются такие числа, которые не имеют общих делителей, кроме единицы... Это значит, что наибольший общий делитель (НОД) таких чисел равен 1. Числа 8 и 15 взаимно простые, потому что их единственный общий делитель - 1."
symbol_count, sentence_count = get_text_stats(text)
print("Количество символов:", symbol_count)
print("Количество предложений:", sentence_count)
