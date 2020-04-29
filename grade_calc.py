# CSCI-3753 Operating Systems

def main():
    show_terms()
    tm = get_term()

    fa19_index = list(i for i in range(1,8)) # list of 1-7
    sp20_index = list(i for i in range(1,6)) # list of 1-5

    if tm == 1:
        show_classes()
        cl = get_inp(fa19_index, 'fa19')
    if tm == 2:
        show_sp20_classes()
        cl = get_inp(sp20_index, 'sp20')


    if tm == 1: # Fall 2019
        if cl == 1:
            os_grade()
        elif cl == 2:
            pl_grade()
        elif cl == 3:
            ds_grade()
        elif cl == 4:
            ro_grade()
        elif cl == 5:
            hc_grade()
        elif cl == 6:
            df_grade()
        elif cl == 7:
            sl_grade()

    if tm == 2:
        if cl == 1:
            sp20_ai_grade()
        elif cl == 2:
            sp20_li_grade()
        elif cl == 3:
            sp20_ru_grade()
        elif cl == 4:
            sp20_pt_grade()
        elif cl == 5:
            sp20_os_grade()


def show_terms():
    print("School Term: ")
    print("\t1. Fall 2019")
    print("\t2. Spring 2020")

def show_classes():
    print("Fall Classes: ")
    print("\t1. CSCI-3753 [Operating Systems]")
    print("\t2. CSCI-3155 [Principles of Programming Languages]")
    print("\t3. CSCI-3022 [Data Science]")
    print("\t4. CSCI-3302 [Intro to Robotics]")
    print("\t5. CSCI-3002 [Human Computer Interactions]")
    print("\t6. CYBR-5830 [Digital Forensics]")
    print("\t7. ASTR-2040 [Search for Life in the Universe]")

def show_sp20_classes():
    print("Spring 2020 Classes: ")
    print("\t1. CSCI-3202 [Intro to Artificial Intelligence]")
    print("\t2. CSCI-4113 [Linux System Administration]")
    print("\t3. RUSS-3241 [Russian Sci-Fi]")
    print("\t4. CYBR-5350 [Penetration Testing]")
    print("\t5. CSCI-3753 [Operating Systems]")

def get_term():
    while True:
        tm = input("\nSelect a school term (1-2): ")
        tm = int(tm)
        if tm in (1,2):
            return(tm)
        else:
            print("\n~~~invalid, try again~~~\n")
            show_terms()
            continue

def get_inp(term_index, term):
    # print(term_index)
    while True:
        cl = input("\nSelect a class (1-{}): ".format(len(term_index)))
        cl = int(cl)
        if cl in term_index:
            return(cl)
        else:
            print("\n~~~invalid, try again~~~\n")
            if term == 'fa19':
                show_classes()
            elif term == 'sp20':
                show_sp20_classes()
            continue

distribution = [] # generic wight distribution
os_weight = [0.1, 0.1, 0.4, 0.2, 0.2] # quiz, PS, PA, midterm, final
pl_weight = [0.4, 0.4, 0.2] # assignments, midterms, final
ds_weight = [0.35, 0.2, 0.1, 0.1, 0.05, 0.2] # homework, midterm, practicum 1, practicum 2, quizlets, final
ro_weight = [0.3, 0.4, 0.05, 0.25] # homework, lab, attendence, final project
hc_weight = [0.05, 0.2, 0.10, 0.25, 0.4] # participation, assignments, reading, quizzes, project
df_weight = [0.1, 0.3, 0.2, 0.2, 0.2] # attendence, projects, labs, midterm, final
sl_weight = [0.05, 0.25, 0.2, 0.2, 0.3] # attendence, homework, assignments, midterm, final

ai_weight = [0.4, 0.2, 0.2, 0.05, 0.05, 0.1] # homework, midterm, endterm, quizlets, participation, practicum
li_weight = [0.3, 0.15, 0.15, 0.1, 0.3] # labs, midterm, endterm, attendence, practical
ru_weight = [0.4, 0.1, 0.15, 0.15, 0.2] # reading, attendence, exam 1, exam 2, final
# pt_weight = [0.3, 0.3, 0.3, 0.1] # assignments, midterm, endterm, final
sp20_os_weight = [0.1, 0.1, 0.4, 0.2, 0.2] # quizzes, problem sets, programming assignments, midterm, final

