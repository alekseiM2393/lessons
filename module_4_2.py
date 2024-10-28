def test_function():
    def inner_function():
        print("я в области видимости функции est_function")

    inner_function()

test_function()
inner_function()
