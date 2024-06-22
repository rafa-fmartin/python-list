from ft_map import ft_map
from ft_filter import ft_filter


x = [1, 2, 3, 4, 5]
print(list(ft_map(lambda dum: dum+1, x)))
print(list(ft_filter(lambda dum: not (dum % 2), x)))