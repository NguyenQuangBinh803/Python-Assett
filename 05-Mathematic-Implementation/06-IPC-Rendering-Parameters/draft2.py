
# /******************************************************************************
# 	バイリニア補間(内分比)による歪み補正パラメータ算出
# ******************************************************************************/
def CalDistCorrectByBilinear(self, pecLogFD, num, xl, yl, xlm, ylm, dx, dy, rx, ry, rdx, rdy ):
	# 最大矩形領域を算出
	x_max=xl[0]
	x_min=xl[0]
	y_max=yl[0]
	y_min=yl[0]

	for i in range(4):
		if(xl[i]<x_min): x_min=xl[i]
		if(xl[i]>x_max): x_max=xl[i]
		if(yl[i]<y_min): y_min=yl[i]
		if(yl[i]>y_max): y_max=yl[i]
	
	rx[0] = x_min
	ry[0] = y_min
	rx[1] = x_max
	ry[1] = y_min
	rx[2] = x_min
	ry[2] = y_max
	rx[3] = x_max
	ry[3] = y_max

	# 最大矩形領域での歪み量を算出
	SA1 = np.zeros((NUM4, 1), dtype=float)
	SA2 = np.zeros((NUM4, 1), dtype=float)
	SA3 = np.zeros((NUM4, 1), dtype=float)
	SA4 = np.zeros((NUM4, 1), dtype=float)
	SS = (x_max-x_min) * (y_max-y_min)

	for i in range(4):
		SA1[i] = (x_max-xl[i])*(y_max-yl[i]) / SS
		SA2[i] = (xl[i]-x_min)*(y_max-yl[i]) / SS
		SA3[i] = (x_max-xl[i])*(yl[i]-y_min) / SS
		SA4[i] = (xl[i]-x_min)*(yl[i]-y_min) / SS
	

	A[16] = {	SA1[0],SA2[0],SA3[0],SA4[0],
						SA1[1],SA2[1],SA3[1],SA4[1],
						SA1[2],SA2[2],SA3[2],SA4[2],
						SA1[3],SA2[3],SA3[3],SA4[3] }

	rdx[0] = dx[0]
	rdy[0] = dy[0]
	rdx[1] = dx[1]
	rdy[1] = dy[1]
	rdx[2] = dx[2]
	rdy[2] = dy[2]
	rdx[3] = dx[3]
	rdy[3] = dy[3]

	ipvt = np.zeros((NUM4*NUM4, 1), dtype=float)

	ret = decomp(4, A, condition, ipvt)

	if(ret!=0) :
		return ERR_ALIGNMENT_CAL_NEW_4POINTS
	
	solve(4,A,rdx,ipvt)
	solve(4,A,rdy,ipvt)

	if ALIGNMENT_DEBUG_PRINT:
		print("rx[0],ry[0],rdx[0],rdy[0]:%12.3lf,%12.3lf,%9.3lf,%9.3lf\n",rx[0],ry[0],rdx[0],rdy[0])
		print("rx[1],ry[1],rdx[1],rdy[1]:%12.3lf,%12.3lf,%9.3lf,%9.3lf\n",rx[1],ry[1],rdx[1],rdy[1])
		print("rx[2],ry[2],rdx[2],rdy[2]:%12.3lf,%12.3lf,%9.3lf,%9.3lf\n",rx[2],ry[2],rdx[2],rdy[2])
		print("rx[3],ry[3],rdx[3],rdy[3]:%12.3lf,%12.3lf,%9.3lf,%9.3lf\n",rx[3],ry[3],rdx[3],rdy[3])

	# 演算用歪み補正量の検証
	vdx = np.zeros((NUM4, 1), dtype=float)
	vdy = np.zeros((NUM4, 1), dtype=float)
	for i in range(4):
		vdx[i] = (	(rx[3]-xl[i])*(ry[3]-yl[i])*rdx[0] - 
					(rx[2]-xl[i])*(ry[2]-yl[i])*rdx[1] -
					(rx[1]-xl[i])*(ry[1]-yl[i])*rdx[2] +
					(rx[0]-xl[i])*(ry[0]-yl[i])*rdx[3] ) / ((rx[3]-rx[0])*(ry[3]-ry[0]))
		vdy[i] = (	(rx[3]-xl[i])*(ry[3]-yl[i])*rdy[0] - 
					(rx[2]-xl[i])*(ry[2]-yl[i])*rdy[1] -
					(rx[1]-xl[i])*(ry[1]-yl[i])*rdy[2] +
					(rx[0]-xl[i])*(ry[0]-yl[i])*rdy[3] ) / ((rx[3]-rx[0])*(ry[3]-ry[0]))

	if ALIGNMENT_DEBUG_PRINT:
		print("> verify[%ld](dx=%9.3lf,vdx=%9.3lf)\n",i,dx[i],vdx[i])
		print("> verify[%ld](dy=%9.3lf,vdy=%9.3lf)\n",i,dy[i],vdy[i])

		delta_dx = dx[i]-vdx[i]
		delta_dy = dy[i]-vdy[i]
		if(delta_dx<-1.0 or 1.0<delta_dx):
			return ERR_ALIGNMENT_4PT_VERIFY_DIST_X
		if(delta_dy<-1.0 or 1.0<delta_dy):
			return ERR_ALIGNMENT_4PT_VERIFY_DIST_Y

	return ERR_ALIGNMENT_NOERR
