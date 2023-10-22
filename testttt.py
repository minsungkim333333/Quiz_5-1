class sabb:
    def __init__(self,jrb,nmb,gyr,kind):
        self.jrb=jrb
        self.nmb=nmb
        self.gyr=gyr
        self.kind=kind
        self.money=0
    def sab(self):
        dsy = self.jrb+self.nmb
        if dsy < 500000000 and self.kind == '일반건설공사_갑':
            rate=0.0293
            result= dsy*rate
        elif 5000000000 > dsy >= 500000000 and self.kind == '일반건설공사_갑':
            rate=0.0186
            result= dsy*rate+5349000
        elif 5000000000 >= dsy and self.kind == '일반건설공사_갑':
            rate=0.0197
            result= dsy*rate
        elif dsy < 500000000 and self.kind == '일반건설공사_을':
            rate=0.0309
            result= dsy*rate
        elif 5000000000 > dsy >= 500000000 and self.kind == '일반건설공사_을':
            rate=0.0199
            result= dsy*rate+5499000
        elif 5000000000 >= dsy and self.kind == '일반건설공사_을':
            rate=0.0210
            result= dsy*rate
        elif dsy < 500000000 and self.kind == '중건설공사':
            rate=0.0343
            result= dsy*rate
        elif 5000000000 > dsy >= 500000000 and self.kind == '중건설공사':
            rate=0.0235
            result= dsy*rate+5400000
        elif 5000000000 >= dsy and self.kind == '중건설공사':
            rate=0.0244
            result= dsy*rate
        elif dsy < 500000000 and self.kind == '철도궤도신설공사':
            rate=0.0245
            result= dsy*rate
        elif 5000000000 > dsy >= 500000000 and self.kind == '철도궤도신설공사':
            rate=0.0157
            result= dsy*rate+4411000
        elif 5000000000 >= dsy and self.kind == '철도궤도신설공사':
            rate=0.0166
            result= dsy*rate
        elif dsy < 500000000 and self.kind == '특수및기타건설공사':
            rate=0.0185
            result= dsy*rate
        elif 5000000000 > dsy >= 500000000 and self.kind == '특수및기타건설공사':
            rate=0.0120
            result= dsy*rate+3250000
        elif 5000000000 >= dsy and self.kind == '특수및기타건설공사':
            rate=0.0127
            result= dsy*rate
        self.moeny=self.money + result
        return print('안전관리비는' + str(result) +'원 입니다.')
    def rule(self):
        if 70 > self.gyr >= 50:
            spend_rule = self.money * 0.5
            print('안전관리비를 ' + str(spend_rule) +'원 이상 사용하여야 합니다.')
        elif 90 > self.gyr >= 70:
            spend_rule = self.money * 0.7
            print('안전관리비를 ' + str(spend_rule) +'원 이상 사용하여야 합니다.')
        elif self.gyr >= 90:
            spend_rule = self.money * 0.9
            print('안전관리비를 ' + str(spend_rule) +'원 이상 사용하여야 합니다.')
        else:
            print('안전관리비 사용 기준금액이 정해져있지 않습니다. 자유롭게 사용 가능합니다.')
        return spend_rule
test=sabb(4000000000,500000000,82,'일반건설공사_갑')
test.sab()
test.rule()
