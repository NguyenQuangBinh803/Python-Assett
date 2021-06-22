import numpy as np




N_BYTE_SEND_SIZE_MAX =	30000		# ���M�ő�T�C�Y [Byte] */
N_BYTE_MEC_SEND_SIZE_MAX =	1024	# ���J���M�ő�T�C�Y [Byte] */



# /*******************************************************************************
# 	�錾
# *******************************************************************************/

RPL_SCALING_FIX = 0             #	/* �w��X�P�[�����O					*/
RPL_SCALING_AUTO = 1            #	/* �I�[�g�X�P�[�����O					*/
RPL_DIST_BILINEAR = 2           #	/* �c�݃A���C�����g(���R�ό`�A��`)	*/
RPL_DIST_AFFINE = 3             #	/* �c�݃A���C�����g(���s�l�ӌ`)		*/

RPL_NON_ALIGNMENT = 0           #	/* �A���C�����g���� */
RPL_PLANE_MODE = 1          #	/* �ꊇ�A���C�����g */
RPL_DIV_MODE = 2            #	/* �����A���C�����g */

RPL_SCL_INDIVIDUAL = 0          #	/* �Ӟ�Ɨ��{��(��[�̈��RPL_SCL_PLANE�Ɠ���) */
RPL_SCL_AVE_AREA = 1            #	/* �Ӟ�{������	*/
RPL_SCL_PLANE = 2           #	/* ��{��			*/


#------------------------------
#	�A���C�����g
#------------------------------
#[S] TP#1907 LDIC�}�[�N�F���p�����[�^����
MAX_PRIORITY_NUM =		10													# #�}�[�N�T�uID��  #TP#2357 �}���`�e���v���[�g�̃T�u�}�[�N���g�� (5 -> 10)
#[E] TP#1907 LDIC�}�[�N�F���p�����[�^����
#[S] TP#2311 �{�́F�p�^�[���A���C�����g�Ή� STEP1
MAX_TEMPLATE_MARK_NUM =	400													# �e���v���[�g�摜�̍ő吔(#Windows��ALN��ALN_MAX_MARK_NUM�ɍ��킹�Ă���) 
#[E] TP#2311 �{�́F�p�^�[���A���C�����g�Ή� STEP1

PRECISION_PRIORITY_NUM =	5						#[S] TP#2519 �{�́F�}���`�e���v���[�g�̃T�u�}�[�N���g��_QV���XNG										# ���x�]���p�}�[�N�T�uID��(5�Œ�) #��PEC�ł̌��������ȍ~�Ŏg�p����B 


MAX_ALIGN_DIV =			2000							
#------------------------------
#[S] TP#1907 LDIC�}�[�N�F���p�����[�^����
MAX_PRIORITY_NUM =		10													# #�}�[�N�T�uID��  #TP#2357 �}���`�e���v���[�g�̃T�u�}�[�N���g�� (5 -> 10)
#[E] TP#1907 LDIC�}�[�N�F���p�����[�^����
#[S] TP#2311 �{�́F�p�^�[���A���C�����g�Ή� STEP1
MAX_TEMPLATE_MARK_NUM =	400													# �e���v���[�g�摜�̍ő吔(#Windows��ALN��ALN_MAX_MARK_NUM�ɍ��킹�Ă���) 
#[E] TP#2311 �{�́F�p�^�[���A���C�����g�Ή� STEP1

PRECISION_PRIORITY_NUM =	5						#[S] TP#2519 �{�́F�}���`�e���v���[�g�̃T�u�}�[�N���g��_QV���XNG										# ���x�]���p�}�[�N�T�uID��(5�Œ�) #��PEC�ł̌��������ȍ~�Ŏg�p����B 


MAX_ALIGN_DIV =			2000												# #�ő啪���� 
#[S] #1453 ���_�A���C�����g�Ή�
MAX_MARK_NUM_DIVIDE_AREA_PIECE =	4											# #piece�����̈���̍ő�}�[�N�� 

MAX_MARK_NUM_DIVIDE_AREA =800													# #�����̈���̍ő�}�[�N�� 
MAX_MARK_NUM =			( MAX_ALIGN_DIV * 4 )								# �ő�}�[�N�� : 2000 �~ #4�ŋL�ڂ��Ă��� 

