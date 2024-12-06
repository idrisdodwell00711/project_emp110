import math

def dh_matrix(theta, alpha, R, D):
    stheta = math.sin(theta)
    salpha = math.sin(alpha)
    ctheta = math.cos(theta)
    calpha = math.cos(alpha)
    # Elements 0 to 2 give the rotation, element 4 gives the displacement vector
    DH_matrix = [[ctheta, -stheta*calpha, stheta*salpha, R*ctheta ],
                 [stheta, ctheta*calpha, -ctheta*salpha, R*stheta],
                 [0, salpha, calpha, D],
                 [0,0,0,1]
                ]
    return DH_matrix