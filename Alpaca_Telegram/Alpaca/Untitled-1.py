# JuSuhun. PEP8 준수

#1.if문 예제
#x = -1
#if x>0:
#    c = 2
#else:
#    a = -1
#print(c)
#만약 else로 간다면 충돌 발생...

#2. 기본 포함 예제
#import math
#n = math.sqrt(9)
#print(n)

#3. Thread Module
# import threading
# def sum(low, high):
#     total = 0
#     for i in range(low, high):
#         total += 1
#     print("SubTHread", total)
#
# t = threading.Thread(target=sum, args=(1,100000))
# t.start()
#
# print("Main Thread")
## MultiCPU는 multiprocessing Module이용

#4. file 읽기 쓰기
# mode 읽기(r), 쓰기(w,x), 추가(a), 수정(+), 텍스트(t) 바이너리(b)
# Open 이후에 Close를 해주어야 하지만 다음과 같은 경우는 With 구문이 끝나면서 객체를 소멸 시켜서 Close 가 필요 없다.
# with open('test.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         print(line)
#
# with open('test.txt', mode='wt', encoding='utf-8') as f:
#     f.write("Hello, World\n")
#     f.write("안녕하세요?\n")
#     f.write("안녕하세요? 반갑습니다.\n")
#
# with open('test.txt', mode='rt', encoding='utf-8') as f:
#     for line in f:
#         print(line)

#5. CSV File
# import csv
# #write
# with open('data.csv', 'w', encoding='utf-8') as f:
#     wr = csv.writer(f)
#     wr.writerow([1,"김정수", False])
#     wr.writerow([2,"박상미", True])
# # read
# with open('data.csv', 'r', encoding='utf-8') as f:
#     rdr = csv.reader(f)
#     for line in rdr:
#         print(line)

#6. 정규 표현식 Regular Expresstion
# import re
# text = "에러 1122 : 래퍼런스 오류\n 에러 1033: 아규먼트 오류"
# regex = re.compile("에러 1033")
# mo = regex.search(text)
# if mo != None:
#     print(mo.group())
# else:
#     print("Not Find")
#
# text2 = "문의 사항이 있으면 032-232-3245 으로 연락 주시기 바랍니다."
# regex2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# matchobj = regex2.search(text2)
# phonenumber = matchobj.group()
# print(phonenumber)

#7. numpy 사용 예제
# import numpy
# list1 = [1, 2, 3, 4]
# a = numpy.array(list1)
# print(a.shape)
#
# b = numpy.array([[1,2,3],[4,5,6]])
# print(b.shape)
# print(b[0,0])

#8. openpyxl 사용.
# import openpyxl
#
# # 엑셀파일 열기
# wb = openpyxl.Workbook()
#
# ws = wb.active
# ws['A1'] = 'Hellow'
#
# # 엑셀 파일 저장
# wb.save("score2.xlsx")
# wb.close()

#9. make the MCC master List for the signal log
# import openpyxl
#
# wb = openpyxl.Workbook()
# ws = wb.active
# ws.append(['ModulID','Signal Category','No','Log Type','Signal Name','Description', 'ifdef..endif'])
# case_name = []
#
# with open('DefIOAddrAcf_2nd.h', mode='rt', encoding='euc-kr') as f:
# # with open('DefIOAddrPreBonder.h', mode='rt', encoding='euc-kr') as f:
#     for line in f:
#         start = line.find('const unsigned short') + 20 
#         end = line.find('=')
#         dummy = 'DUMMY' in line
#         is_able = start is not 19 and end is not -1 and not dummy
#         if is_able:
#             signal_name = line[start:end].strip()
#             if 'IN_' in signal_name:
#                 signal_name = signal_name.replace("IN_", "X_")
#                 signal_categroy = 'Input'
#             else:
#                 signal_name = signal_name.replace("OUT_", "Y_")
#                 signal_categroy = 'Output'
#             signal_name = signal_name.replace("__", "_")
#             log_type = "S"
#             number = ''
#             module_id = ''
#             description = signal_name[2:]
#             ws.append([module_id,signal_categroy,number,log_type,signal_name, description] + case_name)
#         elif '#' in line:
#             if 'endif' in line:
#                 del case_name[-1]
#             elif 'else' in line:
#                 case_name[-1] = case_name[-1].replace('elif_','else_')
#                 case_name[-1] = case_name[-1].replace('if_','else_')
#             elif 'elif' in line:
#                 case_name[-1] = line[line.find('elif')+4:].strip()
#                 case_name[-1] = case_name[-1].replace('\t','')
#                 case_name[-1] = 'elif_' + case_name[-1]
#             elif 'if' in line:
#                 case_name.append(line[line.find('if')+2:].strip())
#                 case_name[-1] = case_name[-1].replace('\t','')
#                 case_name[-1] = 'if_' + case_name[-1]
#
# # with open('test.txt', mode='wt', encoding='utf-8') as f:
# #     f.write("Hello, World\n")
# #     f.write("안녕하세요?\n")
# #     f.write("안녕하세요? 반갑습니다.\n")
#
# # with open('test.txt', mode='rt', encoding='utf-8') as f:
# #     for line in f:
# #         print(line)
#
# # 엑셀 파일 저장
# wb.save("score2.xlsx")
# wb.close()