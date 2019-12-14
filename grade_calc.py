# CSCI-3753 Operating Systems

def main():
    show_classes()
    cl = get_inp()

    if cl == '1':
        os_grade()
    elif cl == '2':
        pl_grade()
    elif cl == '3':
        ds_grade()
    elif cl == '4':
        ro_grade()
    elif cl == '5':
        hc_grade()
    elif cl == '6':
        ai_grade()
    elif cl == '7':
        df_grade()
    elif cl == '8':
        tc_grade()
    elif cl == '9':
        sl_grade()


def show_classes():
    print("Classes: ")
    print("\t1. CSCI-3753 [Operating Systems]")
    print("\t2. CSCI-3155 [Principles of Programming Languages]")
    print("\t3. CSCI-3022 [Data Science]")
    print("\t4. CSCI-3302 [Intro to Robotics]")
    print("\t5. CSCI-3002 [Human Computer Interactions]")
    print("\t6. CSCI-3202 [Intro to AI]")
    print("\t7. CYBR-5830 [Digital Forensics]")
    print("\t8. WRTG-3035 [Technical Communication and Design]")
    print("\t9. ASTR-2040 [Search for Life in the Universe]")



def get_inp():
    while True:
        cl = input("\nselect a class (1-9): ")
        if cl in ('1','2','3','4','5','6','7','8','9'):
            # print("valid: ", cl)
            return(cl)
        else:
            print("\n~~~invalid, try again~~~\n")
            show_classes()
            continue

distribution = [] # generic wight distribution
os_weight = [0.1, 0.1, 0.4, 0.2, 0.2] # quiz, PS, PA, midterm, final
pl_weight = [0.4, 0.4, 0.2] # assignments, midterms, final
ds_weight = [0.35, 0.2, 0.1, 0.1, 0.05, 0.2] # homework, midterm, practicum 1, practicum 2, quizlets, final
ro_weight = [0.3, 0.4, 0.05, 0.25] # homework, lab, attendence, final project
hc_weight = [0.05, 0.2, 0.10, 0.25, 0.4] # participation, assignments, reading, quizzes, project
ai_weight = []
df_weight = [0.1, 0.3, 0.2, 0.2, 0.2] # attendence, projects, labs, midterm, final
tc_weight = []
sl_weight = [0.05, 0.25, 0.2, 0.2, 0.3] # attendence, homework, assignments, midterm, final

# cutoffs:
aa = 93
am = 90
bp = 88
bb = 83
bm = 80
cp = 78
cc = 73
cm = 70
grds = ['A','A-','B+','B','B-','C+','C','C-']


### CLASSES ###

def os_grade():
    print("\nCSCI-3753 Operating Systems")
    print("Enter your grade for each category. Example: '87'")
    w = len(os_weight)
    q = float(input("quiz average: "))
    ps = float(input("problem set average: "))
    pa = float(input("programming assignment average: "))
    m = float(input("midterm grade: "))
    f = 0

    distribution = [q, ps, pa, m, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * os_weight[c])
    get_breakdown(cur, os_weight[w-1])

def pl_grade():
    print("\nCSCI-3155 Principles of Programming Languages")
    print("Enter your grade for each category. Example: '87'")
    w = len(pl_weight)
    a = float(input("assignment average: "))
    m = float(input("midterm average: "))
    f = 0

    distribution = [a, m, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * pl_weight[c])
    get_breakdown(cur, pl_weight[w-1])

def ds_grade():
    print("\nCSCI-3022 Data Science")
    print("Enter your grade for each category. Example: '87'")
    w = len(ds_weight)
    h = float(input("homework average: "))
    p1 = float(input("practicum 1 grade: "))
    p2 = float(input("practicum 2 grade: "))
    q = float(input("quizlets average: "))
    m = float(input("midterm grade: "))
    f = 0

    distribution = [h, p1, p2, q, m, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * ds_weight[c])
    get_breakdown(cur, ds_weight[w-1])

def ro_grade():
    print("\nCSCI-3202 Intro to Robotics")
    print("Enter your grade for each category. Example: '87'")
    w = len(ro_weight)
    h = float(input("homework average: "))
    l = float(input("labs average: "))
    a = float(input("attendence: "))
    f = 0

    distribution = [h, l, a, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * ro_weight[c])
    get_breakdown(cur, ro_weight[w-1])

def hc_grade():
    print("\nCSCI-3002 Human Computer Interaction")
    print("Enter your grade for each category. Example: '87'")
    w = len(hc_weight)
    p = float(input("participation: "))
    a = float(input("assignments average: "))
    r = float(input("reading: "))
    q = float(input("quizes average: "))
    f = 0

    distribution = [p, a, r, q, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * hc_weight[c])
    get_breakdown(cur, hc_weight[w-1])

def ai_grade():
    return(print("AI coming soon"))

def df_grade():
    print("\nCYBR-5830 Digital Forensics")
    print("Enter your grade for each category. Example: '87'")
    w = len(df_weight)
    a = float(input("attendence: "))
    p = float(input("projects average: "))
    l = float(input("labs average: "))
    m = float(input("midterm grade: "))
    f = 0

    distribution = [a, p, l, m, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * df_weight[c])
    get_breakdown(cur, df_weight[w-1])

def tc_grade():
    return(print("Writing coming soon"))

def sl_grade():
    print("\nASTR-2040 Search for Life in the Universe")
    print("Enter your grade for each category. Example: '87'")
    w = len(sl_weight)
    a = float(input("attendence: "))
    h = float(input("homework average: "))
    s = float(input("assignments average: "))
    m = float(input("midterm grade: "))
    f = 0

    distribution = [a, h, s, m, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * sl_weight[c])
    get_breakdown(cur, sl_weight[w-1])

### END cLASSES ###


def get_breakdown(cur, f):
    for i in range(500,0,-1):
        fin = cur + (f * i)

        if aa <= fin:
            faa = i
            if faa <= 1:
                faa = 0
        elif am <= fin < aa:
            fam = i
            if fam <= 1:
                fbp = 0
        elif bp <= fin < am:
            fbp = i
            if fbp <= 1:
                fbb = 0
        elif bb <= fin < bp:
            fbb = i
            if fbb <= 1:
                fbm = 0
        elif bm <= fin < bb:
            fbm = i
            if fbm <= 1:
                fcp = 0
        elif cp <= fin < bm:
            fcp = i
            if fcp <= 1:
                fcc = 0
        elif cc <= fin < cp:
            fcc = i
            if fcc <= 1:
                fcm = 0
        elif cm <= fin < cc:
            fcm = i

    breakdown = [faa, fam, fbp, fbb, fbm, fcp, fcc, fcm]
    print('\nClass grade based on final exam score:')
    for i in range(len(breakdown)):
        print(grds[i], '\t', breakdown[i])
    return()




if __name__ == "__main__":
    main()
