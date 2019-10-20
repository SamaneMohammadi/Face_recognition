# Face_recognition

Classification algorithm

Preprocessing step. 

Compute and save the thin QR decompositions of all the Be matrices, 

Be = QeRe, e = 1,2,...,ne. % z is a test image.

Compute zˆ = F T z.

for e = 1,2,...,ne

Solve Reαe = QTe zˆ for αe. for p = 1,2,...,np

If ∥ αe − hp ∥2 < tol, then classify as person p and stop.
