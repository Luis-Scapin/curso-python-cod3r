#! python
def get_attr(**kwargs):
    return ' '.join(f'{chave.removeprefix("html_")}="{valor}"' for chave, valor in kwargs.items())


def tag(tag, *args, **kwargs):
    return f'<{tag}{" " if kwargs else ""}{get_attr(**kwargs)}>{"".join(args)}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', ' e '),
            tag('strong', 'Leonardo Leitão', id='ll'),
            tag('span', '.'),
            html_class='alert')
    )
 