MAX_ALIGN_DIV_MULTI =		200													# #�ő啪���� 
MAX_MARK_NUM_MULTI =		800													# #�ő�}�[�N�� 
#[S] TP#2520 ���_�A���C�����g�Ή�JOBLOG�ǉ�
MAX_MARK_INFO_NUM =		MAX_MARK_NUM										# �̈悲�ƃ}�[�N���̍ő吔�i�����_�ł�Piece��2000x4=#800���ő� 

MAX_MARK_PNT_MULTI =		( MAX_NTC_PEC_ALN_INF * 4 )							# �A���C�����g���ʒm�p #�ő�}�[�NID�� 
#[E] TP#2520 ���_�A���C�����g�Ή�JOBLOG�ǉ�
MAX_NTC_PEC_ALN_INF =		48													# �A���C�����g���ʒm�p #�ő�̈搔 
#[E] #1453 ���_�A���C�����g�Ή�

CAM_SEL_MAX_X_SHIFT_NUM =	50		# #X�V�t�g�ő吔 
CAM_SEL_MAX_Y_SHIFT_NUM =	30		# #Y�V�t�g�ő吔 

CAM_SEL_MAX_SHOT_NUM_CALIB =		40			# 1�X�L�����ł̍ő�B�e�� ( �J�����L�����u�A�����e�p #) 
CAM_SEL_MAX_SHOT_NUM =			1000		# #1�X�L�����ł̍ő�B�e�� 
CAM_SEL_MAX_SCAN_MARK_NUM =		1000		# #1�X�L�����ŎB�e����ő�}�[�N�� 

MAX_SCAN_SHOT_NUM_PIECE_ALIGNMENT =1000									# Peace�A���C�����g : #1�X�L�����ł̍ő�B�e�� 
MAX_SCAN_MARK_NUM_PIECE_ALIGNMENT =1000									# Peace�A���C�����g : #1�X�L�����ŎB�e����ő�}�[�N�� 
SHOT_AND_BLANK_NUM_PIECE_ALIGNMENT =1000									# Peace�A���C�����g : 1�X�L�����ŎB�e����ő�}�[�N�� + #���B�e�J�����̖��g�p�}�[�N�� 
																					# �� ���B�e�J�����̋󌂂��� ( �ő�3�� ) #���܂߂� 

COMMON_SEGMENT_MAXNUM =	50	# �Z�O�����g�L�� #�ő�� 

COMMON_RIP_SCALE_100_PERCENT =( 100 * 10000 )		# ��{�� 100% [0.0001#%] 


#------------------------------
#	�����_�����O�p�����[�^
#------------------------------
RENDERING_PARAM_DATA_SIZE =( N_BYTE_SEND_SIZE_MAX - 8 )		# �����_�����O�p�����[�^��Binary�f�[�^���̑��M�ő�T�C�Y [#Byte] 

# #�]�����@ 
# typedef enum
# {
# 	RENDERING_PARAM_TRANS_PF = 0,		# ����PF ( �����_�����O�p�����[�^�ʒm��Binary�f�[�^�œ]�� #) 
# 	RENDERING_PARAM_TRANS_FILE,			# #�t�@�C�� 
# 	RENDERING_PARAM_TRANS_NUM
# } RENDERING_PARAM_TRANS
RENDERING_PARAM_TRANS_PF = 0		# ����PF ( �����_�����O�p�����[�^�ʒm��Binary�f�[�^�œ]�� #) 
RENDERING_PARAM_TRANS_FILE = 1			# #�t�@�C�� 
RENDERING_PARAM_TRANS_NUM = 2


#------------------------------
	# �R�����g�p�����[�^
#------------------------------
COM_COMMENT_MAX =					3000# �R�����g�ő吔	# @014
COM_COMMENT_MIN =					1	# �R�����g�ŏ���

#------------------------------
	# �t�@�C���p�X
#------------------------------
#[S] TP#1672 Linux���̃e���v���[�g�ݒ�t�@�C��(ALNPRM.ini)���X�V����Ȃ�
# USR_PASS =		"/usr/"				# Tracker#692
# COMMON_SYSTEMDATA_DIR =	"/home/fujifilm/vecot/systemdata"
# COMMON_MARK_USER_DIR =	"/home/fujifilm/vecot/mark/usr"

# COMMON_FILE_PATH_ALNPRMSET_INI =			COMMON_MARK_USER_DIR "/ALNPRMSET.ini"
# COMMON_FILE_PATH_ALNPRM_INI =				COMMON_SYSTEMDATA_DIR "/ALNPRM.ini"
# #[E] TP#1672 Linux���̃e���v���[�g�ݒ�t�@�C��(ALNPRM.ini)���X�V����Ȃ�
# REMOTE_FILE_PATH_ALNPRMSET_INI =			REMOTE_MARK_USR_PATH "ALNPRMSET.ini"

