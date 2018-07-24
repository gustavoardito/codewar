def title_case(title, minor_words):
    ignore_minor = True
    r = ''
    for t in title.lower().split(' '):
        r += ' {}'.format(
            t.capitalize()
            if ignore_minor or t not in minor_words.lower().split(' ')
            else t
        )
        ignore_minor = False

    return r[1:]

def title_case_best_solution(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
