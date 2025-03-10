# Create Class
class Employee:
  
    # Initializing 
    def __init__(self):
        print('3. Employee created')
  
    # Calling destructor
    def __del__(self):
        print("6. Destructor called")
  
def Create_obj():
    print('2. Making Object...')
    obj = Employee()
    print('4. function end...')
    return obj
  
print('1. Calling Create_obj() function...')
obj = Create_obj()
print('5. Program End...')