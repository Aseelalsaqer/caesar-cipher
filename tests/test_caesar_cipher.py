from caesar_cipher.lab18  import encrypt , decrypt, crack




def test_encrypt():
    sample = 'asd'
    shift1 = 1
    shift2 = 2
    shift3 = 6
    actual1 = encrypt(sample, shift1)
    actual2 = encrypt(sample, shift2)
    actual3 = encrypt(sample, shift3)
    
    excpected1 = 'bte'
    excpected2 = 'cuf'
    excpected3 = 'gyj'
    

    assert actual1 == excpected1
    assert actual2 == excpected2
    assert actual3 == excpected3
  


def test_decrypt():
    sample = 'bte'
    shift = 1
    actual = decrypt(sample, shift)
    excpected = 'asd'
    assert actual == excpected


def test_crack():
    sample = 'it was the worst of times'
    encrypted = encrypt(sample, 2)
    actual = crack(encrypted)
    excpected = 'it was the worst of times'
    assert actual == excpected
