#Question_1
def Question_1():
    P = 4500
    r = 0.07
    t = 5
    I = P * r * t

    print(f"Question_1: Zar{I:.2f}")


#Question_2
def Question_2():
    P = 12000
    i = 0.065
    n = 8
    A = P * (1 + i) ** n

    print(f"Question_2: Zar{A:.2f}")


#Question 3
def Question_3():
        P = 22000
        D_rate = 0.15
        r = 0.11
        t = 3
        dep = P * D_rate
        pbal = P - dep
        A = pbal * (1 + r * t) // 36
       
        print(f"Question_3: Zar{A:.2f}")
       

#Question_4
def Question_4():
    P = 1550
    i = 0.055
    n = 12
    A = P * (1 + i) ** n

    print(f"question_4: Zar{A:.2f}")


#Question_5
def Question_5():
    P = 480000
    i = 0.18
    n = 6
    A = P * (1 - i) ** n

    print(f"Question_5: Zar{A:.2f}")


#Question_6
def Question_6():
    P = 95000
    r = 0.09
    t = 4
    A = P * (1 + r/4) ** (4 * t)
    
    print(f"Question_6: Zar{A:.2f}")
   

#Question_6
def Question_7():
    P = 30000
    r = 0.14
    A = P*(1 +r/12)**12
    I = A - P

    print(f"Question_7: Zar{I:.2f}")


