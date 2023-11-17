from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def mg(*args):
    print(args)
    return "<p>hello</p>"


@register.simple_tag(takes_context=True)
def mg_model(context, *args):
    for item in context:
        print(item)
        # contents = item.get('block', None)
        # if contents:
        #     print(contents)
    # print(args)
    return mark_safe("value='hi'")


class MGModelNode(template.Node):
    def __init__(self, variables):
        self.variables = variables

    def render(self, context):
        return mark_safe(f"<h2> {self.variables}</h2>")


def do_mg_model(parser, token):
    for k in parser.__dict__:
        print('------------')
        print(k, ": ", parser.__dict__[k])
    # print(parser.__dict__)
    try:
        tag_name, variables = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(f"error on template tag {token.contents.split()[0]}")
    return MGModelNode(variables)


register.tag('do_mg_model', do_mg_model)
