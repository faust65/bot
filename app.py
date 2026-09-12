from flask import Flask, request, jsonify, render_template
import random
import math

app=Flask(__name__)
pk={"스페이드 에이스(1)":1,"스페이드 2":2,"스페이드 3":3,"스페이드 4":4,"스페이드 5":5,"스페이드 6":6,"스페이드 7":7,"스페이드 8":8,"스페이드 9":9,"스페이드 10":10,"스페이드 잭(10)":10,"스페이드 퀸(10)":10,"스페이드 킹(10)":10,
    "하트 에이스(1)":1,"하트 2":2,"하트 3":3,"하트 4":4,"하트 5":5,"하트 6":6,"하트 7":7,"하트 8":8,"하트 9":9,"하트 10":10,"하트 잭(10)":10,"하트 퀸(10)":10,"하트 킹(10)":10,
    "다이아몬드 에이스(1)":1,"다이아몬드 2":2,"다이아몬드 3":3,"다이아몬드 4":4,"다이아몬드 5":5,"다이아몬드 6":6,"다이아몬드 7":7,"다이아몬드 8":8,"다이아몬드 9":9,"다이아몬드 10":10,"다이아몬드 잭(10)":10,"다이아몬드 퀸(10)":10,"다이아몬드 킹(10)":10,
    "클로버 에이스(1)":1,"클로버 2":2,"클로버 3":3,"클로버 4":4,"클로버 5":5,"클로버 6":6,"클로버 7":7,"클로버 8":8,"클로버 9":9,"클로버 10":10,"클로버 잭(10)":10,"클로버 퀸(10)":10,"클로버 킹(10)":10}
pp1=0
pp2=0

@app.route('/')
def html():
    return render_template('index.html')

@app.route('/rl', methods=['POST'])
def rl():
    g=random.randrange(1,101)
    
    if(g<=2):
        message="체력 10 차감"
    elif(g<=7):
        message="x5"
    elif(g<=20):
        message="x4"
    elif(g<=35):
        message="x3"
    elif(g<=55):
        message="x2"
    elif(g<=85):
        message="x1"
    elif(g<=100):
        message="x0"
        
    return jsonify({'message':message})

@app.route('/dice', methods=['POST'])
def dice():
    g="x"+str(random.randrange(1,7))
    return jsonify({'message':g})

@app.route('/cd1', methods=['POST'])
def cd1():
    global pp1, pp2
    p1=random.choice(list(pk.keys()))
    p11=random.choice(list(pk.keys()))
    p2=random.choice(list(pk.keys()))
    p22=random.choice(list(pk.keys()))
    pp1=pk[p1]+pk[p11]
    pp2=pk[p2]+pk[p22]
    if(pp1==21 or pp2==21):
        if(pp1=21):
            p="플레이어"
        elif(pp2=21):
            p="딜"
        return jsonify({'message':f'{pp1}<br><br>{p1}<br>{p11}','message2': f'{pp2}<br><br>{p2}<br>{p22}', 'message3':p+" 블랙잭"})    
    return jsonify({'message':f'{pp1}<br><br>{p1}<br>{p11}','message2': f'{pp2}<br><br>{p2}<br>{p22}'})

@app.route('/hit1', methods=['POST'])
def hit1():
    global pp1
    p1=random.choice(list(pk.keys()))
    pp1+=pk[p1]
    return jsonify({'message':f'{pp1}<br><br>{p1}'})

@app.route('/hit2', methods=['POST'])
def hit2():
    global pp2
    p2=random.choice(list(pk.keys()))
    pp2+=pk[p2]
    return jsonify({'message':f'{pp2}<br><br>{p2}'})

if __name__ == '__main__':
    app.run()