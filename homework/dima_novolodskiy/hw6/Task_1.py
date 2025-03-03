text_task = (
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
    'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
)
text_list = text_task.split()
new_text = []
for word in text_list:
    if word.endswith(',') :
        new_word = word.replace(',', 'ing,')
    elif word.endswith('.') :
        new_word = word.replace('.', 'ing.')
    else:
        new_word = word + 'ing'
    new_text.append(new_word)
print(' '.join(new_text))
