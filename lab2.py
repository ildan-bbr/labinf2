def ham(a):
    b = [int(c) for c in a]
    s1 = (b[0]+b[2]+b[4]+b[6])%2
    s2 = (b[1]+b[2]+b[5]+b[6])%2
    s3 = (b[3]+b[4]+b[5]+b[6])%2
    if s1+s2+s3>0:
        badbit = int(str(s3)+str(s2)+str(s1),2)
        b[badbit-1]^=1
        info = ''.join(str(b[i]) for i in (2,4,5,6))
        s = ''.join(str(x) for x in b)
        return (f' ошибка в бите: {badbit},исправленный вид: {s}, правильная информация: {info}')
    else: 
        info = ''.join(str(b[i]) for i in (2,4,5,6))
        return (f'Ошибок нет, правильная информация: {info}')
a = '0100101'
print(ham(a))
