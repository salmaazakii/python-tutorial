import utils
from utils import find_max
import ecommerce.shipping
from ecommerce import shipping
from ecommerce.shipping import calc_shipping

print(utils.find_max([5, 8, 3, 1, 9, 4]))
print(find_max([1, 8, 2, 6, 4, 3]))

ecommerce.shipping.calc_shipping()
shipping.calc_shipping()
calc_shipping()
