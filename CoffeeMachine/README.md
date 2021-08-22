### Coffee Machine LLD
To setup run the following command
```
pip3 install virtualenv
virtualenv venv
source <path_to_venv>/bin/activate
pip3 install pytest

```

To run the test enter following command
```
CD <path_to_coffee_machine_code>
EXPORT PYTHONPATH=$PWD
pytest src/tests 
```

Example 
```
cd CoffeeMachine 
export PYTHONPATH=$PWD
pytest src/tests
```
- [Source Code](./src/main)
- [Test](./src/tests)

#### Class Diagram
![Coffee_machine](https://user-images.githubusercontent.com/29228903/130356865-07d0494f-3068-457b-9107-005785a0b9bc.png)


