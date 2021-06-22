import numpy as np
import math

from ParamtersClasses import *
from SystemErrorCode import *

xl = np.zeros((MAX_MARK_NUM, 1), dtype=float)
yl = np.zeros((MAX_MARK_NUM, 1), dtype=float)
xm = np.zeros((MAX_MARK_NUM, 1), dtype=float)
ym = np.zeros((MAX_MARK_NUM, 1), dtype=float)

xml = np.zeros((MAX_MARK_NUM, 1), dtype=float)
yml = np.zeros((MAX_MARK_NUM, 1), dtype=float)
dx = np.zeros((MAX_MARK_NUM, 1), dtype=float)
dy = np.zeros((MAX_MARK_NUM, 1), dtype=float)
dr = np.zeros((MAX_MARK_NUM, 1), dtype=float)
dxAdj = np.zeros((MAX_MARK_NUM, 1), dtype=float)
dyAdj = np.zeros((MAX_MARK_NUM, 1), dtype=float)
dist_dx = np.zeros((MAX_MARK_NUM, 1), dtype=float)
dist_dy = np.zeros((MAX_MARK_NUM, 1), dtype=float)
dist_dr = np.zeros((MAX_MARK_NUM, 1), dtype=float)


#ifndef __linux__
def llround (x) :
    if x > 0.0 :
        return int(floor(x + 0.5))
    else:
        return int(-1.0 * floor(abs(x) + 0.5))

#endif


