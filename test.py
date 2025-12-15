
import unittest
import time
from exam import safe_execute, SafeExecuteException


class TestSafeExecute(unittest.TestCase):
    
    def test_basic_success(self):
        @safe_execute(max_tries=1)
        def add(a, b):
            return a + b
        
        self.assertEqual(add(2, 3), 5)
    
    def test_retry_on_error(self):
        counter = 0
        
        @safe_execute(max_tries=3)
        def sometimes_fails():
            nonlocal counter
            counter += 1
            if counter < 3:
                raise ValueError("Ще не готово")
            return 
        
        result = sometimes_fails()
        self.assertEqual(result, "Успіх!")
        self.assertEqual(counter, 3)
    
    def test_max_tries_exceeded(self):
        @safe_execute(max_tries=2)
        def always_fails():
            raise RuntimeError("Завжди падає")
        
        with self.assertRaises(SafeExecuteException):
            always_fails()
    
    def test_timeout(self):
        @safe_execute(max_tries=1, timeout=0.1)
        def too_slow():
            time.sleep(0.2)
            return
        
        with self.assertRaises(SafeExecuteException):
            too_slow()
    
    def test_delay_between_tries(self):
        times = []
        
        @safe_execute(max_tries=3, delay=0.05)
        def record_time():
            times.append(time.time())
            if len(times) < 3:
                raise Exception("Ще раз")
            return 
        
        result = record_time()
        self.assertEqual(result, "Готово")
        
        self.assertGreater(times[1] - times[0], 0.04)
        self.assertGreater(times[2] - times[1], 0.04)


if __name__ == "__main__":
    print("Запуск простих тестів...")
    unittest.main()