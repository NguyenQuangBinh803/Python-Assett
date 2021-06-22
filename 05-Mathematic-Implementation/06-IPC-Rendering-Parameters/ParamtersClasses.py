import numpy as np




N_BYTE_SEND_SIZE_MAX =	30000		# 送信最大サイズ [Byte] */
N_BYTE_MEC_SEND_SIZE_MAX =	1024	# メカ送信最大サイズ [Byte] */



# /*******************************************************************************
# 	宣言
# *******************************************************************************/

RPL_SCALING_FIX = 0             #	/* 指定スケーリング					*/
RPL_SCALING_AUTO = 1            #	/* オートスケーリング					*/
RPL_DIST_BILINEAR = 2           #	/* 歪みアライメント(自由変形、台形)	*/
RPL_DIST_AFFINE = 3             #	/* 歪みアライメント(平行四辺形)		*/

RPL_NON_ALIGNMENT = 0           #	/* アライメント無し */
RPL_PLANE_MODE = 1          #	/* 一括アライメント */
RPL_DIV_MODE = 2            #	/* 分割アライメント */

RPL_SCL_INDIVIDUAL = 0          #	/* 個片領域独立倍率(基板端領域はRPL_SCL_PLANEと同じ) */
RPL_SCL_AVE_AREA = 1            #	/* 個片領域倍率平均	*/
RPL_SCL_PLANE = 2           #	/* 基板倍率			*/


#------------------------------
#	アライメント
#------------------------------
#[S] TP#1907 LDICマーク認識パラメータ調整
MAX_PRIORITY_NUM =		10													# #マークサブID数  #TP#2357 マルチテンプレートのサブマーク個数拡張 (5 -> 10)
#[E] TP#1907 LDICマーク認識パラメータ調整
#[S] TP#2311 本体：パターンアライメント対応 STEP1
MAX_TEMPLATE_MARK_NUM =	400													# テンプレート画像の最大数(#Windows版ALNのALN_MAX_MARK_NUMに合わせている) 
#[E] TP#2311 本体：パターンアライメント対応 STEP1

PRECISION_PRIORITY_NUM =	5						#[S] TP#2519 本体：マルチテンプレートのサブマーク個数拡張_QVレスNG										# 精度評価用マークサブID数(5固定) #※PECでの結合処理以降で使用する。 


MAX_ALIGN_DIV =			2000							
#------------------------------
#[S] TP#1907 LDICマーク認識パラメータ調整
MAX_PRIORITY_NUM =		10													# #マークサブID数  #TP#2357 マルチテンプレートのサブマーク個数拡張 (5 -> 10)
#[E] TP#1907 LDICマーク認識パラメータ調整
#[S] TP#2311 本体：パターンアライメント対応 STEP1
MAX_TEMPLATE_MARK_NUM =	400													# テンプレート画像の最大数(#Windows版ALNのALN_MAX_MARK_NUMに合わせている) 
#[E] TP#2311 本体：パターンアライメント対応 STEP1

PRECISION_PRIORITY_NUM =	5						#[S] TP#2519 本体：マルチテンプレートのサブマーク個数拡張_QVレスNG										# 精度評価用マークサブID数(5固定) #※PECでの結合処理以降で使用する。 


MAX_ALIGN_DIV =			2000												# #最大分割数 
#[S] #1453 多点アライメント対応
MAX_MARK_NUM_DIVIDE_AREA_PIECE =	4											# #piece分割領域内の最大マーク数 

MAX_MARK_NUM_DIVIDE_AREA =800													# #分割領域内の最大マーク数 
MAX_MARK_NUM =			( MAX_ALIGN_DIV * 4 )								# 最大マーク数 : 2000 × #4で記載しておく 

MAX_ALIGN_DIV_MULTI =		200													# #最大分割数 
MAX_MARK_NUM_MULTI =		800													# #最大マーク個数 
#[S] TP#2520 多点アライメント対応JOBLOG追加
MAX_MARK_INFO_NUM =		MAX_MARK_NUM										# 領域ごとマーク情報の最大数（現時点ではPieceの2000x4=#800が最大 

MAX_MARK_PNT_MULTI =		( MAX_NTC_PEC_ALN_INF * 4 )							# アライメント情報通知用 #最大マークID数 
#[E] TP#2520 多点アライメント対応JOBLOG追加
MAX_NTC_PEC_ALN_INF =		48													# アライメント情報通知用 #最大領域数 
#[E] #1453 多点アライメント対応

CAM_SEL_MAX_X_SHIFT_NUM =	50		# #Xシフト最大数 
CAM_SEL_MAX_Y_SHIFT_NUM =	30		# #Yシフト最大数 

CAM_SEL_MAX_SHOT_NUM_CALIB =		40			# 1スキャンでの最大撮影数 ( カメラキャリブ、メンテ用 #) 
CAM_SEL_MAX_SHOT_NUM =			1000		# #1スキャンでの最大撮影数 
CAM_SEL_MAX_SCAN_MARK_NUM =		1000		# #1スキャンで撮影する最大マーク数 

