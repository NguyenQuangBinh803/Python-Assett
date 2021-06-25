# #**************************************************** *****************************
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
# pivot_vector = the pivot vector
# pivot_vector [k] = Pivot in column k (row)
# pivot_vector [n-1] = (-1) ^ (number of exchanges)
# [Return value]
# 0: Normal
# 1: Singularity: At n = 1 and ax = b, if a = 0, the solution is not uniquely determined.
# 2: Determinant does not have enough conditions to find a solution.
# [Other]
# The determinant det (A) can be calculated by the following formula.
# det (A) = pivot_vector [n-1] * A [0] [0] * A [1] [1] * ... * A [n-1] [n-1]
# # ************************************************ ****************************** /

import numpy as np

LU_DEBUG_PRINT = False


def swap(a, b):
        temp = a
        a = b
        b = temp


def decomp(n, A):
        condition_number = 0
        pivot_vector = np.zeros((n, 1), dtype=float)
        t = 0
        ek = 0
        anorm = 0.0
        ynorm = 0
        znorm = 0
        work = np.zeros((n, 1), dtype=float)

        # if n == 1 and A [0] == 0.0:
        # return 1

        # Calculation of 1 norm of # A * /

        for j in range(n):
                t = 0.0
                for i in range(n):
                        t += abs(A[i * n + j])
                if (t > anorm):
                        anorm = t

        pivot_vector[n - 1] = 1
        # Gaussian elimination with partial pivot selection * /
        for k in range(n - 1):
                # Pivot selection * /
                max_value = k
                for i in range(k + 1, n):
                        if (abs(A[i * n + k]) > abs(A[max_value * n + k])):
                                max_value = i
                pivot_vector[k] = max_value
                # Pivot replacement * /
                if (max_value != k):
                        pivot_vector[n - 1] = - pivot_vector[n - 1]
                        for j in range(k, n):
                                swap((A[max_value * n + j]), (A[k * n + j]))

                                # If the selected pivot is 0, there is no solution. * /
                                # if (A [k * n + k] == 0.0):
                                # return 2

                                # Forward erase * /
                                for i in range(k + 1, n):
                        A[i * n + k] /= -A[k * n + k]

                for j in range(k + 1, n):
                        if (A[k * n + j] != 0.0):
                for i in range(k + 1, n):
                        # No need to calculate if # 0 (same) * /
                        A[i * n + j] += A[i * n + k] * A[k * n + j]

                # Find  condition_number (A) * /
                for k in range(n):
                        t = 0.0
                        if (k != 0):
                                for i in range(k):
                                        t += A[i * n + k] * work[i]

                        ek = 1.05
                if (t < 0.0):
                        ek = -1.0
                if (A[k * n + k] == 0.0):
                        condition_number = 1.0E+32
                        return 2

                work[k] = -(ek + t) / A[k * n + k]

        for k in range(n - 2, 0, -1):

                t = 0.0
                for i in range(k + 1, n):
                        t += A[i * n + k] * work[k]

                work[k] = t
                max_value = pivot_vector[k]
                if (max_value != k):
                        swap(work[max_value], work[k])

        ynorm = 0.0
        for i in range(n):
                ynorm += abs(work[i])

        # A * z = y * /
        solve(n, A, work, pivot_vector)

        znorm = 0.0
        for i in range(n):
                znorm += abs(work[i])

        # Calculation of conditional number * /
        condition_number = anorm * znorm / ynorm
        if (condition_number < 1.0):
                condition_number = 1.0

        # Confirmation display * /
        if LU_DEBUG_PRINT:
                for i in range(n):
                        for j in range(n):
                                print("%.6lf ", A[i * n + j])
                        print("\n")

        print("condition_number(A)=%lf\n", condition_number)

        return 0


def solve(n, A, b, pivot_vector):

        max_value = 0

        # n=1の数式処理 */
        if n == 1:
                b[0] /= A[0]
                return

        # 前進消去で右辺のベクトル(b)に関係する処理 */
        for k in range(n - 1):
                max_value = pivot_vector[k]
                swap(b[max_value], b[k])
                for i in range(k + 1, n):
                        b[i] += A[i * n + k] * b[k]

        # 後進代入 */
        for k in range(n - 1, 0, -1):
                b[k] /= A[k * n + k]
                for i in range(k):
                        b[i] -= A[i * n + k] * b[k]
        b[0] /= A[0]

if __name__ == "__main__":
        A = np.random.rand((5, 5), dtype=float)
        condition_number = abs(np.linalg.det(A)) * abs(np.linalg.det(np.linalg.inv(A)))
        decomp(5, A)
