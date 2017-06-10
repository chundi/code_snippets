# -*- coding:utf-8 -*-

def reverse_linked_list(link):
    if link.next is None: return link
    def reverse(head, next):
        if next is None: return head
        third = next.next
        next.next = head
        return reverse(next, third)
    reversed_first = reverse(link, link.next)
    link.next = None
    return reversed_first

def print_link(head):
    curr = head
    while True:
        print("{0}".format(curr.name))
        curr = curr.next
        if not curr: break

if __name__ == '__main__':
    class Item(object):
        def __init__(self, name, _next):
            self.name = name
            self.next = _next

    g = Item('g', None)
    f = Item('f', g)
    e = Item('e', f)
    d = Item('d', e)
    c = Item('c', d)
    b = Item('b', c)
    a = Item('a', b)

    print_link(a)
    first = reverse_linked_list(a)
    print('-'*80)
    print_link(first)