MAX_SCAN_SHOT_NUM_PIECE_ALIGNMENT =1000									# Peaceアライメント : #1スキャンでの最大撮影数 
MAX_SCAN_MARK_NUM_PIECE_ALIGNMENT =1000									# Peaceアライメント : #1スキャンで撮影する最大マーク数 
SHOT_AND_BLANK_NUM_PIECE_ALIGNMENT =1000									# Peaceアライメント : 1スキャンで撮影する最大マーク数 + #未撮影カメラの未使用マーク数 
																					# ※ 未撮影カメラの空撃ち数 ( 最大3回 ) #を含める 

COMMON_SEGMENT_MAXNUM =	50	# セグメント有効 #最大個数 

COMMON_RIP_SCALE_100_PERCENT =( 100 * 10000 )		# 基準倍率 100% [0.0001#%] 


#------------------------------
#	レンダリングパラメータ
#------------------------------
RENDERING_PARAM_DATA_SIZE =( N_BYTE_SEND_SIZE_MAX - 8 )		# レンダリングパラメータのBinaryデータ部の送信最大サイズ [#Byte] 

# #転送方法 
# typedef enum
# {
# 	RENDERING_PARAM_TRANS_PF = 0,		# 共通PF ( レンダリングパラメータ通知のBinaryデータで転送 #) 
# 	RENDERING_PARAM_TRANS_FILE,			# #ファイル 
# 	RENDERING_PARAM_TRANS_NUM
# } RENDERING_PARAM_TRANS
RENDERING_PARAM_TRANS_PF = 0		# 共通PF ( レンダリングパラメータ通知のBinaryデータで転送 #) 
RENDERING_PARAM_TRANS_FILE = 1			# #ファイル 
RENDERING_PARAM_TRANS_NUM = 2


#------------------------------
	# コメントパラメータ
#------------------------------
COM_COMMENT_MAX =					3000# コメント最大数	# @014
COM_COMMENT_MIN =					1	# コメント最小数

#------------------------------
	# ファイルパス
#------------------------------
#[S] TP#1672 Linux側のテンプレート設定ファイル(ALNPRM.ini)が更新されない
# USR_PASS =		"/usr/"				# Tracker#692
# COMMON_SYSTEMDATA_DIR =	"/home/fujifilm/vecot/systemdata"
# COMMON_MARK_USER_DIR =	"/home/fujifilm/vecot/mark/usr"

# COMMON_FILE_PATH_ALNPRMSET_INI =			COMMON_MARK_USER_DIR "/ALNPRMSET.ini"
# COMMON_FILE_PATH_ALNPRM_INI =				COMMON_SYSTEMDATA_DIR "/ALNPRM.ini"
# #[E] TP#1672 Linux側のテンプレート設定ファイル(ALNPRM.ini)が更新されない
# REMOTE_FILE_PATH_ALNPRMSET_INI =			REMOTE_MARK_USR_PATH "ALNPRMSET.ini"

# ▼ -- Start -- #1729 カメラ照明色毎 基板オフセット機能追加 ▼

#------------------------------------------------------------
#* << ストロボ種別 >>
#------------------------------------------------------------
# enum OPTION_STROBE_KIND
# {
# 	STROBE_TYPE_1 = 0,		# 標準照明の照明番号
# 	STROBE_TYPE_2,			# オプション照明1の照明番号
# 	STROBE_TYPE_3,			# オプション照明2の照明番号
# 	MAX_OPTION_STROBE		# ストロボ種別数
# }

STROBE_TYPE_1 = 0	    	# 標準照明の照明番号
STROBE_TYPE_2 = 1			# オプション照明1の照明番号
STROBE_TYPE_3 = 2			# オプション照明2の照明番号
MAX_OPTION_STROBE = 3 		# ストロボ種別数

# ▲ --- End --- #1729 カメラ照明色毎 基板オフセット機能追加 ▲

# #_SYSTEM_COMMON_H_ 



RPL_SCALING_FIX	=			0	#/* 指定スケーリング					*/
RPL_SCALING_AUTO=			1	#/* オートスケーリング					*/
RPL_DIST_BILINEA=R			2	#/* 歪みアライメント(自由変形、台形)	*/
RPL_DIST_AFFINE	=			3	#/* 歪みアライメント(平行四辺形)		*/

RPL_NON_ALIGNMENT		=	0	#/* アライメント無し */
RPL_PLANE_MODE	=			1	#/* 一括アライメント */
RPL_DIV_MODE	=			2	#/* 分割アライメント */

RPL_SCL_INDIVIDUAL =			0	#/* 個片領域独立倍率(基板端領域はRPL_SCL_PLANEと同じ) */
RPL_SCL_AVE_AREA=			1	#/* 個片領域倍率平均	*/
RPL_SCL_PLANE	=			2	#/* 基板倍率			*/

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
# 	int32_t		x;					// マークX座標[1/100um]
# 	int32_t		y;					// マークY座標[1/100um]
# } MARK_DT;
MARK_DT = namedtuple("MARK_DT", "x y")

