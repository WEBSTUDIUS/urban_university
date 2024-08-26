def all_variants(text):
    for item in text:
        yield item
    for i in range(0, len(text)):
        if i < len(text) - 1:
            yield text[i] + text[i + 1]
        else:
            yield text[0] + text[-1]
    yield text


a = all_variants("abc")
for i in a:
    print(i)
