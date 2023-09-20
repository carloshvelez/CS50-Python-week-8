from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(25)
    assert jar.capacity == 25
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(5)
    assert jar.size == 6



def test_withdraw():
    jar = Jar(20)
    jar.deposit(15)
    jar.withdraw(5)
    assert jar.size == 10