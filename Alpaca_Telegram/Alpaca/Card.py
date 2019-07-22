import re

def HotCommand(msg):
	if '지출 정리' in msg:
		result = "[지출 정리]\n";
		msg = msg.replace(',', '')
		msg_list = msg.split('/')

		A = int(msg_list[1])
		B = int(msg_list[2])
		C = int(msg_list[3])
		D = int(msg_list[4])

		result += "누적 : " + format(A, ',') + '\n'
		result += "잔여할부금 : " + format(B, ',') + '\n'
		result += "이번달 결제 대금 : " + format(C, ',') + '\n'
		result += "현제 계좌 잔액 : " + format(D, ',') + '\n'
		result += "이번달 지출 : " + format(-A+B+C, ',') + '\n'
		result += "이번달 지출 계 : " + format(-A+B+C+D, ',') + '\n'
		result += "잔여 지출 계 : " + format(-A+C+D, ',') + '\n'
		return result
	else:
		return "잘못된 입력 입니다."

	
#format(값, "형식규칙") 혹은
#"{형식규칙}".format(값)


#개인 지출 정리

#누적 : 2,002,649
#잔여할부금 : 863,500 (8, 9, 10, 11, 12)
#이번달 결제 대금 : 0
#현제 계좌 잔액 : 0
#이번달 지출 : 1,139,149‬
#이번달 지출 계 : -1,139,149‬
#잔여 지출 계 : -2,002,649

#지출 정리 2,002,649 / 863,500 / 0 / 0