# cutoffs:
aa = 93
am = 90
bp = 88
bb = 83
bm = 80
cp = 78
cc = 73
cm = 70
dp = 68
dd = 63
dm = 60
grds = ['A','A-','B+','B','B-','C+','C','C-','D+','D','D-']


### CLASSES ###

### FALL 2019 ###

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


### Spring 2020 ###

def sp20_ai_grade():
    print("\nCSCI-3202 Intro to Artificial Intelligence")
    print("Enter your grade for each category. Example: '87'")
    w = len(ai_weight)
    h = float(input("homework average: "))
    m = float(input("midterm exam: "))
    e = float(input("endterm exam: "))
    q = float(input("quizlet average: "))
    p = float(input("participation: "))
    f = 0

    distribution = [h, m, e, q, p, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * ai_weight[c])
    get_breakdown(cur, ai_weight[w-1])

def sp20_li_grade():
    print("\nCSCI-4113 Linux System Administration")
    print("Enter your grade for each category. Example: '87'")
    w = len(li_weight)
    # l1 = float(input("lab 1 grade: "))
    # l2 = float(input("lab 2 grade: "))
    # l3 = float(input("lab 3 grade: "))
    # l4 = float(input("lab 4 grade: "))
    # l5 = float(input("lab 5 grade: "))
    # l6 = float(input("lab 6 grade: "))
    # l = (l1+l2+l3+l4+l5+l6)/6
    l = float(input("lab average: "))
    m = float(input("exam 1 grade: "))
    e = float(input("exam 2 grade: "))
    # e = (e1+e1)/2
    a = float(input("attendence: "))
    f = 0

    distribution = [l, m, e, a, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * li_weight[c])
    get_breakdown(cur, li_weight[w-1])

def sp20_ru_grade():
    print("\nRUSS-3241 Russian Sci-Fi")
    print("Enter your grade for each category. Example: '87'")
    w = len(ru_weight)
    r = float(input("reading check average: "))
    a = float(input("attendence: "))
    m1 = float(input("midterm 1: "))
    m2 = float(input("midterm 2: "))
    f = 0

    distribution = [r, a, m1, m2, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * ru_weight[c])
    get_breakdown(cur, ru_weight[w-1])

def sp20_pt_grade():
    print("CYBR-5350 Penetration Testing")
    print("Canvas grade book not updated, cannot perform breakdown")
    return

def sp20_os_grade():
    print("\nCSCI-3753 Operating Systems")
    print("Enter your grade for each category. Example: '87'")
    w = len(sp20_os_weight)
    q = float(input("quiz average: "))
    ps = float(input("problem set average: "))
    pa = float(input("programming assignment average: "))
    m = float(input("midterm grade: "))
    f = 0

    distribution = [q, ps, pa, m, f]
    cur = 0
    for c in range(w-1):
        cur += (distribution[c] * sp20_os_weight[c])
    get_breakdown(cur, sp20_os_weight[w-1])

### END cLASSES ###


def get_breakdown(cur, f):

    faa, fam, fbp, fbb, fbm, fcp, fcc, fcm, fdp, fdd, fdm = 0,0,0,0,0,0,0,0,0,0,0

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
            if fcm <= 1:
                fdp = 0
        elif dp <= fin < cm:
            fdp = i
            if fdp <= 1:
                fdd = 0
        elif dd <= fin < dp:
            fdd = i
            if fdd <= 1:
                fdm = 0
        elif dm <= fin < dd:
            fdm = i

    breakdown = [faa, fam, fbp, fbb, fbm, fcp, fcc, fcm, fdp, fdd, fdm]
    print('\nClass grade based on final exam score:')
    for i in range(len(breakdown)):
        print(grds[i], '\t', breakdown[i])
    return()




if __name__ == "__main__":
    main()