class RenderingParametersForwardMathematicalModel():
    directionTemp1 = SDirection(0,0,0,0,0,0,0,0,0)
    directionTemp2 = SDirection(0,0,0,0,0,0,0,0,0)
    alignmentParamTemp1 = SAlignmentParam(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    vectorParamTemp1 = SVectorParam(0,0,0,0,0,0,0,0,0,0,0)

    def __init__(self):
        pass

    # calcRenderingPrmLib_calcRenderingPrm_for_div
    def MathematicalCore(self, pecLogFD, JobId, subJobID, boradNum, revice_mode, markNum, designPos, measurePos, planePos, tranceform_mode, alignMode, planeInfo, divInfo, distControl, outAlignParam, outRenderingParam):
        '''
        int calcRenderingPrmLib_calcRenderingPrm_for_div(
        int				pecLogFD,
        const int		JobId,
        const int		subJobID,
        const int		boradNum,
        const int		revice_mode,
        const int		markNum,
        const MARK_DT	designPos,				# TP609 200�����Ή� 
        const MARK_DT 	measurePos,			# TP609 200�����Ή� 
        const MARK_DT	planePos[2],
        const int		/*tranceform_mode*/,
        const int		/*alignMode*/,
        const			PlaneAlignInfo* planeInfo,
        const			DivAlignInfo*	divInfo,
        const			DistControl*	distControl,
        AlignmentParam*	outAlignParam,
        RenderingParam*	outRenderingParam )
        '''

        # Input Paramters 
        divInfo = DivAlignInfo()

        i = 0
        markIdx = 0
        ret = 0
        idx = 0
        start_num = 0
        mNum = 0
        mark_id = 0 
        divCnt = 0
        divNum = 0
        divNum = divInfo.divnum_x * divInfo.divnum_y

        if divNum == 0:
            return ERR_ALIGNMENT_INVALID_AREA_NUM
        

        # �p�����[�^�`�F�b�N(�����̈�}�[�N�_�� 2�_or4�_)
        for divCnt in range(0, divNum):

            # �p�����[�^�`�F�b�N(�����̈�}�[�N�_�� 2�`800�_)
            if divInfo.markNum[divCnt] < 2 or MAX_MARK_NUM_DIVIDE_AREA < divInfo.markNum[divCnt]:
                return ERR_ALIGNMENT_MARK_NUM

        
        # ��{���̎Z�o
        kx_plane=0.0
        ky_plane=0.0
        kx_ave_area=0.0
        ky_ave_area=0.0

        self.CalcScalingPlane(pecLogFD, JobId, subJobID, boradNum, markNum, designPos,	measurePos,	kx_plane, ky_plane)

        self.CalcScalingAveArea(pecLogFD, JobId,	subJobID, boradNum,markNum, designPos,	measurePos,	divInfo, kx_ave_area, ky_ave_area )

    def CalcScalingPlane(self, pecLogFD,JobId,subJobID,boradNum,markNum, designPos, measurePos,	kx_plane, ky_plane ):
        i = 0 
        ret = 0
        # TP609 200�����Ή� �e���|�����̈�̃��[�J���ϐ���p�~
        markInfo = SMarkInfo(0,0,0,0,0,0)
        
        # TP609 200�����Ή� �e���|�����̈�̃��[�J���ϐ���p�~
        #[S] #1487 3�_�A���C�����g�Ή�
        idx = 0
        #[E] #1487 3�_�A���C�����g�Ή�
        markInfo.num = markNum		# TP609 200�����Ή� �e���|�����̈�̃��[�J���ϐ���p�~
        #[S] #1487 3�_�A���C�����g�Ή�
        idx = 0
        for i in range(markNum):
            if measurePos[i].x == 88888888:
                markInfo.num -= 1		# TP609 200�����Ή� �e���|�����̈�̃��[�J���ϐ���p�~
                continue
            
            # TP609 200�����Ή� �e���|�����̈�̃��[�J���ϐ���p�~
            markInfo.xlog[idx]= designPos [i].x
            markInfo.ylog[idx]= designPos [i].y
            markInfo.xmes[idx]= measurePos[i].x
            markInfo.ymes[idx]= measurePos[i].y
            idx += 1
        

        #[E] #1487 3�_�A���C�����g�Ή�

        # TP609 200�����Ή� �e���|�����̈�̃��[�J���ϐ���p�~
        directionPanel = self.directionTemp1
        directionArray = self.directionTemp2
        
        directionPanel.scalingMode = RPL_SCALING_AUTO
        directionPanel.kx = 0.0
        directionPanel.ky = 0.0
        directionArray.scalingMode = RPL_SCALING_AUTO		# �c�ݕ␳���̔[���ӕ�(�̈�0)�̓X�P�[�����O���[�h(�c�ݕ␳����)�Ƃ���B
        directionArray.kx = 0.0
        directionArray.ky = 0.0

        # �����p-�A���C�����g�p�����[�^
        alignmentParam = self.alignmentParamTemp1
        # �����p-�x�N�^�p�����[�^
        vectorParam = self.vectorParamTemp1
        # TP609 200�����Ή� �e���|�����̈�̃��[�J���ϐ���p�~

        ret = self.CalAlignmentParam(pecLogFD, False, directionPanel,markInfo,alignmentParam,vectorParam)		#������2000�������� �e���|�����̈�̃��[�J���ϐ���p�~
        
        if ret!=ERR_ALIGNMENT_NOERR :
            return ret
        
        kx_plane = alignmentParam.kx		# TP609 200�����Ή� �e���|�����̈�̃��[�J���ϐ���p�~
        ky_plane = alignmentParam.ky		# TP609 200�����Ή� �e���|�����̈�̃��[�J���ϐ���p�~

        return 0
    



    def CalAlignmentParam(self, pecLogFD, bDistSW, pDirection,pMarkInfo,pAlignParam,pVecotorParam):
        global xl
        global yl
        global xm
        global ym

        global xml
        global yml
        global dx
        global dy
        global dr
        global dxAdj
        global dyAdj
        global dist_dx
        global dist_dy
        global dist_dr
        i = 0
        ret = 0 
        tmpNum = 0

        # �v���{���̎Z�o�p
        kxMes = 0.0
        kyMes = 0.0

        if  pDirection.scalingMode!=RPL_SCALING_FIX and pDirection.scalingMode!=RPL_SCALING_AUTO and pDirection.scalingMode!=RPL_DIST_AFFINE and pDirection.scalingMode!=RPL_DIST_BILINEAR :
            return ERR_ALIGNMENT_SCALING_PARAM

        # TP609 200�����Ή� 
        # TP609 200�����Ή� 

        #[S] #1487 3�_�A���C�����g�Ή�
        for i in range(pMarkInfo.num):
            if pMarkInfo.xmes[i] == 88888888:
                continue
            xl[i]=pMarkInfo.xlog[i]
            yl[i]=pMarkInfo.ylog[i]
            xm[i]=pMarkInfo.xmes[i]
            ym[i]=pMarkInfo.ymes[i]

        # �\���E���J����p�̃I�t�Z�b�g���Z�o
        sum_xl=0
        sum_yl=0
        sum_xm=0
        sum_ym=0
        tmpNum = pMarkInfo.num
        for i in range(pMarkInfo.num):
            if pMarkInfo.xmes[i] == 88888888:
                tmpNum-= 1
                continue
            sum_xl+=pMarkInfo.xlog[i]
            sum_yl+=pMarkInfo.ylog[i]
            sum_xm+=pMarkInfo.xmes[i]
            sum_ym+=pMarkInfo.ymes[i]

        # [S]TP#1559 2000�������PStep1 NG�s�[�X�Ή�
        if tmpNum <= 0:
            return ERR_ALIGNMENT_MARK_NUM			# 0�����Ȃ��悤�ɃK�[�h��ǉ�

        # [E]TP#1559 2000�������PStep1 NG�s�[�X�Ή�
        pAlignParam.gx = llround(sum_xl / tmpNum)
        pAlignParam.gy = llround(sum_yl / tmpNum)
        pAlignParam.ofsx = llround((sum_xm - sum_xl) / tmpNum)
        pAlignParam.ofsy = llround((sum_ym - sum_yl) / tmpNum)
        #[E] #1487 3�_�A���C�����g�Ή�

        # �{���̐ݒ�
        theta = 0
        kx = 0
        ky = 0
        ofsx = 0
        ofsy = 0
        
        if 	pDirection.scalingMode==RPL_SCALING_FIX:				# �w��{�����g�p
            # �����~�X���^����w��{���̓G���[�Ƃ���
            if pDirection.kx<0.95 or 1.05<pDirection.kx:
                return ERR_ALIGNMENT_KX_VALUE
            
            if pDirection.ky<0.95 or 1.05<pDirection.ky:
                return ERR_ALIGNMENT_KY_VALUE
            
            kx = pDirection.kx
            ky = pDirection.ky
        elif pDirection.scalingMode==RPL_SCALING_AUTO or pDirection.scalingMode==RPL_DIST_AFFINE or pDirection.scalingMode==RPL_DIST_BILINEAR:	#�{���������v�Z
            kx = 0.0
            ky = 0.0
        

        # ��]/�{��/�I�t�Z�b�g���Z�o
        if pMarkInfo.num == 2:
            ret = self.CalThetaKxKyOfsFor2Points(pecLogFD,xl,yl,xm,ym,theta,kxMes,kyMes,ofsx,ofsy)			# �����{��
            if ret!=ERR_ALIGNMENT_NOERR:
                return ret
            ret = self.CalThetaKxKyOfsFor2Points(pecLogFD,xl,yl,xm,ym,theta,kx,ky,ofsx,ofsy)				# �I����{��
            if ret!=ERR_ALIGNMENT_NOERR:
                return ret
        else :
            ret = self.CalThetaKxKyOfsByLSM(pecLogFD,pMarkInfo.num,xl,yl,xm,ym,theta,kxMes,kyMes,ofsx,ofsy) # �����{��
            if ret!=ERR_ALIGNMENT_NOERR:
                ret = self.CalThetaKxyOfsByLSM(pecLogFD,pMarkInfo.num,xl,yl,xm,ym,theta,kxMes,kyMes,ofsx,ofsy)
                if ret!=ERR_ALIGNMENT_NOERR:
                    return ret
            
            ret = self.CalThetaKxKyOfsByLSM(pecLogFD,pMarkInfo.num,xl,yl,xm,ym,theta,kx,ky,ofsx,ofsy)		# �I����{��
            if ret!=ERR_ALIGNMENT_NOERR:
                ret = self.CalThetaKxyOfsByLSM(pecLogFD,pMarkInfo.num,xl,yl,xm,ym,theta,kx,ky,ofsx,ofsy)
                if ret!=ERR_ALIGNMENT_NOERR:
                    return ret

        # �Z�o���ꂽ��]/�{��/�I�t�Z�b�g�ő�����W��݌v���W��֕ϊ�
        # �}�[�N����l�̎Z�o
        # TP609 200�����Ή� 
        # TP609 200�����Ή� 

        for i in range(pMarkInfo.num):
            if xm[i] == 88888888:
                xml[i] = 0
                yml[i] = 0
                dist_dx[i] = 0
                dist_dy[i] = 0
                dist_dr[i] = 0
            else :
                xml[i]= (xm[i] - ofsx) * math.cos(-theta) - (ym[i]- ofsy) * math.sin(-theta)
                yml[i]= (xm[i] - ofsx) * math.sin(-theta) + (ym[i]- ofsy) * math.cos(-theta)
                dist_dx[i] = xml[i] - (xl[i] * kx)
                dist_dy[i] = yml[i] - (yl[i] * ky)
                dist_dr[i] = math.sqrt(dist_dx[i]*dist_dx[i]+dist_dy[i]*dist_dy[i])

        # ��]�E�{���E�I�t�Z�b�g������̎c��
        # �Œ�{�����̃}�[�N����ʁF�Œ�{������̂����
        # �{���␳���̃}�[�N����ʁF�{���␳�ォ��̂����
        pAlignParam.mkMaxVal = 0
        for i in range(pMarkInfo.num):
            pAlignParam.mkdx[i] = dist_dx[i]
            pAlignParam.mkdy[i] = dist_dy[i]
            pAlignParam.mkdr[i] = dist_dr[i]
            
            #[S] #1487 3�_�A���C�����g�Ή�	
            if  pAlignParam.mkdr[i] == 88888888 :
                continue
            
            #[E] #1487 3�_�A���C�����g�Ή�
            if pAlignParam.mkdr[i] > pAlignParam.mkMaxVal:
                pAlignParam.mkMaxIdx = i
                pAlignParam.mkMaxVal = pAlignParam.mkdr[i]
            
        

        # �c�ݕ␳�ʂ̐ݒ�
        if 	pDirection.scalingMode==RPL_SCALING_FIX and pMarkInfo.num==4 :	# �Œ�{�����S�_�}�[�N��-�w��c�ݗʂ��̗p
            for i in range(pMarkInfo.num):
                dx[i] = pDirection.dx[i]				# �w�肳�ꂽ�c�ݗ�X�����
                dy[i] = pDirection.dy[i]				# �w�肳�ꂽ�c�ݗ�Y�����
                dr[i] = math.math.sqrt(dx[i]*dx[i]+dy[i]*dy[i])
        # ���̑��͋�`����̘c�ݗʂ��̗p
        else:
            for i in range(pMarkInfo.num):
                dx[i] = dist_dx[i]
                dy[i] = dist_dy[i]
                dr[i] =	dist_dr[i]

        # �o�C���j�A�c�ݕ␳�p�����[�^�̏�����
        pVecotorParam.rx[0] = 0	
        pVecotorParam.ry[0] = 0

        pVecotorParam.rx[1] = 0	
        pVecotorParam.ry[1] = 0

        pVecotorParam.rx[2] = 0	
        pVecotorParam.ry[2] = 0

        pVecotorParam.rx[3] = 0	
        pVecotorParam.ry[3] = 0

        pVecotorParam.rdx[0] = 0
        pVecotorParam.rdy[0] = 0

        pVecotorParam.rdx[1] = 0
        pVecotorParam.rdy[1] = 0

        pVecotorParam.rdx[2] = 0
        pVecotorParam.rdy[2] = 0

        pVecotorParam.rdx[3] = 0
        pVecotorParam.rdy[3] = 0


        # I dont get what is the reason of up until now does they add the 4 constant
        if (pDirection.scalingMode==RPL_SCALING_FIX or		# �Œ�X�P�[�����O
                pDirection.scalingMode==RPL_DIST_AFFINE or		# ���s�l�ӌ`
                pDirection.scalingMode== RPL_DIST_BILINEAR ) and  bDistSW and pMarkInfo.num==4 :				# �c�ݕ␳SW�L�����S�_�A���C�����g
            rx = np.zeros((4, 1), dtype=float)
            ry = np.zeros((4, 1), dtype=float)
            rdx = np.zeros((4, 1), dtype=float)
            rdy = np.zeros((4, 1), dtype=float)
            xlm = 0
            ylm = 0 

            # �c�ݗʒ���(Ver0.14�ł��̈ʒu�֕ύX)
            ret = self.AdjustDistParam(	pecLogFD,
                                    pDirection.distAdjustment,
                                    pDirection.distAnnularing,
                                    pDirection.Dlimit_start,
                                    pDirection.Dlimit_max,
                                    dx,dy,dxAdj,dyAdj )
            if ret != ERR_ALIGNMENT_NOERR:
                return ret

            # ���s�l�ӌ`���c�ݕ␳�p�����[�^(P1[3]=0,P2[3]=0)
            if 	pDirection.scalingMode == RPL_DIST_AFFINE :
                ret = self.CalDistCorrectByAffine(pecLogFD,4,xl,yl,dxAdj,dyAdj)
                if ret!=ERR_ALIGNMENT_NOERR:
                    return ret

            # ���O�o��
            for i in range(pMarkInfo.num):
                dr = math.sqrt(dxAdj[i]*dxAdj[i]+dyAdj[i]*dyAdj[i])

            # �C�Ӌ�`�̈�ł̘c�ݗʂ̎Z�o
            ret = self.CalDistCorrectByBilinear(pecLogFD,4, xl, yl, xml, yml, dxAdj, dyAdj, rx, ry, rdx, rdy )
            if ret!=ERR_ALIGNMENT_NOERR:
                return ret

            # ���O�o��
            for i in range(pMarkInfo.num):
                dr = math.math.sqrt(rdx[i]*rdx[i]+rdy[i]*rdy[i])

            
            for i in range(4):
                ddx = (	(rx[3]-xl[i])*(ry[3]-yl[i])*rdx[0] - 
                        (rx[2]-xl[i])*(ry[2]-yl[i])*rdx[1] -
                        (rx[1]-xl[i])*(ry[1]-yl[i])*rdx[2] +
                        (rx[0]-xl[i])*(ry[0]-yl[i])*rdx[3] ) / ((rx[3]-rx[0])*(ry[3]-ry[0]))
                ddy = (	(rx[3]-xl[i])*(ry[3]-yl[i])*rdy[0] - 
                        (rx[2]-xl[i])*(ry[2]-yl[i])*rdy[1] -
                        (rx[1]-xl[i])*(ry[1]-yl[i])*rdy[2] +
                        (rx[0]-xl[i])*(ry[0]-yl[i])*rdy[3] ) / ((rx[3]-rx[0])*(ry[3]-ry[0]))
                xlm = (kx*xl[i]+ddx) * math.cos(theta) - (ky*yl[i]+ddy) * math.sin(theta) + ofsx
                ylm = (kx*xl[i]+ddx) * math.sin(theta) + (ky*yl[i]+ddy) * math.cos(theta) + ofsy

                delta_x = xm[i]-xlm
                delta_y = ym[i]-ylm


            pVecotorParam.rx[0] = llround(rx[0])
            pVecotorParam.ry[0] = llround(ry[0])
            pVecotorParam.rx[1] = llround(rx[1])
            pVecotorParam.ry[1] = llround(ry[1])
            pVecotorParam.rx[2] = llround(rx[2])
            pVecotorParam.ry[2] = llround(ry[2])
            pVecotorParam.rx[3] = llround(rx[3])
            pVecotorParam.ry[3] = llround(ry[3])

            pVecotorParam.rdx[0] = llround(rdx[0])
            pVecotorParam.rdy[0] = llround(rdy[0])
            pVecotorParam.rdx[1] = llround(rdx[1])
            pVecotorParam.rdy[1] = llround(rdy[1])
            pVecotorParam.rdx[2] = llround(rdx[2])
            pVecotorParam.rdy[2] = llround(rdy[2])
            pVecotorParam.rdx[3] = llround(rdx[3])
            pVecotorParam.rdy[3] = llround(rdy[3])

            # �摜�ϊ��s��(P1[0]-P1[3],P2[0]-P2[0])�̐���
            ss = (rx[3]-rx[0])*(ry[3]-ry[0])
            pVecotorParam.p1[0] = (rdx[0]*rx[3]*ry[3]-rdx[1]*rx[2]*ry[2]-rdx[2]*rx[1]*ry[1]+rdx[3]*rx[0]*ry[0]) / ss
            pVecotorParam.p1[1] = (-rdx[0]*ry[3]+rdx[1]*ry[2]+rdx[2]*ry[1]-rdx[3]*ry[0]) / ss
            pVecotorParam.p1[2] = (-rdx[0]*rx[3]+rdx[1]*rx[2]+rdx[2]*rx[1]-rdx[3]*rx[0]) / ss
            pVecotorParam.p1[3] = (rdx[0]-rdx[1]-rdx[2]+rdx[3]) / ss

            pVecotorParam.p2[0] = (rdy[0]*rx[3]*ry[3]-rdy[1]*rx[2]*ry[2]-rdy[2]*rx[1]*ry[1]+rdy[3]*rx[0]*ry[0]) / ss
            pVecotorParam.p2[1] = (-rdy[0]*ry[3]+rdy[1]*ry[2]+rdy[2]*ry[1]-rdy[3]*ry[0]) / ss
            pVecotorParam.p2[2] = (-rdy[0]*rx[3]+rdy[1]*rx[2]+rdy[2]*rx[1]-rdy[3]*rx[0]) / ss
            pVecotorParam.p2[3] = (rdy[0]-rdy[1]-rdy[2]+rdy[3]) / ss

            # �}�[�N����l�̍ĎZ�o!=�c�ݕ␳��͂���ʂ��������Ȃ�
            for i in range(pMarkInfo.num):
                ddx = (		(rx[3]-xl[i])*(ry[3]-yl[i])*rdx[0] - 
                            (rx[2]-xl[i])*(ry[2]-yl[i])*rdx[1] -
                            (rx[1]-xl[i])*(ry[1]-yl[i])*rdx[2] +
                            (rx[0]-xl[i])*(ry[0]-yl[i])*rdx[3] ) / ((rx[3]-rx[0])*(ry[3]-ry[0]))
                ddy = (		(rx[3]-xl[i])*(ry[3]-yl[i])*rdy[0] - 
                            (rx[2]-xl[i])*(ry[2]-yl[i])*rdy[1] -
                            (rx[1]-xl[i])*(ry[1]-yl[i])*rdy[2] +
                            (rx[0]-xl[i])*(ry[0]-yl[i])*rdy[3] ) / ((rx[3]-rx[0])*(ry[3]-ry[0]))
                dx[i] = xml[i] - (xl[i] * kx + ddx)
                dy[i] = yml[i] - (yl[i] * ky + ddy)
                dr[i] = math.sqrt(dx[i]*dx[i]+dy[i]*dy[i])
            
        else: 		
            # RPL_SCALING_AUTO
            # �p�����[�^����
            for i in range(pMarkInfo.num):
                xlm = (kx*xl[i]) * math.cos(theta) - (ky*yl[i]) * math.sin(theta) + ofsx
                ylm = (kx*xl[i]) * math.sin(theta) + (ky*yl[i]) * math.cos(theta) + ofsy
                delta_x = xm[i]-xlm
                delta_y = ym[i]-ylm
                # �}�[�N����l�̍Đݒ�
                dx[i] = dist_dx[i]
                dy[i] = dist_dy[i]
                dr[i] = dist_dr[i]

        # �\���E���J����p�̉�]��ݒ�
        pAlignParam.kx = kxMes
        pAlignParam.ky = kyMes
        pAlignParam.theta = theta

        # ����ő�l�Ƌ��e�l�̒ǉ�
        pAlignParam.mkMaxCorrErrIdx = 0
        pAlignParam.mkMaxCorrErrVal = 0
        for i in range(pMarkInfo.num):
            # �摜�����c��
            pAlignParam.mkCorrErrdx[i] =dx[i]
            pAlignParam.mkCorrErrdy[i] =dy[i]
            pAlignParam.mkCorrErrdr[i] =dr[i]
            # �摜�����␳��
            pAlignParam.mkCorrValdx[i] =dxAdj[i]
            pAlignParam.mkCorrValdy[i] =dyAdj[i]
            pAlignParam.mkCorrValdr[i] =math.sqrt(dxAdj[i]*dxAdj[i]+dyAdj[i]*dyAdj[i])

            if pAlignParam.mkCorrErrdr[i]>pAlignParam.mkMaxCorrErrVal:
                pAlignParam.mkMaxCorrErrIdx = i
                pAlignParam.mkMaxCorrErrVal = pAlignParam.mkCorrErrdr[i]
            

            if pAlignParam.mkCorrValdr[i]>pAlignParam.mkMaxCorrValVal:
                pAlignParam.mkMaxCorrValIdx = i
                pAlignParam.mkMaxCorrValVal = pAlignParam.mkCorrErrdr[i]
            

            # �p�����[�^�̌���
            vfy_x = pAlignParam.mkdx[i] - ( pAlignParam.mkCorrErrdx[i] + pAlignParam.mkCorrValdx[i] )
            vfy_y = pAlignParam.mkdy[i] - ( pAlignParam.mkCorrErrdy[i] + pAlignParam.mkCorrValdy[i] )

            if  vfy_x < -0.1 or 0.1 < vfy_x:
                return ERR_ALIGNMENT_VFY_CORR_ERR_VAL_X
            
            if  vfy_y < -0.1 or 0.1 < vfy_y:
                return ERR_ALIGNMENT_VFY_CORR_ERR_VAL_Y

        # �o�͕ϐ��֌��ʂ̊i�[
        pVecotorParam.theta = theta
        pVecotorParam.kx = kx
        pVecotorParam.ky = ky
        pVecotorParam.ofsx = llround(ofsx)
        pVecotorParam.ofsy = llround(ofsy)

        return	ret


    def CalThetaKxKyOfsFor2Points(self, pecLogFD,    xl,    yl,    xm,    ym,     theta,     kx,     ky,     ofsx,     ofsy):
    	# �d�S�̎Z�o
        gxl = (xl[0] + xl[1]) / 2
        gyl = (yl[0] + yl[1]) / 2
        gxm = (xm[0] + xm[1]) / 2
        gym = (ym[0] + ym[1]) / 2

        # �{���Z�o
        DX = xl[1] - xl[0]
        DY = yl[1] - yl[0]
        MX = xm[1] - xm[0]
        MY = ym[1] - ym[0]
        if kx<0.000001 and ky<0.000001 : 
            kx = ky = math.sqrt(MX * MX + MY * MY) / math.sqrt(DX * DX + DY * DY)
        

        # ���ςɂ���]�ʎZ�o
        # XY�{������l�����邽�ߔ{�����|����
        DX *= kx
        DY *= ky
        MX = xm[1] - xm[0]
        MY = ym[1] - ym[0]

        # ���ς����]�p�x�p�x���v�Z */
        DD = math.sqrt(DX * DX + DY * DY)
        MD = math.sqrt(MX * MX + MY * MY)
        if DD*MD<0.000001:
            return ERR_ALIGNMENT_POINT_VAL_ERR
        
        theta = math.acos( (DX * MX + DY * MY) / (DD * MD) )

        # �O�ς����]���������� */
        DxM = DX * MY - DY * MX
        if DxM < 0 :
            theta *= -1 
        

        # �݌v�d�S�̔{����]�ɂ��ړ��ʂ��Z�o
        gxl_mov = kx * gxl * math.cos(theta) - ky * gyl * math.sin(theta)
        gyl_mov = kx * gxl * math.sin(theta) + ky * gyl * math.cos(theta)

        ofsx = gxm - gxl_mov
        ofsy = gym - gyl_mov

        # �Z�o�p�����[�^�̌���
        xml[0] = kx * xl[0] * math.cos(theta) - ky * yl[0] * math.sin(theta) + ofsx
        yml[0] = kx * xl[0] * math.sin(theta) + ky * yl[0] * math.cos(theta) + ofsy
        xml[1] = kx * xl[1] * math.cos(theta) - ky * yl[1] * math.sin(theta) + ofsx
        yml[1] = kx * xl[1] * math.sin(theta) + ky * yl[1] * math.cos(theta) + ofsy

        # ��]�p�x����v���邱�Ƃ̊m�F
        MDX = xml[1] - xml[0]
        MDY = yml[1] - yml[0]
        # ���ς����]�p�x�p�x���v�Z�B�p�x����v���Ă��邩����
        verify_theta = math.acos( (MDX * MX + MDY * MY) / (math.sqrt(MDX * MDX + MDY * MDY) * math.sqrt(MX * MX + MY * MY)) )
        if verify_theta<-0.000001 or 0.000001<verify_theta:
            print("[ER] verify_error: theta=%lf (Out of range=+/-0.000001)",verify_theta)
            return ERR_ALIGNMENT_VERIFY_THETA
        
        # �v�������ƕϊ������̍��v�̌���
        err0 = math.sqrt((xml[0]-xm[0])*(xml[0]-xm[0])+(yml[0]-ym[0])*(yml[0]-ym[0]))
        err1 = math.sqrt((xml[1]-xm[1])*(xml[1]-xm[1])+(yml[1]-ym[1])*(yml[1]-ym[1]))
        lml  = math.sqrt((xml[1]-xml[0])*(xml[1]-xml[0])+(yml[1]-yml[0])*(yml[1]-yml[0]))

        #ll   = math.sqrt((xl[1]-xl[0])*(xl[1]-xl[0])+(yl[1]-yl[0])*(yl[1]-yl[0]))
        lm   = math.sqrt((xm[1]-xm[0])*(xm[1]-xm[0])+(ym[1]-ym[0])*(ym[1]-ym[0]))

        verify_dist0 = abs(err1 - err0)
        if verify_dist0>0.0001:
            print("[ER] Verify error: %lf verify dist (err1=%lf,err2=%lf) (Out of range=+/-0.0001)\n", verify_dist0, err1, err0)
            return  ERR_ALIGNMENT_VERIFY_DIST
        
        if lm>lml:
            verify_dist1 = abs(lml+err0+err1-lm)
        else:
            verify_dist1 = abs(lm+err0+err1-lml)
        
        if verify_dist1>0.1:
            print("[ER] Verify error: %lf (lml=%lf,lm=%lf,err1=%lf,err2=%lf) (Out of range=+/-0.1)\n",verify_dist1,lml, lm, err1, err0)
            return  ERR_ALIGNMENT_VERIFY_DIST

        return ERR_ALIGNMENT_NOERR

    def CalThetaKxKyOfsByLSM(self, pecLogFD, num, xl, yl, xm, ym, theta, kx,ky, ofsx, ofsy):
    	# �����ϐ�
        self.xxl = np.zeros((MAX_MARK_NUM, 1), dtype=float)
        self.yyl = np.zeros((MAX_MARK_NUM, 1), dtype=float)
        self.xxm = np.zeros((MAX_MARK_NUM, 1), dtype=float)
        self.yym = np.zeros((MAX_MARK_NUM, 1), dtype=float)
        
                    
        # �݌v�l�Ǝ����_�̏d�S���W���Z�o
        gxl = 0
        gyl = 0
        gxm = 0
        gym = 0
        #[S] #1487 3�_�A���C�����g�Ή�
        tmpNum
        tmpNum = num
        for i in range(num):
            if xm[i] == 88888888 :
                tmpNum -= 1
                continue
            gxl += xl[i]
            gyl += yl[i]
            gxm += xm[i]
            gym += ym[i]
        
        gxl = gxl / tmpNum
        gyl = gyl / tmpNum
        gxm = gxm / tmpNum
        gym = gym / tmpNum

        # �݌v�l�Ǝ����l�̏d�S�����_�ֈړ�
        for i in range(num):
            if  xm[i] == 88888888 :
                self.xxl[i] = xl[i]
                self.yyl[i] = yl[i]
                self.xxm[i] = xm[i]
                self.yym[i] = ym[i]
            else :
                #[E] #1487 3�_�A���C�����g�Ή�
                self.xxl[i] = xl[i] - gxl       #�݌v�l���W�ړ�
                self.yyl[i] = yl[i] - gyl
                self.xxm[i] = xm[i] - gxm       #�����l���W�ړ�
                self.yym[i] = ym[i] - gym
                

        # double�v�Z�p�e���|����
        A=0
        B=0
        C=0
        D=0
        E=0
        F=0
        G=0

        # �Ɖ�]�ʂ����߂� 1���
        for i in range(num):
            if xxm[i] == 88888888 :
                continue

            #[E] #1487 3�_�A���C�����g�Ή�
            A += self.xxl[i] * self.xxl[i]
            B += self.xxl[i] * self.yym[i]
            C += self.xxl[i] * self.xxm[i]
            D += self.yyl[i] * self.yyl[i]
            E += self.yyl[i] * self.xxm[i]
            F += self.yyl[i] * self.yym[i]
            G += self.xxm[i] * self.xxm[i] + self.yym[i] * self.yym[i]

        if abs(A * D * G - D * B * B - A * E * E) < 0.0000000001:
            print("[FL] Cal theta fault(1): div by zero\n")
            return ERR_ALIGNMENT_LSM_THETA
    
        dTheta1 = (B * C * D - A * E * F) / (A * D * G - D * B * B - A * E * E)

        # �Ɖ�]�ʂ����߂� 2���
        A = 0
        B = 0
        C = 0
        D = 0
        E = 0
        F = 0
        G = 0
        for i in range(num):
            if xxm[i] == 88888888 :
                continue
            xm_tmp = xxm[i] * math.cos(-dTheta1) - yym[i] * math.sin(-dTheta1)
            ym_tmp = xxm[i] * math.sin(-dTheta1) + yym[i] * math.cos(-dTheta1)
            A += self.xxl[i] * self.xxl[i]
            B += self.xxl[i] * ym_tmp
            C += self.xxl[i] * xm_tmp
            D += self.yyl[i] * self.yyl[i]
            E += self.yyl[i] * xm_tmp
            F += self.yyl[i] * ym_tmp
            G += self.xxm[i] * xm_tmp + self.yym[i] * ym_tmp
        
        if abs(A * D * G - D * B * B - A * E * E) < 0.0000000001:
            print("[ER] Cal theta fault(2): div by zero\n")
            return ERR_ALIGNMENT_LSM_THETA
        

        if kx<0.000001 and ky<0.000001:
            kx = (C * D * G - B * E * F - C * E * E) / (A * D * G - D * B * B - A * E * E)
            ky = (A * G * F - B * C * E - F * B * B) / (A * D * G - D * B * B - A * E * E)
        

        dTheta2 = (B * C * D - A * E * F) / (A * D * G - D * B * B - A * E * E)

        theta = dTheta1 + dTheta2
    
        # �݌v�d�S�̔{����]�ɂ��ړ��ʂ��Z�o
        gxl_mov = kx * gxl * math.cos(*theta) - ky * gyl * math.sin(theta)
        gyl_mov = kx * gxl * math.sin(*theta) + ky * gyl * math.cos(theta)

        ofsx = gxm - gxl_mov
        ofsy = gym - gyl_mov

        return ERR_ALIGNMENT_NOERR


    def AdjustDistParam(self, pecLogFD, adjustment, annularing, D_limit_start, D_limit_max, dx, dy, dxAdj, dyAdj):
        
        if (adjustment<0.0 or 100.0<adjustment):
            print("[ER] error: Invalid dist adjustment(Adj=%5.3lf)\n",adjustment)
            return ERR_ALIGNMENT_DIST_ADJUST_ERROR
        

        # �c�ݗʂ̒���
        
        dr = np.zeros((4, 1), dtype=float)
        drAdj = np.zeros((4, 1), dtype=float)
        drr = 0

        print("AdjustDistParam(Adj=%5.3lf, AL=%d[0.01um], Dlimit_start=%d, Dlimit_max=%d)\n", adjustment, annularing,D_limit_start, D_limit_max)
        for i in range(4):
            dxAdj[i] = 0.0
            dyAdj[i] = 0.0
            dr[i] = math.sqrt(dx[i]*dx[i]+dy[i]*dy[i])

            if dr[i]<0.000001: 
                continue

            # �c�ݕ␳����
            drr = adjustment / 100.0 * (dr[i] - D_limit_start)
            dxAdj[i] = dx[i] * drr / dr[i]
            dyAdj[i] = dy[i] * drr / dr[i]
            drAdj[i] = math.sqrt(dxAdj[i]*dxAdj[i]+dyAdj[i]*dyAdj[i])

            # �c�ݕ␳�J�n�l�܂ł�0�Ƃ���B
            if drr<0:
                print("[2-%2d] Dist limit(start) : drr(%8.0lf)=dr(%8.0lf) - limit_start(%d)\n",i,drr,dr[i],D_limit_start)
                dxAdj[i] = 0.0
                dyAdj[i] = 0.0
                drAdj[i] = 0.0
            
            print("[1-%2d] Dist Adj: dx(%8.0lf->%8.0lf), dy(%8.0lf->%8.0lf), dr(%8.0lf->%8.0lf)\n",
                        i,dx[i],dxAdj[i],dy[i],dyAdj[i],dr[i],drAdj[i])

            # �A�j���������O
            if (dr[i]-drAdj[i])>annularing and dr[i]>0.000001:
                dxAdj[i] = dx[i] - dx[i] * annularing / dr[i]	# dx[i] * (dr-annularing)/dr
                dyAdj[i] = dy[i] - dy[i] * annularing / dr[i] # dy[i] * (dr-annularing)/dr
                drAdj[i] = math.sqrt(dxAdj[i]*dxAdj[i]+dyAdj[i]*dyAdj[i])
                print("[3-%2d] Keep AL : dx(%8.0lf->%8.0lf), dy(%8.0lf->%8.0lf), dr(%8.0lf->%8.0lf)\n",i,dx[i],dxAdj[i],dy[i],dyAdj[i],dr[i],drAdj[i])
            

            # �c�ݕ␳����
            if D_limit_max>0.000001 and drAdj[i]>D_limit_max:
                print("[4-%2d] Dist limit(max) : drAdj(%3.2f) > Dlimit_max(%d)\n",i,drAdj[i],D_limit_max)
                dxAdj[i] = dx[i] * D_limit_max / dr[i]
                dyAdj[i] = dy[i] * D_limit_max / dr[i]
                drAdj[i] = math.sqrt(dxAdj[i]*dxAdj[i]+dyAdj[i]*dyAdj[i])
                print("[4-%2d] Dist limit(max) : dx(%8.0lf->%8.0lf), dy(%8.0lf->%8.0lf), dr(%8.0lf->%8.0lf)\n", i,dx[i],dxAdj[i],dy[i],dyAdj[i],dr[i],drAdj[i])

        # ���O�o��
        print("Distortion parameter adjust result\n")
        for i in range(4):
            print("[%2d] (%10.3lf, %10.3lf, %10.3lf)\n", i,dxAdj[i],dyAdj[i],drAdj[i])

        return ERR_ALIGNMENT_NOERR

    # /******************************************************************************
    # 	�o�C���j�A���(������)�ɂ��c�ݕ␳�p�����[�^�Z�o
    # ******************************************************************************/
    def CalDistCorrectByBilinear(self, pecLogFD, num, xl, yl, xlm, ylm, dx, dy, rx, ry, rdx, rdy ):
        # �ő��`�̈���Z�o
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

        # �ő��`�̈�ł̘c�ݗʂ��Z�o
        SA1 = np.zeros((4, 1), dtype=float)
        SA2 = np.zeros((4, 1), dtype=float)
        SA3 = np.zeros((4, 1), dtype=float)
        SA4 = np.zeros((4, 1), dtype=float)
        SS = (x_max-x_min) * (y_max-y_min)

        for i in range(4):
            SA1[i] = (x_max-xl[i])*(y_max-yl[i]) / SS
            SA2[i] = (xl[i]-x_min)*(y_max-yl[i]) / SS
            SA3[i] = (x_max-xl[i])*(yl[i]-y_min) / SS
            SA4[i] = (xl[i]-x_min)*(yl[i]-y_min) / SS
        

        A = {	SA1[0],SA2[0],SA3[0],SA4[0],
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

        ipvt = np.zeros((4*4, 1), dtype=float)

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

        # ���Z�p�c�ݕ␳�ʂ̌���
        vdx = np.zeros((4, 1), dtype=float)
        vdy = np.zeros((4, 1), dtype=float)
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

if __name__ == "__main__":
    pass
