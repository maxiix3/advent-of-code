puzzle = [int(i) for i in open("input.txt").read().split()]

def sumtree(tree):
    child = tree.pop(0)
    meta = tree.pop(0)
    total_sum = 0
    while child > 0:
        total_sum += sumtree(tree)
        child -= 1
    while meta > 0:
        total_sum += tree.pop(0)
        meta -= 1
    return total_sum

print("part 1:", sumtree(puzzle))

def sumvalues(tree, metas=[]):
    child = tree.pop(0)
    meta = tree.pop(0)
    total_sum = 0
    while child > 0:
        meta_list = []
        while meta > 0:
            meta_list.append(tree.pop(0))
        if len(metas) != 0:
            total_sum += sumvalue(tree, meta_list)
        child -= 1
    while meta > 0:
        total_sum += tree.pop(0)
        meta -= 1
    return total_sum
