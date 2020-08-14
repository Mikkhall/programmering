def run_test(start, end, unsolvable):
    def board(str):
        return [list(row) for row in str.split('\n')]
    print_info(board(start), board(end))
    moves = loopover(board(start), board(end))
    if unsolvable:
        Test.assert_equals(moves, None, 'Unsolvable configuration')
    else:
        Test.assert_equals(check(board(start), board(end), moves), True)

@test.it('Test 2x2 (1)')
def test_2x2_1():
    run_test('12\n34', 
             '12\n34', 
             False)
             
@test.it('Test 2x2 (2)')
def test_2x2_1():
    run_test('42\n31',
             '12\n34',
             False)

@test.it('Test 4x5')
def test_4x5_1():
    run_test('ACDBE\nFGHIJ\nKLMNO\nPQRST',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST',
             False)

@test.it('Test 5x5 (1)')
def test_5x5_1():
    run_test('ACDBE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             False)

@test.it('Test 5x5 (2)')
def test_5x5_2():
    run_test('ABCDE\nKGHIJ\nPLMNO\nFQRST\nUVWXY',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             False)

@test.it('Test 5x5 (3)')
def test_5x5_3():
    run_test('CWMFJ\nORDBA\nNKGLY\nPHSVE\nXTQUI',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             False)

@test.it('Test 5x5 (unsolvable)')
def test_5x5_4():
    run_test('WCMDJ\nORFBA\nKNGLY\nPHVSE\nTXQUI',
             'ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY',
             True)

@test.it('Test 6x6')
def test_6x6():
    run_test('WCMDJ0\nORFBA1\nKNGLY2\nPHVSE3\nTXQUI4\nZ56789',
             'ABCDEF\nGHIJKL\nMNOPQR\nSTUVWX\nYZ0123\n456789',
             False)