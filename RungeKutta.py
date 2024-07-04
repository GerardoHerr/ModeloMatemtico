
def funcionM(M, R, D, A, F, t):
    tasa_d = 0.23
    fMatriculado = -tasa_d*M
    return fMatriculado

def funcionR(M, R, D, A, F, t):
    tasa_r = 0.14 #0,14
    tasa_ab = 1.154 #1.154
    tasa_rf = 0.35
    fReprobados = tasa_r*M - tasa_ab*R - tasa_rf*F
    return fReprobados

def funcionD(M, R, D, A, F, t):
    tasa_ap = 0.696 #696
    tasa_ab = 0.154 #154 
    tasa_mf = 0.25
    fDesertores = tasa_ab*R - tasa_ap*D + tasa_mf*F
    return fDesertores

def funcionA(M, R, D, A, F, t):
    tasa_ap = 0.696
    fAprobados = tasa_ap*D    
    return fAprobados

def funcionF(M, R, D, A, F, t):
    tasa_mf = 0.25
    tasa_m = 0.80 
    fForaneos = tasa_mf * M - tasa_m * D - tasa_m *  F 
    return fForaneos

def funcionM_1(M, R, D, A, F, t, h):
    k11 = funcionM(M,R,D,A,F,t)
    k21 = funcionR(M,R,D,A,F,t)
    k31 = funcionD(M,R,D,A,F,t)
    k41 = funcionA(M,R,D,A,F,t)
    k51 = funcionF(M,R,D,A,F,t)
    k12 = funcionM(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k22 = funcionR(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k32 = funcionD(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k42 = funcionA(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k52 = funcionF(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k13 = funcionM(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k23 = funcionR(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k33 = funcionD(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k43 = funcionA(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k53 = funcionF(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k14 = funcionM(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k24 = funcionR(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k34 = funcionD(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k44 = funcionA(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k54 = funcionF(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    fM_1 = M + h/6 * (k11+2*k12+2*k13+k14)
    return fM_1

def funcionR_1(M, R, D, A, F, t, h):
    k11 = funcionM(M,R,D,A,F,t)
    k21 = funcionR(M,R,D,A,F,t)
    k31 = funcionD(M,R,D,A,F,t)
    k41 = funcionA(M,R,D,A,F,t)
    k51 = funcionF(M,R,D,A,F,t)
    k12 = funcionM(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k22 = funcionR(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k32 = funcionD(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k42 = funcionA(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k52 = funcionF(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k13 = funcionM(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k23 = funcionR(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k33 = funcionD(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k43 = funcionA(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k53 = funcionF(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k14 = funcionM(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k24 = funcionR(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k34 = funcionD(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k44 = funcionA(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k54 = funcionF(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    fR_1 = R + h/6 * (k21+2*k22+2*k23+k24)
    return fR_1

def funcionD_1(M, R, D, A, F, t, h):
    k11 = funcionM(M,R,D,A,F,t)
    k21 = funcionR(M,R,D,A,F,t)
    k31 = funcionD(M,R,D,A,F,t)
    k41 = funcionA(M,R,D,A,F,t)
    k51 = funcionF(M,R,D,A,F,t)
    k12 = funcionM(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k22 = funcionR(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k32 = funcionD(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k42 = funcionA(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k52 = funcionF(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k13 = funcionM(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k23 = funcionR(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k33 = funcionD(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k43 = funcionA(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k53 = funcionF(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k14 = funcionM(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k24 = funcionR(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k34 = funcionD(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k44 = funcionA(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k54 = funcionF(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    fD_1 = D + h/6 * (k31+2*k32+2*k33+k34)
    return fD_1

def funcionA_1(M, R, D, A, F, t, h):
    k11 = funcionM(M,R,D,A,F,t)
    k21 = funcionR(M,R,D,A,F,t)
    k31 = funcionD(M,R,D,A,F,t)
    k41 = funcionA(M,R,D,A,F,t)
    k51 = funcionF(M,R,D,A,F,t)
    k12 = funcionM(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k22 = funcionR(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k32 = funcionD(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k42 = funcionA(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k52 = funcionF(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k13 = funcionM(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k23 = funcionR(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k33 = funcionD(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k43 = funcionA(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k53 = funcionF(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k14 = funcionM(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k24 = funcionR(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k34 = funcionD(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k44 = funcionA(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k54 = funcionF(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    fA_1 = A + h/6 * (k41+2*k42+2*k43+k44)
    return fA_1

def funcionF_1(M, R, D, A, F, t, h):
    k11 = funcionM(M,R,D,A,F,t)
    k21 = funcionR(M,R,D,A,F,t)
    k31 = funcionD(M,R,D,A,F,t)
    k41 = funcionA(M,R,D,A,F,t)
    k51 = funcionF(M,R,D,A,F,t)
    k12 = funcionM(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k22 = funcionR(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k32 = funcionD(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k42 = funcionA(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k52 = funcionF(M+k11*h/2, R+k21*h/2, D+k31*h/2, A+k41*h/2, F+k51*h/2, t+h/2)
    k13 = funcionM(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k23 = funcionR(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k33 = funcionD(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k43 = funcionA(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k53 = funcionF(M+k12*h/2, R+k22*h/2, D+k32*h/2, A+k42*h/2, F+k52*h/2, t+h/2)
    k14 = funcionM(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k24 = funcionR(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k34 = funcionD(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k44 = funcionA(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    k54 = funcionF(M+k13*h, R+k23*h, D+k33*h, A+k43*h, F+k53*h, t+h)
    fF_1 = F + h/6 * (k51+2*k52+2*k53+k54)
    return fF_1

   #prueba del primer valor
print("MATRICULADOS    APROBADOS     REPRROBADOS   DESERTORES    FORANEOS")
Y1 = 391
Y2 = 313 #313
Y3 = 78
Y4 = 103
Y5 = 9
t = 0
for a in range (6):
    Y1 = funcionM_1(Y1, Y2, Y3, Y4, Y5, t, 0.1)
    Y2 = funcionR_1(Y1, Y2, Y3, Y4, Y5, t, 0.1)
    Y3 = funcionD_1(Y1, Y2, Y3, Y4, Y5, t, 0.1)
    Y4 = funcionA_1(Y1, Y2, Y3, Y4, Y5, t, 0.1)
    Y5 = funcionF_1(Y1, Y2, Y3, Y4, Y5, t, 0.1)
    t = t+0.1
    print(f"{round(Y1)}              {round(Y2)}             {round(Y3)}             {round(Y4)}         {round(Y5)}")

    