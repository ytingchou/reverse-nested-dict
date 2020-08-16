import unittest
import solution


class TestSolution(unittest.TestCase):
    def test_reverse(self):
        input_value = {
            'hired': {
                'be': {
                    'to': {
                        'deserve': 'I'
                    }
                }
            }
        }
        result = solution.reverse(input_value)
        target_value = {
            'I': {
                'deserve': {
                    'to': {
                        'be': 'hired'
                    }
                }
            }
        }
        self.assertDictEqual(result, target_value)

if __name__ == '__main__':
    unittest.main()