# �� -- Start -- #1729 �J�����Ɩ��F�� ��I�t�Z�b�g�@�\�ǉ� ��

#------------------------------------------------------------
#* << �X�g���{��� >>
#------------------------------------------------------------
# enum OPTION_STROBE_KIND
# {
# 	STROBE_TYPE_1 = 0,		# �W���Ɩ��̏Ɩ��ԍ�
# 	STROBE_TYPE_2,			# �I�v�V�����Ɩ�1�̏Ɩ��ԍ�
# 	STROBE_TYPE_3,			# �I�v�V�����Ɩ�2�̏Ɩ��ԍ�
# 	MAX_OPTION_STROBE		# �X�g���{��ʐ�
# }

STROBE_TYPE_1 = 0	    	# �W���Ɩ��̏Ɩ��ԍ�
STROBE_TYPE_2 = 1			# �I�v�V�����Ɩ�1�̏Ɩ��ԍ�
STROBE_TYPE_3 = 2			# �I�v�V�����Ɩ�2�̏Ɩ��ԍ�
MAX_OPTION_STROBE = 3 		# �X�g���{��ʐ�

# �� --- End --- #1729 �J�����Ɩ��F�� ��I�t�Z�b�g�@�\�ǉ� ��

# #_SYSTEM_COMMON_H_ 



RPL_SCALING_FIX	=			0	#/* �w��X�P�[�����O					*/
RPL_SCALING_AUTO=			1	#/* �I�[�g�X�P�[�����O					*/
RPL_DIST_BILINEA=R			2	#/* �c�݃A���C�����g(���R�ό`�A��`)	*/
RPL_DIST_AFFINE	=			3	#/* �c�݃A���C�����g(���s�l�ӌ`)		*/

RPL_NON_ALIGNMENT		=	0	#/* �A���C�����g���� */
RPL_PLANE_MODE	=			1	#/* �ꊇ�A���C�����g */
RPL_DIV_MODE	=			2	#/* �����A���C�����g */

RPL_SCL_INDIVIDUAL =			0	#/* �Ӟ�Ɨ��{��(��[�̈��RPL_SCL_PLANE�Ɠ���) */
RPL_SCL_AVE_AREA=			1	#/* �Ӟ�{������	*/
RPL_SCL_PLANE	=			2	#/* ��{��			*/

from collections import namedtuple


class DivAlignInfo:
    def __init__(self):
        self.divnum_x = 0
        self.divnum_y = 0
        self.MARK_DT = 0
        self.divPoint = np.zeros((MAX_ALIGN_DIV,2), dtype=float)
        self.markNum = np.zeros((MAX_ALIGN_DIV), dtype=float)
        self.SCALE_T = 0
        self.scale = np.zeros((MAX_ALIGN_DIV), dtype=float)
        self.MARK_DIST = 0
        self.markDist = np.zeros((MAX_MARK_NUM), dtype=float)
        self.areaMarkInfo = np.zeros((MAX_MARK_NUM), dtype=float)
        self.markInfoIndex = np.zeros((MAX_ALIGN_DIV), dtype=float)
        self.areaScaleMode = 0
        self.boardScaleMode = 0



# typedef struct mark_info {
# 	int32_t		x;					// �}�[�NX���W[1/100um]
# 	int32_t		y;					// �}�[�NY���W[1/100um]
# } MARK_DT;
MARK_DT = namedtuple("MARK_DT", "x y")

# typedef struct scale_t {
# 	double		x;					//	X�{��(%)
# 	double		y;					//	Y�{��(%)
# } SCALE_T;
SCALE_T = namedtuple("SCALE_T", "x y")



# typedef struct {
# 	int				num;						// �}�[�N��
# 	double			xlog[MAX_MARK_NUM];			// �_�����WX [1/100um]
# 	double			ylog[MAX_MARK_NUM];			// �_�����WY [1/100um]
# 	double			xmes[MAX_MARK_NUM];			// �v�����WX [1/100um]
# 	double			ymes[MAX_MARK_NUM];			// �v�����WY [1/100um]
# } SMarkInfo;


SMarkInfo = namedtuple("SMarkInfo", "num xlog ylog xmes ymes")


