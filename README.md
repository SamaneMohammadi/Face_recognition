# Face_recognition

The amount of work in this algorithm is high: for each test image z we must solve ne least squares problems with Ce ∈ Rni ×np.

C = S ×i F ×e G, which implies Ce =FBe,

where Be ∈ Rne np ×np is the matrix identified with (S ×e G)(:, e, :). Note that F ∈ R. Then, for the analysis only, enlarge the matrix so that it becomes square and orthogonal:
Fˆ = F F ⊥ , Fˆ T Fˆ = I .
Now insert Fˆ T inside the norm:
∥Cα−z∥2= ∥FˆT(FBα−z)∥ =∥Beαe −FTz∥2 +∥(F⊥)Tz∥2
It follows that we can solve the ne least squares problems by first computing F T z and then solving:
min∥Beαe −FTz∥2, e = 1,2,...,ne.
It is also possible to precompute a QR decomposition of each matrix Be to further reduce the work.
