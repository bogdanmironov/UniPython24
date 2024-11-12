'''
Задача 2 (1т.)
В академичните публикации е прието при наличие на повече няколко автори с имейли с еднакви домейни, техните имена да се обединяват.

Т.е. за краткост name1@domain, name2@domain се изписват вместо това като {name1,name2}@domain.

Напишете функция emails_shortener, която приема emails (списък от низове) и връща множество (set) от низове, където всички имейли с еднакви домейни са обединени по гореописания начин.

Hint 1: за да разделите низ s по даден символ c, изполвайте s.split(c). Връща лист с всяка разбита част (низ).

Hint 2: низове се слепват с метода join. Например ":".join(["john", "doe", "jr"]) ще върне "john:doe:jr".

Hint 3: в set се добавя елемент с метода add.
'''


def emails_shortener(emails):
    domains = {}
    result = set()

    for email in emails:
        email_split = email.split('@')

        if email_split[1] in domains.keys():
            domains[email_split[1]].append(email_split[0])
        else:
            domains[email_split[1]] = [email_split[0]]

    for key, values in domains.items():
        if len(values) == 1:
            result.add(f'{",".join(values)}@{key}')
        else:
            result.add(f'{{{",".join(values)}}}@{key}')

    return result


assert emails_shortener([
    "pesho@abv.bg",
    "gosho@abv.bg",
    "sasho@abv.bg",
]) == {
    "{pesho,gosho,sasho}@abv.bg"
}

assert emails_shortener([
    "tinko@fmi.uni-sofia.bg",
    "minko@fmi.uni-sofia.bg",
    "pesho@pesho.org",
]) == {
    "{tinko,minko}@fmi.uni-sofia.bg",
    "pesho@pesho.org",
}

assert emails_shortener([
    "toi_e@pesho.org",
    "golemiq@cyb.org",
]) == {
    "toi_e@pesho.org",
    "golemiq@cyb.org",
}

print("✅ All OK! +1 points")