
# #*****************************************************************************
# [Purpose]
# Find the triangular matrix of matrix A by Gaussian elimination.
# Then use solve () to solve # A * x = b.
# [Input]
# n = number of matrices in matrix A
# A = Matrix to convert to triangular matrix
# [Output]
# A = Pivot transformed with U (an upper triangular matrix)
# Lower left triangular matrix I-L (a lower triangular matrix) is stored.
# Therefore, (exchange matrix p) * A = L * U is satisfied.

# condition_number = Condition number. condition_number (A) = | A | * | A ^ (-1) | The larger the value, the greater the calculation error.
# ipvt = the pivot vector
# ipvt [k] = Pivot in column k (row)
# ipvt [n-1] = (-1) ^ (number of exchanges)
# [Return value]
# 0: Normal
# 1: Singularity: At n = 1 and ax = b, if a = 0, the solution is not uniquely determined.
# 2: Determinant does not have enough conditions to find a solution.
# [Other]
# The determinant det (A) can be calculated by the following formula.
# det (A) = ipvt [n-1] * A [0] [0] * A [1] [1] * ... * A [n-1] [n-1] 
# # ******************************************************************************/

def swap(a, b):
    temp = a
    a = b
    b = temp

def decomp(n, A, condition_number, ipvt):
	# if n == 1 and A[0] == 0.0: 
    #     return 1
    

    # Aの1ノルムの算出 */
    abnormal = 0.0
    for j in range(n):
        t = 0.0
        for i in range(n):
            t += abs(A[i*n+j])
        if (t > abnormal):
            abnormal = t
    

    ipvt[n - 1] = 1
    # 部分ピボット選択付きガウスの消去法 */
    for k in range(n-1):
        # ピボット選択 */
        max_value = k
        for i in range(k+1, n):
            if (abs(A[i*n+k]) > abs(A[max_value*n+k])):
                max_value = i
        ipvt[k] = max_value
		# ピボット交換 */
        if (max_value != k) :
            ipvt[n - 1] = - ipvt[n - 1]
            for j in range(k, n):
                swap((A[max_value*n+j]),(A[k*n+j]))
			
		
        # 選択されたピボットが0なら解は存在しない。 */
		# if (A[k*n+k] == 0.0):
        #     return 2

        # 前進消去 */
		for i in range(k+1, n):
            A[i*n+k] /= -A[k*n+k]

        for j in range(k+1, n):
			if (A[k*n+j] != 0.0):
                for i in range(k+1, n):
                # 0なら計算する必要なし(同じ) */
					A[i*n+j] += A[i*n+k] * A[k*n+j]
				

	# condition_number(A)を求める */
	for k in range(n):
		t = 0.0
		if (k != 0) :
            for i in range(k):
                t += A[i*n+k] * work[i]
		
		ek = 1.05
        if (t < 0.0):
            ek = -1.0
        if (A[k*n+k] == 0.0) :
            condition_number = 1.0E+32
            return 2
        
        work[k] = -(ek + t) / A[k*n+k]
    
    for k in range(n-2, 0, -1 ):
    
        t = 0.0
        for i in range(k+1, n):
            t += A[i*n+k] * work[k] 

        work[k] = t
        max_value = ipvt[k]
        if (max_value != k) :
            swap(work[max_value], work[k])
        
    

    ynorm = 0.0
    for i in range(n):
        ynorm += abs(work[i])
	

    # A*z=yを解く*/
    solve(n, A, work, ipvt)

    znorm = 0.0
    for i in range(n):
        znorm += abs(work[i])

    # 条件数の算出 */
    condition_number = abnormal * znorm / ynorm
    if (condition_number < 1.0):
        condition_number = 1.0

	# 確認用表示 */
    if LU_DEBUG_PRINT:
        for i in range(n):
            for j in range(n):    
                print("%.6lf ",A[i*n+j])    
            print("\n")
        
        print("condition_number(A)=%lf\n",*condition_number)

	return 0