# typedef struct {
# 	int				scalingMode;				// �X�P�[�����O���[�h(0,1,2)
# 	double			kx;							// X�����w��{�� kx[�{��]	
# 	double			ky;							// Y�����w��{�� ky[�{��]	
# 	double			dx[MAX_MARK_NUM];			// X�����w��c�ݕ␳�l
# 	double			dy[MAX_MARK_NUM];			// Y�����w��c�ݕ␳�l
# 	double			distAdjustment;				// �c�ݕ␳�����l(0�`100)[��]	
# 	int				distAnnularing;				// �c�ݕ␳�A�j���������O [1/100um]
# 	int				Dlimit_start;				// �c�ݕ␳�J�n�l[1/100um]
# 	int				Dlimit_max;					// �c�ݕ␳�����l[1/100um]
# } SDirection;
SDirection = namedtuple("SDirection", "scalingMode kx ky dx dy distAdjustment distAnnularing Dlimit_start Dlimit_max")



# typedef struct {
# 	int				ofsx;						// �I�t�Z�b�gofsx [1/100um]
# 	int				ofsy;						// �I�t�Z�b�gofsy [1/100um]
# 	double			theta;						// ��]��theta [rad]	
# 	double			kx;							// ��{�� kx
# 	double			ky;							// ��{�� ky
# 	int				gx;							// X�d�S
# 	int				gy;							// Y�d�S
# 	int				mkMaxIdx;					// �}�[�N����ő�l
# 	double			mkMaxVal;					// �}�[�N����ő�l			
# 	double			mkdx[MAX_MARK_NUM];			// �}�[�N�̃Y����dX [1/100um]
# 	double			mkdy[MAX_MARK_NUM];			// �}�[�N�̃Y����dY [1/100um]
# 	double			mkdr[MAX_MARK_NUM];			// �}�[�N�̃Y����de [1/100um]
# 	int				mkMaxCorrErrIdx;			// ����ő�l
# 	double			mkMaxCorrErrVal;			// ����ő�l
# 	double			mkCorrErrdx[MAX_MARK_NUM];	// �}�[�N�␳�c��dX [1/100um]
# 	double			mkCorrErrdy[MAX_MARK_NUM];	// �}�[�N�␳�c��dY [1/100um]
# 	double			mkCorrErrdr[MAX_MARK_NUM];	// �}�[�N�␳�c��de [1/100um]
# 	int				mkMaxCorrValIdx;			// �␳�ʍő�l
# 	double			mkMaxCorrValVal;			// �␳�ʍő�l
# 	double			mkCorrValdx[MAX_MARK_NUM];	// �}�[�N�␳�c��dX [1/100um]
# 	double			mkCorrValdy[MAX_MARK_NUM];	// �}�[�N�␳�c��dY [1/100um]
# 	double			mkCorrValdr[MAX_MARK_NUM];	// �}�[�N�␳�c��de [1/100um]
# } SAlignmentParam;

SAlignmentParam = namedtuple("SAlignmentParam", "ofsx ofsy theta kx ky gx gy mkMaxIdx mkMaxVal mkdx mkdy mkdr mkMaxCorrErrIdx mkMaxCorrErrVal mkCorrErrdx mkCorrErrdy mkCorrErrdr mkMaxCorrValIdx mkMaxCorrValVal mkCorrValdx mkCorrValdy mkCorrValdr")


# typedef struct {
# 	double			theta;						// ��]��theta [rad]	
# 	double			kx;							// �I���{�� kx
# 	double			ky;							// �I���{�� ky
# 	int				ofsx;						// �I�t�Z�b�gofsx
# 	int				ofsy;						// �I�t�Z�b�gofsy
# 	int				rx[4];						// ��`���_���Wrx [1/100um]
# 	int				ry[4];						// ��`���_���Wry [1/100um]
# 	int				rdx[4];						// ��`�̈撸�_�ł̃Y���␳��dx [1/100um]
# 	int				rdy[4];						// ��`�̈撸�_�ł̃Y���␳��dy [1/100um]
# 	double			p1[4];						// ��`�␳/���s�l�ӌ`�␳�p�p�����[�^
# 	double			p2[4];						// ��`�␳/���s�l�ӌ`�␳�p�p�����[�^
# } SVectorParam;
SVectorParam = namedtuple("SVectorParam","theta kx ky ofsx ofsy rx ry rdx rdy p1 p2")