# typedef struct scale_t {
# 	double		x;					//	X倍率(%)
# 	double		y;					//	Y倍率(%)
# } SCALE_T;
SCALE_T = namedtuple("SCALE_T", "x y")



# typedef struct {
# 	int				num;						// マーク個数
# 	double			xlog[MAX_MARK_NUM];			// 論理座標X [1/100um]
# 	double			ylog[MAX_MARK_NUM];			// 論理座標Y [1/100um]
# 	double			xmes[MAX_MARK_NUM];			// 計測座標X [1/100um]
# 	double			ymes[MAX_MARK_NUM];			// 計測座標Y [1/100um]
# } SMarkInfo;


SMarkInfo = namedtuple("SMarkInfo", "num xlog ylog xmes ymes")


# typedef struct {
# 	int				scalingMode;				// スケーリングモード(0,1,2)
# 	double			kx;							// X方向指定倍率 kx[倍率]	
# 	double			ky;							// Y方向指定倍率 ky[倍率]	
# 	double			dx[MAX_MARK_NUM];			// X方向指定歪み補正値
# 	double			dy[MAX_MARK_NUM];			// Y方向指定歪み補正値
# 	double			distAdjustment;				// 歪み補正調整値(0～100)[％]	
# 	int				distAnnularing;				// 歪み補正アニュラリング [1/100um]
# 	int				Dlimit_start;				// 歪み補正開始値[1/100um]
# 	int				Dlimit_max;					// 歪み補正制限値[1/100um]
# } SDirection;
SDirection = namedtuple("SDirection", "scalingMode kx ky dx dy distAdjustment distAnnularing Dlimit_start Dlimit_max")



# typedef struct {
# 	int				ofsx;						// オフセットofsx [1/100um]
# 	int				ofsy;						// オフセットofsy [1/100um]
# 	double			theta;						// 回転量theta [rad]	
# 	double			kx;							// 基板倍率 kx
# 	double			ky;							// 基板倍率 ky
# 	int				gx;							// X重心
# 	int				gy;							// Y重心
# 	int				mkMaxIdx;					// マークずれ最大値
# 	double			mkMaxVal;					// マークずれ最大値			
# 	double			mkdx[MAX_MARK_NUM];			// マークのズレ量dX [1/100um]
# 	double			mkdy[MAX_MARK_NUM];			// マークのズレ量dY [1/100um]
# 	double			mkdr[MAX_MARK_NUM];			// マークのズレ量de [1/100um]
# 	int				mkMaxCorrErrIdx;			// ずれ最大値
# 	double			mkMaxCorrErrVal;			// ずれ最大値
# 	double			mkCorrErrdx[MAX_MARK_NUM];	// マーク補正残差dX [1/100um]
# 	double			mkCorrErrdy[MAX_MARK_NUM];	// マーク補正残差dY [1/100um]
# 	double			mkCorrErrdr[MAX_MARK_NUM];	// マーク補正残差de [1/100um]
# 	int				mkMaxCorrValIdx;			// 補正量最大値
# 	double			mkMaxCorrValVal;			// 補正量最大値
# 	double			mkCorrValdx[MAX_MARK_NUM];	// マーク補正残差dX [1/100um]
# 	double			mkCorrValdy[MAX_MARK_NUM];	// マーク補正残差dY [1/100um]
# 	double			mkCorrValdr[MAX_MARK_NUM];	// マーク補正残差de [1/100um]
# } SAlignmentParam;

SAlignmentParam = namedtuple("SAlignmentParam", "ofsx ofsy theta kx ky gx gy mkMaxIdx mkMaxVal mkdx mkdy mkdr mkMaxCorrErrIdx mkMaxCorrErrVal mkCorrErrdx mkCorrErrdy mkCorrErrdr mkMaxCorrValIdx mkMaxCorrValVal mkCorrValdx mkCorrValdy mkCorrValdr")


# typedef struct {
# 	double			theta;						// 回転量theta [rad]	
# 	double			kx;							// 露光倍率 kx
# 	double			ky;							// 露光倍率 ky
# 	int				ofsx;						// オフセットofsx
# 	int				ofsy;						// オフセットofsy
# 	int				rx[4];						// 矩形頂点座標rx [1/100um]
# 	int				ry[4];						// 矩形頂点座標ry [1/100um]
# 	int				rdx[4];						// 矩形領域頂点でのズレ補正量dx [1/100um]
# 	int				rdy[4];						// 矩形領域頂点でのズレ補正量dy [1/100um]
# 	double			p1[4];						// 台形補正/平行四辺形補正用パラメータ
# 	double			p2[4];						// 台形補正/平行四辺形補正用パラメータ
# } SVectorParam;
SVectorParam = namedtuple("SVectorParam","theta kx ky ofsx ofsy rx ry rdx rdy p1 p2")