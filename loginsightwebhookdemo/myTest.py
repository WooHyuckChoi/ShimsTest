# ! / usr / bin / env python

"" "
여보세요! 이 템플릿을 사용하면 심을 만드는 데 도움이 될 수 있습니다.
먼저`TEMPLATE`와`template` 매개 변수를 조정하십시오.
그런 다음 webhook 대상의 API 사양을 기반으로 페이로드를 조정합니다.
마지막으로 다음과 같이 import 문을 __init__.py에 추가합니다.
import loginsightwebhookdemo.template
"" "


loginsightwebhookdemo import app, parse, callapi 에서 가져 오기
에서 플라스크 수입 요청, JSON
가져 오기 로깅


__author__ =  " "
__license__ =  " Apache v2 "
__verion__ =  " 1.0 "


# 매개 변수
TEMPLATEURL  =  ' https://wh.jandi.com/connect-api/webhook/15292345/a76ad35760d264ff84ddc964e35efa2f '
# 기본 인증
# TEMPLATEUSER = ''
# TEMPLATEPASS = ''
# 토큰 인증
# TEMPLATETOKEN = ''


# <ALERTID>가없는 경로는 LI 용이며 vROps 용 경로입니다.
@ app.route ( " / endpoint / template " , methods = [ ' POST ' ])
@ app.route ( " / endpoint / template / <ALERTID> " , 방법 = [ ' PUT ' ])
@ app.route ( " / endpoint / template / <TOKEN> " , methods = [ ' POST ' ])
@ app.route ( " / endpoint / template / <TOKEN> / <ALERTID> " , 방법 = [ ' PUT ' ])
@ app.route ( " / endpoint / template / <EMAIL> / <TOKEN> " , 방법 = [ ' POST ' ])
@ app.route ( " / endpoint / template / <EMAIL> / <TOKEN> / <ALERTID> " , 방법 = [ ' PUT ' ])
def  템플릿 ( 알리미 = 없음 , 토큰 = 없음 , 이메일 = 없음 ) :
    "" "
    이 심에 대한 정보.
    TEMPLATE * 매개 변수를 정의해야합니다.
    "" "
    경우 ( 하지  TEMPLATEURL  또는 ( 하지  TEMPLATEUSER  및  되지  이메일 ) 또는 ( 하지  TEMPLATEPASS  및  되지는  TEMPLATETOKEN  및  하지  TOKEN )) :
        return ( " TEMPLATE * 매개 변수를 설정해야합니다. shim을 편집하십시오! " , 500 , 없음 )
     TEMPLATEUSER 가 아닌  경우 :
        USER  =  EMAIL
    else :
        USER  =  TEMPLATEUSER
    # 암호보다 토큰 선호
    경우  TEMPLATETOKEN  또는  토큰 :
        경우  TEMPLATETOKEN :
            USER  =  USER  +  ' / 토큰 '
            통과  =  템플 라틴
        else :
            USER  =  USER  +  ' / 토큰 '
            합격  =  토큰
    else :
        패스  =  템플레이트 패스

    a = 구문 분석 (요청)

    페이로드 = {
        " 본문 " : a [ ' 정보 ' ],
        " connectColor " : " # FAC11B " ,
        " connectInfo " : [{
            " title " : a [ ' AlertName ' ]}]
    }

    # Content-type 기본값 : application / json
    # 변경된 경우 수동으로 content-type을 지정해야합니다
    headers = { ' Content-type ' : ' application / json ' , ' Accept ' : ' application / vnd.tosslab.jandi-v2 + json ' }
     헤더 가 아닌 경우 :
        헤더 =  없음

    # ################
    # 화재 및 분실 시스템
    # ################

    callapi ( TEMPLATEURL , ' post ' , json.dumps (payload), headers)를 반환합니다.

    # #########################################
    # 시스템 점검, 발사 및 삭제
    # 사고 / 티켓 관리 시스템
    # #########################################

    # # 들어오는 webhook의 AlertName을 포함하는 열린 사건 목록을 가져옵니다.
    # incident = callapi (TEMPLATEURL + '/api/v2/search.json?query=type:ticket 상태 : 공개 제목 : "+ a ['AlertName '] +'" ','get ', 없음, 헤더, ( USER, PASS))
    # 시도 :
    #     i = json.loads (사건)
    # except :
    #     사건 접수

    # try : # 이미 열린 사건이 있는지 확인하십시오.
    #     if i [ 'results'] [0] [ 'id']는 None이 아닙니다.
    #         옵션 1 : 아무 것도하지 마라.
    #         # logging.info ( '끝낼 일이 없습니다.')
    #         #return ( "OK", 200, None)

    #         # 옵션 2 : 새 코멘트 추가
    #         payload = { 'ticket': { 'comment': { 'body': a [ 'moreinfo']}}}
    #         return callapi (TEMPLATEURL + '/ api / v2 / tickets /'+ str (i [ '결과'] [0] [ 'id']) + '.json', 'put', json.dumps (페이로드) 헤더, (USER, PASS))
    # except : # 열린 사건이 없다면 하나를 연다.
    #     payload = {
    #         "ticket": {
    #             "subject": a [ 'AlertName'],
    #             "comment": {
    #                 "body": a [ 'moreinfo'],
    #             },
    #             "type": '사건',
    #         }
    #     }
    #     return callapi (TEMPLATEURL + '/api/v2/tickets.json', 'post', json.dumps (페이로드), 헤더, (USER, PASS))
