import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_results = [('ABC', 120.48, 121.2, (120.48 + 121.2) / 2), ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)]
    for i, quote in enumerate(quotes):
      self.assertEqual(getDataPoint(quote), expected_results[i])

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_result = [('ABC', 120.48, 119.2, (120.48 + 119.2) / 2), ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)]
    for i, quote in enumerate(quotes):
      self.assertEqual(getDataPoint(quote), expected_result[i])

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_incompleteData(self):
    incomplete_quote = {'stock': 'XYZ'}
    with self.assertRaises(KeyError):
      getDataPoint(incomplete_quote)
    
  def test_getDataPoint_invalidDataTypes(self):
    invalid_quote = {'stock': 'XYZ', 'top_bid': {'price': 'invalid', 'size': 10}, 'top_ask': {'price': 'invalid', 'size': 5}}
    with self.assertRaises(ValueError):
      getDataPoint(invalid_quote)

  def test_getDataPoint_largeNumbers(self):
    quote = {'stock': 'BIG', 'top_bid': {'price': 1e10, 'size': 100}, 'top_ask': {'price': 1e10 + 1, 'size': 100}}
    expected_result = ('BIG', 1e10, 1e10 + 1, 1e10 + 0.5)
    self.assertEqual(getDataPoint(quote), expected_result)
  
  def test_getDataPoint_zeroPrices(self):
    quote = {'stock': 'ZERO', 'top_bid': {'price': 0, 'size': 100}, 'top_ask': {'price': 0, 'size': 100}}
    expected_result = ('ZERO', 0, 0, 0)
    self.assertEqual(getDataPoint(quote), expected_result)

  def test_getRatio_priceAZero(self):
    self.assertEqual(getRatio(0, 1), 0)

  def test_getRatio_priceBZero(self):
    self.assertIsNone(getRatio(1, 0))

  def test_getRatio_bothPricesZero(self):
    self.assertIsNone(getRatio(0, 0))

  def test_getRatio_normalCondition(self):
    self.assertEqual(getRatio(2, 1), 2)

  def test_getRatio_equalPrices(self):
    self.assertEqual(getRatio(1, 1), 1)


if __name__ == '__main__':
    unittest.main()
