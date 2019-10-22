A = float(input('请输入您带的钱数：'))
B = int(input('请输入您要买几包零食：'))
lingshi = 8
if A - lingshi * B > 0:
    print('找回' + str(A - lingshi * B) + '元')
else:
    print('还差' + str(lingshi * B - A) + '元')
